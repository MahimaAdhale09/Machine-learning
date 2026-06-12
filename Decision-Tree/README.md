# 🌳 Decision Tree Classification

## 📌 Project Overview

This project demonstrates the implementation of the Decision Tree Classification algorithm for predicting target classes based on input features. Decision Trees are supervised machine learning algorithms that create a tree-like model of decisions and their possible consequences. They are widely used due to their simplicity, interpretability, and effectiveness in solving classification problems.

---

## 🎯 Problem Statement

The objective of this project is to build a Decision Tree Classification model capable of accurately classifying observations into predefined categories using historical data. The model learns patterns from the training dataset and predicts outcomes for unseen data.

---

## 🗂️ Dataset Information

- Dataset Type: Classification Dataset
- Target Variable: Categorical
- Features: Numerical and/or Categorical
- Missing Values: Handled during preprocessing
- Data Cleaning: Performed before model training
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
Encoding Categorical Variables
       │
       ▼
Feature Scaling (Optional)
       │
       ▼
Train-Test Split
       │
       ▼
Decision Tree Model Training
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

## 📚 About Decision Tree

A Decision Tree is a supervised learning algorithm used for classification and regression tasks.

It consists of:

- Root Node
- Decision Nodes
- Branches
- Leaf Nodes

The model recursively splits the dataset into smaller subsets based on feature values until a stopping criterion is met.

---

## 🔍 Splitting Criteria

### Gini Impurity

Gini Impurity measures the probability of incorrectly classifying a randomly chosen element.

Formula:

Gini = 1 - Σ(pi²)

Where:

- pi = Probability of class i

A lower Gini value indicates a better split.

---

### Entropy

Entropy measures the randomness or impurity within a node.

Formula:

Entropy = -Σ(pi log₂ pi)

Where:

- pi = Probability of class i

A lower entropy value indicates a purer node.

---

## 🛠️ Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

### Encoding Categorical Features

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
model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5,
    random_state=42
)

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

## 📈 Visualization of Decision Tree

```python
from sklearn import tree
import matplotlib.pyplot as plt

plt.figure(figsize=(15,10))

tree.plot_tree(
    model,
    filled=True,
    feature_names=X.columns,
    class_names=True
)

plt.show()
```

---

## 📊 Performance Metrics

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🎯 Hyperparameters

| Parameter | Description |
|------------|------------|
| criterion | Splitting criterion (gini/entropy) |
| max_depth | Maximum depth of tree |
| min_samples_split | Minimum samples required to split a node |
| min_samples_leaf | Minimum samples required at leaf node |
| random_state | Ensures reproducibility |

---

## ✅ Advantages of Decision Tree

- Easy to understand and interpret
- Requires minimal data preprocessing
- Handles both numerical and categorical data
- Works well for nonlinear relationships
- Feature importance can be extracted
- Fast training and prediction

---

## ❌ Disadvantages of Decision Tree

- Prone to overfitting
- Sensitive to noisy data
- Can become complex with large datasets
- Small changes in data can produce different trees

---

## 📌 Applications

- Medical Diagnosis
- Customer Segmentation
- Fraud Detection
- Credit Risk Analysis
- Loan Approval Systems
- Disease Prediction
- Marketing Analytics

---

## 📈 Results

The Decision Tree model was trained and evaluated on the dataset. The model successfully learned decision rules from the training data and predicted the target classes for unseen observations.

Performance was measured using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 🎯 Conclusion

Decision Tree Classification is one of the most popular and interpretable machine learning algorithms. It provides clear decision-making paths and works effectively on classification problems. By tuning hyperparameters such as maximum depth and minimum samples per split, the model can achieve better generalization and reduce overfitting.

---

## 👨‍💻 Author

**Mahima Adhale**


Machine Learning Enthusiast | Data Analyst | Python Developer

---

⭐ If you found this project useful, please give it a star!