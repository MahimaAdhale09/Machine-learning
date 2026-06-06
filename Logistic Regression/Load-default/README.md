# 🏦 Loan Default Risk Prediction Using Logistic Regression

## 📌 Project Overview
This project focuses on predicting whether a borrower is likely to default on a loan using a **Logistic Regression** classification model. The model analyzes demographic, financial, and credit-related information of loan applicants to classify them as either likely to default or not default.

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning classification model that predicts whether a borrower is likely to default on a loan based on various factors such as:

- Age
- Annual Income
- Credit Score
- Loan Amount
- Employment Years
- Number of Credit Lines
- Debt-to-Income Ratio
- Missed Payments (Last 2 Years)
- Savings Balance
- Loan Purpose

The model helps financial institutions assess loan risk and make informed lending decisions.

---

## 📊 Dataset Information

### Dataset Shape
- **Total Rows:** 1000
- **Total Columns:** 11

### Independent Variables (Features)

- Age
- Annual Income
- Credit Score
- Loan Amount
- Employment Years
- Number of Credit Lines
- Debt-to-Income Ratio
- Missed Payments Last 2 Years
- Savings Balance
- Loan Purpose

### Target Variable

- **Defaulted**
  - 0 → Loan Not Defaulted
  - 1 → Loan Defaulted

### Problem Type
- Classification

### Algorithm Used
- Logistic Regression

---

## 🏗️ Workflow Architecture

```text
Import Libraries
        ↓
Load Dataset (1000 × 11)
        ↓
Data Understanding
        ↓
Data Quality Checks
        ↓
Exploratory Data Analysis (EDA)
        ↓
Encoding
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Model Building
        ↓
Prediction
        ↓
Evaluation
        ↓
Training & Testing Score
        ↓
Business Conclusion
```

---

## 🧹 Data Preprocessing

### Data Quality Checks
- Checked dataset dimensions.
- Verified data types.
- Checked for missing values.
- Checked for duplicate records.

### Encoding
Since **Loan Purpose** is a categorical variable, encoding techniques were applied before model training.

### Feature Scaling
Numerical features were standardized using:

```python
StandardScaler()
```

to improve model performance.

---

## 📈 Exploratory Data Analysis (EDA)

### Univariate Analysis
- Distribution of numerical variables.
- Summary statistics using `describe()`.

### Bivariate Analysis
- Relationship between independent variables and loan default status.
- Correlation analysis among features.

### Visualization Techniques
- Histograms
- Boxplots
- Countplots
- Correlation Heatmaps

---

## 🎯 Feature Selection

### Independent Variables (X)

```python
X = df.drop('Defaulted', axis=1)
```

### Dependent Variable (Y)

```python
y = df['Defaulted']
```

---

## ✂️ Train-Test Split

The dataset was divided into training and testing datasets:

```python
train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)
```

- Training Data: 70%
- Testing Data: 30%

---

## 🤖 Model Building

### Logistic Regression

```python
lr = LogisticRegression()
lr.fit(x_train, y_train)
```

The model learns the relationship between applicant attributes and loan default risk.

---

## 🔮 Prediction

Predictions were generated on the test dataset:

```python
y_pred = lr.predict(x_test)
```

---

## 📏 Model Evaluation

The model performance was evaluated using:

### Confusion Matrix
- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

### Classification Report
- Precision
- Recall
- F1-Score
- Support

### Accuracy Score

| Metric | Score |
|----------|----------|
| Training Accuracy | 90.63% |
| Testing Accuracy | 91.00% |

---

## 📊 Classification Report Summary

### Class 0 (Non-Defaulted Loans)
- Precision: 94%
- Recall: 91%
- F1-Score: 92%

### Class 1 (Defaulted Loans)
- Precision: 88%
- Recall: 92%
- F1-Score: 90%

---

## 🔄 Cross Validation

To evaluate model stability, **K-Fold Cross Validation** was performed:

```python
KFold(n_splits=5)
cross_val_score(LogisticRegression(), X, y, cv=kf)
```

This helps ensure the model generalizes well across different subsets of data.

---

## 💡 Business Conclusion

- A Logistic Regression model was successfully developed to predict loan defaults.
- The model achieved:
  - **Training Accuracy:** 90.63%
  - **Testing Accuracy:** 91.00%
- The model demonstrates strong predictive performance and good generalization on unseen data.
- It effectively identifies both defaulted and non-defaulted borrowers.
- Financial institutions can use this model to:
  - Assess borrower risk.
  - Reduce potential loan losses.
  - Improve credit approval decisions.
  - Enhance portfolio risk management.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📚 Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    KFold,
    cross_val_score
)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import (
    StandardScaler,
    OrdinalEncoder,
    LabelEncoder
)

from sklearn.metrics import (
    confusion_matrix,
    classification_report
)
```

---

## 📂 Project Structure

```text
Loan Default Risk Prediction
│
├── Dataset
├── Data Understanding
├── Data Quality Checks
├── Exploratory Data Analysis
├── Encoding
├── Feature Scaling
├── Feature Selection
├── Train-Test Split
├── Logistic Regression Model
├── Prediction
├── Evaluation
├── Cross Validation
└── Business Conclusion
```

---

## 👩‍💻 Author

**Mahima Adhale**

Machine Learning & Data Analytics Project