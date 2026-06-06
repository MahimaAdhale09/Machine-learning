# 💧 Water Potability Classification Using Logistic Regression

## 📌 Project Overview
This project focuses on predicting whether water is safe for drinking (potable) using various water quality parameters. A **Logistic Regression** classification model is developed to analyze physicochemical properties of water and classify samples as potable or non-potable.

---

## 🎯 Problem Statement
The objective of this project is to develop a machine learning classification model that predicts the potability of water using water quality attributes such as:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

The model helps determine whether a water sample is safe for drinking.

---

## 📊 Dataset Information

### Dataset Shape
- **Total Rows:** 3276
- **Total Columns:** 10

### Independent Variables (Features)
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
- **Potability**
  - 0 → Non-Potable Water
  - 1 → Potable Water

### Problem Type
- Classification

### Algorithm Used
- Logistic Regression

---

## 🏗️ Workflow Architecture

```text
Import Libraries
        ↓
Load Dataset
        ↓
Data Understanding
        ↓
Data Quality Checks
        ↓
Handling Missing Values
        ↓
Exploratory Data Analysis (EDA)
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
Business Conclusion
```

---

## 🧹 Data Preprocessing

### Data Quality Checks
- Checked for duplicate records.
- Checked for missing values.

### Missing Value Handling
Missing values were found in:

- pH
- Sulfate
- Trihalomethanes

These missing values were replaced using the **Mean Imputation** technique with `SimpleImputer`.

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

### Univariate Analysis
- Statistical summary using `describe()`
- Data type inspection
- Missing value analysis

### Visualization
- Boxplots for outlier detection
- Pairplots to understand relationships among variables

### Observations
- All variables are numerical.
- No categorical encoding was required.
- Logistic Regression was applied directly after preprocessing.

---

## 🎯 Feature Selection

### Independent Variables (X)

```python
X = df.iloc[:,:-1]
```

### Dependent Variable (Y)

```python
y = df['Potability']
```

---

## ✂️ Train-Test Split

The dataset was split into training and testing sets:

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

The model learns the relationship between water quality attributes and water potability.

---

## 🔮 Prediction

Predictions were generated on the testing dataset:

```python
y_pred = lr.predict(x_test)
```

---

## 📏 Model Evaluation

The model was evaluated using:

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

| Metric | Value |
|----------|----------|
| Training Accuracy | 60.23% |
| Testing Accuracy | 62.77% |

---

## 📉 Results Interpretation

- The model correctly classified most non-potable water samples.
- The model struggled to identify potable water samples.
- Class imbalance affected overall model performance.
- The classifier became biased toward the majority class.

---

## 💡 Business Conclusion

- A Logistic Regression model was successfully developed for water potability prediction.
- The model achieved:
  - **Training Accuracy:** 60.23%
  - **Testing Accuracy:** 62.77%
- The model performs reasonably well for identifying non-potable water.
- However, it fails to accurately identify potable water samples.
- The current model is biased toward the majority class and is not suitable for reliable real-world water quality prediction.
- Future improvements may include:
  - Handling class imbalance using SMOTE or resampling techniques.
  - Feature engineering.
  - Hyperparameter tuning.
  - Trying advanced classification algorithms such as Random Forest, XGBoost, or Gradient Boosting.

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

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)
```

---

## 📂 Project Structure

```text
Water Potability Classification
│
├── Dataset
├── Data Cleaning
├── Missing Value Treatment
├── Exploratory Data Analysis
├── Feature Selection
├── Train-Test Split
├── Logistic Regression Model
├── Prediction
├── Evaluation
└── Conclusion
```

---

## 👩‍💻 Author

**Mahima Adhale**

Machine Learning & Data Analytics Project