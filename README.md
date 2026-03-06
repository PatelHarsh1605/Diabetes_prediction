# 🩺 AI Diabetes Risk Prediction Dashboard

An interactive **Machine Learning powered medical dashboard** built with **Streamlit** that predicts the probability of diabetes based on patient health parameters.

This system allows users to input medical information and instantly receive a **risk prediction, visual insights, and model explainability**.

⚠️ This project is for **educational and research purposes only** and should not be used as a substitute for professional medical diagnosis.

---

# 🚀 Features

### 🔍 Patient Risk Prediction

* Enter patient medical parameters
* Predict probability of diabetes
* Risk classification (Low / Moderate / High)

### 📊 Interactive Dashboard

* Real-time prediction visualization
* Risk gauge chart
* Medical feature summary

### 📈 Data Insights

* Explore dataset distributions
* Visualize health indicators
* Identify patterns in medical data

### 🧠 Model Performance

* ROC Curve
* AUC Score
* Model evaluation metrics

### 🔬 Explainable AI

* SHAP feature importance
* Understand which factors influence prediction

---

# 🛠 Tech Stack

| Tool         | Purpose                    |
| ------------ | -------------------------- |
| Python       | Core programming           |
| Streamlit    | Web app interface          |
| Scikit-learn | Machine learning model     |
| Pandas       | Data processing            |
| NumPy        | Numerical operations       |
| Plotly       | Interactive visualizations |
| Matplotlib   | Graph plotting             |
| SHAP         | Model explainability       |

---

# 📂 Project Structure

```
diabetes-dashboard/
│
├── app.py                 # Streamlit application
├── diabetes_model.pkl     # Trained ML model
├── diabetes_data.csv      # Dataset used for analysis
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-dashboard.git
cd diabetes-dashboard
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Then open the browser:

```
http://localhost:8501
```

---

# 📊 Input Features Used

The model predicts diabetes risk using the following medical parameters:

* Pregnancies
* Glucose Level
* Blood Pressure
* Skin Thickness
* Insulin
* Body Mass Index (BMI)
* Diabetes Pedigree Function
* Age

---

# 📉 Model

The machine learning model was trained using **Scikit-learn classification algorithms** to predict diabetes probability based on patient health indicators.

Model output includes:

* Binary prediction (Diabetic / Non-Diabetic)
* Probability score
* Risk categorization

---

# ⚠️ Disclaimer

This tool is intended for **educational and research purposes only**.
It is not a medical diagnostic system.

Always consult a **qualified healthcare professional** for medical advice and diagnosis.

---

# 📌 Future Improvements

* Patient PDF health reports
* Real-time data integration
* Model retraining pipeline
* Advanced medical dashboards
* Cloud deployment

---

# 👨‍💻 Author

**Harsh Patel**

* IT Student
* Interested in **AI / Machine Learning**
* Passionate about building real-world ML applications

---

# ⭐ Support

If you find this project useful, consider giving it a **star ⭐ on GitHub**.
