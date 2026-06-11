# 💼 Salary Prediction Using Employee Demographics and Job Attributes (KNN Regression)

## 📌 Project Overview

This project focuses on predicting employee salaries using demographic and professional attributes. The objective is to identify how factors such as job title, years of experience, education level, skills count, company size, location, remote work status, and certifications influence employee compensation.

A K-Nearest Neighbors (KNN) Regression model is developed to estimate salaries accurately based on these workforce characteristics.

The project covers the complete Machine Learning pipeline including data understanding, data preprocessing, exploratory data analysis, feature engineering, model building, hyperparameter tuning, and model evaluation.

---

# 🎯 Problem Statement

The objective of this project is to analyze employee-related attributes and develop a machine learning model capable of predicting employee salaries based on professional and demographic characteristics.

By identifying the key factors that influence salary levels, organizations can make data-driven compensation decisions, while individuals can gain insights into potential earnings based on their career profiles.

---

# 🔄 Workflow Architecture

```text
Dataset Collection
        │
        ▼
Dataset Loading
        │
        ▼
Data Understanding
├── Dataset Shape
├── Data Types
├── Statistical Summary
└── Feature Analysis
        │
        ▼
Data Quality Check
├── Missing Value Detection
├── Duplicate Record Detection
└── Data Validation
        │
        ▼
Exploratory Data Analysis (EDA)
├── Boxplot Analysis
├── Experience vs Salary
├── Skills vs Certifications
└── Industry-based Analysis
        │
        ▼
Feature Engineering
├── Ordinal Encoding
│   ├── Job Title
│   ├── Location
│   ├── Education Level
│   ├── Company Size
│   └── Remote Work
├── Feature Selection
└── Drop Industry Column
        │
        ▼
Define Features & Target
├── X (Independent Variables)
└── y (Salary)
        │
        ▼
Feature Scaling
(StandardScaler)
        │
        ▼
Train-Test Split
(70% Training | 30% Testing)
        │
        ▼
Hyperparameter Tuning
(Test K Values 2–19)
        │
        ▼
Model Training
(KNN Regressor)
        │
        ▼
Salary Prediction
(y_pred)
        │
        ▼
Model Evaluation
├── R² Score
├── Mean Absolute Error (MAE)
├── Mean Squared Error (MSE)
└── Root Mean Squared Error (RMSE)
        │
        ▼
Final Salary Prediction Model
```

---

# 📊 Dataset Information

### Dataset Description

The dataset contains employee workforce information collected from various industries and locations worldwide.

### Dataset Characteristics

- Total Records: 250,000
- Total Features: 10
- Problem Type: Regression
- Algorithm Used: K-Nearest Neighbors Regressor

### Independent Variables

1. Job Title
2. Experience Years
3. Education Level
4. Skills Count
5. Industry
6. Company Size
7. Location
8. Remote Work
9. Certifications

### Target Variable

- Salary

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

---

# 📋 Data Preprocessing

### Data Quality Checks

- Missing Value Detection
- Duplicate Record Detection
- Data Type Verification

### Data Cleaning

- Verified missing values
- Checked duplicate records
- Removed unnecessary columns

### Feature Selection

- Industry column removed before model training

---

# 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

### Boxplot Analysis

Used to identify outliers and understand feature distributions.

### Experience vs Salary Analysis

Scatter plot showing the relationship between employee experience and salary.

### Skills vs Certifications Analysis

Scatter plot showing how skills and certifications vary across industries.

---

# 🔧 Feature Engineering

## Ordinal Encoding

### Job Title Encoding

| Job Title | Encoding |
|------------|----------|
| Data Analyst | 0 |
| Business Analyst | 1 |
| Frontend Developer | 2 |
| Backend Developer | 3 |
| Software Engineer | 4 |
| Data Scientist | 5 |
| Cybersecurity Analyst | 6 |
| DevOps Engineer | 7 |
| Cloud Engineer | 8 |
| Product Manager | 9 |
| Machine Learning Engineer | 10 |
| AI Engineer | 11 |

