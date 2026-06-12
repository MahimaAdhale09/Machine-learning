# 🌳 Decision Tree (CART) Classification Project

## 📌 Project Overview

This project demonstrates the implementation of the CART (Classification and Regression Tree) algorithm using Decision Tree Classification. CART is a supervised machine learning algorithm used for both classification and regression tasks. In classification problems, CART uses Gini Impurity as the splitting criterion to create an optimal decision tree.

The model learns decision rules from the training dataset and predicts the target class for unseen observations.

---

# 🎯 Problem Statement

The objective of this project is to build a CART Decision Tree Classification model capable of accurately classifying observations into predefined categories based on their input features.

The model recursively partitions the dataset into smaller subsets until pure leaf nodes are formed or stopping criteria are met.

---

# 🗂️ Dataset Information

- Dataset Type: Classification Dataset
- Features: Numerical and/or Categorical Variables
- Target Variable: Categorical
- Missing Values: Handled during preprocessing
- Objective: Predict the target class

---

# ⚙️ Workflow Architecture

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
Feature Selection
       │
       ▼
Train-Test Split
       │
       ▼
CART Decision Tree Training
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

# 📚 What is CART?

CART stands for:

**C**lassification  
**A**nd  
**R**egression  
**T**ree

It is a tree-based supervised learning algorithm that creates binary splits at every node.

### For Classification

- Uses Gini Impurity
- Produces categorical outputs

### For Regression

- Uses Residual Sum of Squares (RSS)
- Produces continuous outputs

---

# 🌳 Structure of Decision Tree

```text
                 Root Node
                      │
          ┌───────────┴───────────┐
          │                       │
      Decision Node         Decision Node
          │                       │
      ┌───┴───┐               ┌───┴───┐
      │       │               │       │
   Leaf     Leaf           Leaf     Leaf
   Node     Node           Node     Node
```

---

# 🔍 Gini Impurity

CART Classification uses Gini Impurity to determine the best split.

### Formula

Gini = 1 − Σ(pi)²

Where:

- pi = Probability of class i

### Interpretation

| Gini Value | Meaning |
|------------|----------|
| 0 | Pure Node |
| Close to 1 | Impure Node |

Lower Gini Impurity indicates a better split.

---

# 🛠️ Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
```

---

# 📥 Data Loading

```python
df = pd.read_csv("dataset.csv")

df.head()
```

---

# 🔎 Exploratory Data Analysis

```python
df.info()

df.describe()

df.isnull().sum()
```

---

# 🧹 Data Preprocessing

## Handling Missing Values

```python
df.fillna(df.mean(), inplace=True)
```

## Encoding Categorical Variables

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['column_name'] = le.fit_transform(df['column_name'])
```

---

# ✂️ Train-Test Split

```python
X = df.drop('target', axis=1)

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
```

---

# 🚀 CART Model Training

```python
cart = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5,
    random_state=42
)

cart.fit(X_train, y_train)
```

---

# 🔮 Prediction

```python
y_pred = cart.predict(X_test)
```

---

# 📊 Model Evaluation

## Training Accuracy

```python
print("Training Accuracy:",
      cart.score(X_train, y_train))
```

## Testing Accuracy

```python
print("Testing Accuracy:",
      cart.score(X_test, y_test))
```

## Accuracy Score

```python
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
```

---

## Classification Report

```python
print(classification_report(y_test, y_pred))
```

### Metrics Included

- Precision
- Recall
- F1-Score
- Support

---

## Confusion Matrix

```python
cm = confusion_matrix(y_test, y_pred)

print(cm)
```

---

# 🌳 Visualizing CART Tree

```python
from sklearn import tree

plt.figure(figsize=(20,10))

tree.plot_tree(
    cart,
    filled=True,
    feature_names=X.columns,
    class_names=True
)

plt.show()
```

---

# 📈 Hyperparameters

| Parameter | Description |
|------------|-------------|
| criterion | gini |
| max_depth | Maximum depth of tree |
| min_samples_split | Minimum samples required for split |
| min_samples_leaf | Minimum samples required at leaf node |
| max_features | Number of features considered for split |
| random_state | Reproducibility |

---

# 📊 Evaluation Metrics

### Accuracy

Measures overall correctness.

### Precision

Measures positive prediction accuracy.

### Recall

Measures ability to identify positive cases.

### F1-Score

Harmonic mean of Precision and Recall.

### Confusion Matrix

Displays actual vs predicted classes.

---

# ✅ Advantages of CART

- Easy to understand and interpret
- Handles both numerical and categorical features
- No feature scaling required
- Can model nonlinear relationships
- Fast prediction
- Feature importance can be extracted

---

# ❌ Disadvantages of CART

- Prone to overfitting
- Sensitive to noisy data
- Can become complex for large datasets
- Small data changes may create different trees

---

# 💼 Real-World Applications

- Disease Prediction
- Customer Segmentation
- Fraud Detection
- Loan Approval
- Credit Risk Analysis
- Employee Attrition Prediction
- Marketing Campaign Analysis
- Customer Churn Prediction

---

# 📈 Results

The CART Decision Tree model was successfully trained on the dataset. The model learned decision rules using Gini Impurity and classified unseen observations with good predictive performance.

Performance was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 🎯 Conclusion

CART (Classification and Regression Tree) is one of the most powerful and interpretable machine learning algorithms. For classification tasks, it uses Gini Impurity to create optimal binary splits and build a decision tree structure. CART provides easy visualization, strong predictive capability, and straightforward interpretation, making it a popular choice for classification problems.

---

# 👨‍💻 Author

**Mahima Adhale**

Machine Learning Enthusiast | Data Analyst | Python Developer

---

⭐ If you found this project useful, don't forget to star the repository.