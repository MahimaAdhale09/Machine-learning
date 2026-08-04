# 💧 Water Potability Prediction Using Support Vector Machine (SVM)

## 📌 Project Overview

Access to safe drinking water is one of the most important factors for maintaining public health. Water quality depends on several physical and chemical properties such as pH, hardness, dissolved solids, sulfate concentration, conductivity, chloramines, organic carbon, trihalomethanes, and turbidity.

This project develops a **Machine Learning Classification Model** using **Support Vector Machine (SVM)** to predict whether a water sample is **Potable (Safe for Drinking)** or **Not Potable (Unsafe for Drinking)** based on these water quality parameters.

The project also includes data preprocessing, missing value handling, feature scaling, class imbalance handling using **ADASYN**, hyperparameter tuning using **GridSearchCV**, and model evaluation.

---

# 🎯 Problem Statement

Determining water quality through laboratory testing is often time-consuming, expensive, and requires specialized equipment. Machine Learning provides an efficient alternative by predicting water potability using existing water quality measurements.

The objective of this project is to build an accurate machine learning model capable of classifying water samples into potable and non-potable categories using Support Vector Machine (SVM).

---

# 📂 Dataset Information

- **Dataset Name:** Water Potability Dataset
- **Total Rows:** 3276
- **Total Columns:** 10

### Independent Variables

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Target Variable

- Potability

### Target Classes

- **1 → Potable**
- **0 → Not Potable**

### Problem Type

**Binary Classification**

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn (ADASYN)
- Support Vector Machine (SVM)
- GridSearchCV
- Jupyter Notebook

---

# 📊 Data Preprocessing

The following preprocessing steps were performed before model training:

- Data Loading
- Exploratory Data Analysis (EDA)
- Missing Value Handling
- Feature Selection
- Feature Scaling using StandardScaler
- Train-Test Split
- Handling Imbalanced Dataset using ADASYN

---

# 🤖 Machine Learning Model

The classification model used in this project is:

**Support Vector Machine (SVM)**

Hyperparameter tuning was performed using **GridSearchCV** to obtain the best model parameters.

---

# 📈 Model Evaluation

The model performance was evaluated using:

- Accuracy Score
- Classification Report
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 🔄 Project Workflow

```text
                    Water Potability Dataset
                              │
                              ▼
                     Load Dataset using Pandas
                              │
                              ▼
                  Exploratory Data Analysis (EDA)
                              │
                              ▼
                  Handle Missing Values
                              │
                              ▼
                     Feature Selection
                              │
                              ▼
                     Train-Test Split
                              │
                              ▼
                  Feature Scaling (StandardScaler)
                              │
                              ▼
          Handle Class Imbalance using ADASYN
                              │
                              ▼
          Hyperparameter Tuning (GridSearchCV)
                              │
                              ▼
              Train Support Vector Machine (SVM)
                              │
                              ▼
                     Predict Test Data
                              │
                              ▼
                    Evaluate Model
                              │
                              ▼
                 Water Potability Prediction
```

---

# 📁 Project Structure

```
Water-Potability-Prediction/
│
├── water_potability.csv
├── SVC_water_potability.ipynb
├── README.md
└── requirements.txt
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Water-Potability-Prediction.git
```

Move to project directory

```bash
cd Water-Potability-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook

```bash
jupyter notebook
```

Open

```
SVC_water_potability.ipynb
```

---

# 📦 Required Libraries

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
jupyter
```

---

# 🚀 Future Improvements

- Deploy the model using Flask or FastAPI
- Build a Streamlit web application
- Deploy on Render or Railway
- Compare SVM with Random Forest, XGBoost, and LightGBM
- Improve prediction accuracy through advanced feature engineering

---

# 🎯 Key Features

- Binary Classification Problem
- Missing Value Handling
- Feature Scaling
- ADASYN Oversampling
- Hyperparameter Tuning
- Support Vector Machine (SVM)
- Classification Report
- Accuracy Evaluation
- Confusion Matrix
- End-to-End Machine Learning Pipeline

---

# 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Standardization
- Handling Imbalanced Data
- Support Vector Machine (SVM)
- GridSearchCV
- Model Evaluation
- Binary Classification

---

# 👩‍💻 Author

**Mahima Adhale**

B.Tech Computer Science & Engineering

Machine Learning | Data Analytics | Python | SQL | Power BI

---

# ⭐ If you found this project helpful, please give it a Star ⭐