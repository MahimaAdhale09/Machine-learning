# K-Nearest Neighbors (KNN) Classification

## Project Overview

K-Nearest Neighbors (KNN) is a supervised machine learning algorithm used for classification and regression tasks. It classifies a new data point based on the majority class of its K nearest neighbors. KNN is simple, effective, and widely used for pattern recognition and predictive modeling.

This project demonstrates the implementation of KNN Classification for predicting class labels based on feature similarity.

---

## Problem Statement

The objective of this project is to build a machine learning model using the K-Nearest Neighbors (KNN) algorithm to accurately classify observations into their respective categories based on the similarity of feature values. The model identifies the nearest neighbors of a new observation and assigns the class that is most common among those neighbors.

---

## Workflow Architecture

```text
Dataset Collection
        │
        ▼
Data Understanding
(Shape, Info, Describe)
        │
        ▼
Data Cleaning
(Missing Values, Duplicates)
        │
        ▼
Exploratory Data Analysis
(Univariate & Bivariate Analysis)
        │
        ▼
Encoding
(Label Encoding / One-Hot Encoding)
        │
        ▼
Feature & Target Separation
(X and y)
        │
        ▼
Feature Scaling
(StandardScaler)
        │
        ▼
Train-Test Split
        │
        ▼
Hyperparameter Tuning
(Finding Optimal K Value)
        │
        ▼
KNN Model Building
        │
        ▼
Prediction
        │
        ▼
Model Evaluation
(Accuracy, Precision, Recall, F1-Score)
        │
        ▼
Conclusion
```

---

## Data Structure

```text
Total Rows           : Depends on Dataset
Total Columns        : Depends on Dataset

Independent Variables: Feature Columns

Target Column        : Class Label

Problem Type         : Classification Problem

Model Used           : K-Nearest Neighbors (KNN)
```

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

---

## Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
```

---

## Data Preprocessing

### Handling Missing Values

```python
df.isnull().sum()
```

### Handling Duplicate Values

```python
df.drop_duplicates(inplace=True)
```

### Feature and Target Separation

```python
X = df.drop('target', axis=1)
y = df['target']
```

### Feature Scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

## Train-Test Split

```python
x_train, x_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42
)
```

---

## Hyperparameter Tuning

```python
train_acc = []
test_acc = []

for i in range(2,20):
    
    kn = KNeighborsClassifier(n_neighbors=i)
    
    kn.fit(x_train,y_train)
    
    train_acc.append(kn.score(x_train,y_train))
    
    test_acc.append(kn.score(x_test,y_test))
```

### Selecting Best K Value

```python
best_k = 5
```

---

## Model Building

```python
kn = KNeighborsClassifier(n_neighbors=5)

kn.fit(x_train,y_train)

y_pred = kn.predict(x_test)
```

---

## Model Evaluation

### Classification Report

```python
from sklearn.metrics import classification_report

print(classification_report(y_test,y_pred))
```

### Confusion Matrix

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)

print(cm)
```

### Accuracy Score

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,y_pred)

print(accuracy)
```

---

## Advantages of KNN

- Simple and easy to understand.
- No training phase required.
- Effective for small datasets.
- Works well for multi-class classification.
- Can capture complex decision boundaries.

---

## Disadvantages of KNN

- Computationally expensive for large datasets.
- Sensitive to irrelevant features.
- Requires feature scaling.
- Performance decreases with high-dimensional data.

---

## Applications of KNN

- Medical Diagnosis
- Disease Prediction
- Credit Risk Analysis
- Customer Segmentation
- Image Classification
- Recommendation Systems
- Fraud Detection

---

## Conclusion

K-Nearest Neighbors (KNN) is a simple yet powerful supervised machine learning algorithm used for classification problems. It classifies data points based on the majority vote of their nearest neighbors. Proper data preprocessing, feature scaling, and selection of the optimal K value significantly improve model performance. KNN is highly effective for pattern recognition tasks and serves as a strong baseline classification algorithm for many real-world applications.

---

## Author

Mahima Adhale

Machine Learning Project | KNN Classification