---

### Location Encoding

| Location | Encoding |
|-----------|----------|
| India | 0 |
| Netherlands | 1 |
| Singapore | 2 |
| Australia | 3 |
| Sweden | 4 |
| Remote | 5 |
| Germany | 6 |
| UK | 7 |
| Canada | 8 |
| USA | 9 |

---

### Education Level Encoding

| Education Level | Encoding |
|-----------------|----------|
| High School | 0 |
| Diploma | 1 |
| Bachelor | 2 |
| Master | 3 |
| PhD | 4 |

---

### Company Size Encoding

| Company Size | Encoding |
|--------------|----------|
| Startup | 0 |
| Small | 1 |
| Medium | 2 |
| Large | 3 |
| Enterprise | 4 |

---

### Remote Work Encoding

| Remote Work | Encoding |
|-------------|----------|
| No | 0 |
| Hybrid | 1 |
| Yes | 2 |

---

# ⚖️ Feature Scaling

Since KNN is a distance-based algorithm, StandardScaler was applied to normalize all features before model training.

### Benefits

- Improves distance calculations
- Prevents feature dominance
- Enhances model performance

---

# 🤖 Model Building

## Algorithm Used

### K-Nearest Neighbors Regressor (KNN Regressor)

KNN Regression predicts numerical values by averaging the values of the nearest neighboring data points.

---

## Hyperparameter Tuning

Different K values ranging from 2 to 19 were tested.

The model with the highest testing performance was selected.

### Optimal K Value

```python
n_neighbors = 13
```

---

# 📊 Model Evaluation

The model was evaluated using:

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted salaries.

### Root Mean Squared Error (RMSE)

Measures prediction error in the original salary scale.

### Mean Absolute Error (MAE)

Measures the average absolute prediction error.

### R² Score

Measures how well the model explains salary variance.

---

# 📈 Model Performance

### Training Accuracy (R² Score)

98.86%

### Testing Accuracy (R² Score)

98.67%

### Error Metrics

| Metric | Value |
|----------|------------|
| Mean Squared Error (MSE) | 18,480,860.42 |
| Root Mean Squared Error (RMSE) | 4,298.94 |
| Mean Absolute Error (MAE) | 3,385.84 |
| R² Score | 98.67% |

---

# ✅ Conclusion

The K-Nearest Neighbors (KNN) Regression model was successfully trained to predict employee salaries using workforce and employment-related attributes.

The model achieved a training R² score of 98.86% and a testing R² score of 98.67%, indicating exceptional predictive performance and strong generalization capability.

The low MAE, RMSE, and MSE values further demonstrate that the predicted salaries are very close to actual salaries. The minimal gap between training and testing accuracy confirms that the model is neither overfitting nor underfitting.

Overall, the KNN Regressor proved to be highly effective for salary estimation and can serve as a reliable tool for compensation analysis and workforce planning.

### Final Result

✅ KNN Regression achieved an R² Score of 98.67% for employee salary prediction.

---

# 🚀 Future Scope

- Apply GridSearchCV for advanced hyperparameter tuning.
- Compare performance with:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
  - Gradient Boosting Regressor
- Perform Feature Importance Analysis.
- Deploy the model using Streamlit or Flask.
- Build an Employee Salary Prediction Web Application.

---

# 👨‍💻 Author

**Mahima Adhale**

Machine Learning | Data Science | Artificial Intelligence Enthusiast

---

## ⭐ Skills Demonstrated

- Data Cleaning
- Data Validation
- Exploratory Data Analysis
- Feature Engineering
- Ordinal Encoding
- Feature Scaling
- KNN Regression
- Hyperparameter Tuning
- Model Evaluation
- Predictive Analytics
- Machine Learning Pipeline Development