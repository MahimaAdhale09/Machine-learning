# 🌳 Decision Tree C5.0 Classification

## 📌 Project Overview

This project demonstrates the implementation of the C5.0 Decision Tree algorithm for classification tasks. C5.0 is an advanced version of the C4.5 algorithm developed by Ross Quinlan. It is designed to generate accurate and efficient decision trees by using information gain and gain ratio for selecting the best attributes during tree construction.

C5.0 is widely used in machine learning because it produces smaller trees, handles missing values efficiently, supports boosting, and provides higher classification accuracy compared to earlier decision tree algorithms.

---

## 🎯 Problem Statement

The objective of this project is to build a C5.0 Decision Tree model that can accurately classify observations into predefined categories based on input features. The model learns patterns from historical data and predicts the target class for new observations.

---

## 🗂️ Dataset Information

- Dataset Type: Classification Dataset
- Target Variable: Categorical
- Features: Numerical and/or Categorical
- Missing Values: Handled during preprocessing
- Objective: Predict the target class

---

## ⚙️ Workflow Architecture

```text
Data Collection
       │
       ▼
Data Loading
       │
       ▼
Exploratory Data Analysis (EDA)
       │
       ▼
Data Cleaning
       │
       ▼
Handling Missing Values
       │
       ▼
Encoding Categorical Features
       │
       ▼
Feature Selection
       │
       ▼
Train-Test Split
       │
       ▼
C5.0 Decision Tree Training
       │
       ▼
Prediction
       │
       ▼
Model Evaluation
       │
       ▼
Performance Analysis
```

---

## 📚 About C5.0 Algorithm

C5.0 is an improved version of the C4.5 algorithm.

Key features include:

- Faster training speed
- Lower memory usage
- Better classification accuracy
- Supports boosting
- Handles missing values
- Automatic feature selection
- Generates smaller and simpler trees

The algorithm selects the best feature using Gain Ratio.

---

## 🔍 Entropy

Entropy measures the impurity or randomness in the dataset.

Formula:

Entropy(S) = - Σ Pi log₂(Pi)

Where:

- Pi = Probability of class i

Lower entropy indicates a purer node.

---

## 🔍 Information Gain

Information Gain measures the reduction in entropy after splitting the dataset.

Formula:

Information Gain = Entropy(Parent) − Weighted Entropy(Children)

A feature with higher Information Gain is preferred for splitting.

---

## 🔍 Gain Ratio

C5.0 uses Gain Ratio instead of pure Information Gain to reduce bias toward attributes with many distinct values.

Formula:

Gain Ratio = Information Gain / Split Information

The attribute with the highest Gain Ratio is selected as the splitting feature.

---

## 🛠️ Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

---

## 📥 Data Loading

```python
df = pd.read_csv("dataset.csv")

df.head()
```

---

## 🔎 Exploratory Data Analysis

```python
df.info()

df.describe()

df.isnull().sum()
```

---

## 🧹 Data Preprocessing

### Handling Missing Values

```python
df.fillna(df.mean(), inplace=True)
```

### Encoding Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['column_name'] = le.fit_transform(df['column_name'])
```

---

## ✂️ Train-Test Split

```python
X = df.drop('target', axis=1)

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

## 🚀 Model Training

```python
# Example representation of C5.0 logic

model.fit(X_train, y_train)
```

---

## 🔮 Prediction

```python
y_pred = model.predict(X_test)
```

---

## 📊 Model Evaluation

### Accuracy Score

```python
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

### Classification Report

```python
print(classification_report(y_test, y_pred))
```

### Confusion Matrix

```python
cm = confusion_matrix(y_test, y_pred)

print(cm)
```

---

## 📈 Performance Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🎯 Advantages of C5.0

- Higher accuracy than ID3 and C4.5
- Generates smaller trees
- Faster execution
- Handles missing values efficiently
- Supports boosting
- Better memory optimization
- Performs automatic feature selection
- Handles both numerical and categorical data

---

## ❌ Disadvantages of C5.0

- More computationally intensive than simple trees
- Can overfit on noisy datasets
- Less commonly available in Python libraries
- Complex tree structures may reduce interpretability

---

## 📌 Applications

- Medical Diagnosis
- Credit Risk Assessment
- Customer Churn Prediction
- Fraud Detection
- Disease Prediction
- Marketing Analytics
- Loan Approval Systems
- Customer Segmentation

---

## 📊 Results

The C5.0 Decision Tree model successfully learned classification rules from the training data and accurately predicted the target classes on unseen observations.

Performance was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🎯 Conclusion

C5.0 is one of the most advanced decision tree algorithms and offers significant improvements over ID3 and C4.5. By utilizing Gain Ratio, boosting capabilities, and efficient tree pruning techniques, C5.0 produces accurate, compact, and interpretable classification models. It is particularly useful for datasets containing categorical and numerical attributes and is widely applied in real-world classification problems.

---

## 👨‍💻 Author

**Mahima Adhale**

Machine Learning Enthusiast | Data Analyst | Python Developer

---

⭐ If you found this project useful, don't forget to star the repository!