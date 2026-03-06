import streamlit as st
import numpy as np
import pandas as pd
import joblib
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import shap
from sklearn.metrics import roc_curve, auc

# -----------------------
# Load model and data
# -----------------------
model = joblib.load("diabetes_model.pkl")
data = pd.read_csv("diabetes_data.csv")

st.set_page_config(
    page_title="AI Diabetes Dashboard",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 AI Diabetes Risk Prediction System")

# -----------------------
# Tabs
# -----------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Prediction",
    "Data Insights",
    "Model Performance",
    "Explainability"
])

# ====================================================
# TAB 1 : PREDICTION
# ====================================================

with tab1:

    st.header("Patient Risk Prediction")

    col1, col2 = st.columns([1,1])

    with col1:

        pregnancies = st.number_input("Pregnancies",0,20,1)
        glucose = st.number_input("Glucose",0,300,120)
        bp = st.number_input("Blood Pressure",0,200,70)
        skin = st.number_input("Skin Thickness",0,100,20)
        insulin = st.number_input("Insulin",0,900,80)
        bmi = st.number_input("BMI",0.0,70.0,25.0)
        dpf = st.number_input("DPF",0.0,3.0,0.5)
        age = st.number_input("Age",1,120,30)

        predict = st.button("Predict Risk")

    with col2:

        if predict:

            input_data = np.array([[pregnancies,glucose,bp,skin,insulin,bmi,dpf,age]])

            probability = model.predict_proba(input_data)[0][1]

            st.metric(
                "Diabetes Probability",
                f"{probability*100:.2f}%"
            )

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=probability*100,
                title={'text':"Risk Level"},
                gauge={
                    'axis':{'range':[0,100]},
                    'steps':[
                        {'range':[0,30],'color':"green"},
                        {'range':[30,60],'color':"yellow"},
                        {'range':[60,100],'color':"red"}
                    ]
                }
            ))

            st.plotly_chart(fig)

# ====================================================
# TAB 2 : DATA INSIGHTS
# ====================================================

with tab2:

    st.header("Dataset Insights")

    st.write("Dataset Preview")
    st.dataframe(data.head())

    st.subheader("Feature Distribution")

    feature = st.selectbox(
        "Select Feature",
        data.columns[:-1]
    )

    st.bar_chart(data[feature])

# ====================================================
# TAB 3 : MODEL PERFORMANCE
# ====================================================

with tab3:

    st.header("Model Evaluation")

    X = data.drop("Outcome",axis=1)
    y = data["Outcome"]

    probs = model.predict_proba(X)[:,1]

    fpr,tpr,_ = roc_curve(y,probs)
    roc_auc = auc(fpr,tpr)

    fig, ax = plt.subplots()

    ax.plot(fpr,tpr,label=f"AUC = {roc_auc:.2f}")
    ax.plot([0,1],[0,1],'--')

    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("ROC Curve")

    ax.legend()

    st.pyplot(fig)

# ====================================================
# TAB 4 : EXPLAINABILITY (SHAP)
# ====================================================

with tab4:

    st.header("Model Explainability")

    X = data.drop("Outcome",axis=1)

    explainer = shap.Explainer(model, X)
    shap_values = explainer(X)

    fig = plt.figure()
    shap.summary_plot(shap_values, X, show=False)

    st.pyplot(fig)