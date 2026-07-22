# 🌳 Random Forest Algorithm

## 📌 Introduction

Random Forest is a supervised machine learning algorithm used for both **classification** and **regression** tasks. It belongs to the ensemble learning family, where multiple Decision Trees are combined to produce more accurate and stable predictions.

Instead of relying on a single Decision Tree, Random Forest creates many decision trees during training and combines their outputs. This approach reduces overfitting, improves accuracy, and provides better generalization on unseen data.

---

# 📖 What is Random Forest?

Random Forest is an ensemble learning technique based on **Bagging (Bootstrap Aggregating)**.

It works by:

- Creating multiple random subsets of the training dataset.
- Building one Decision Tree for each subset.
- Selecting a random subset of features at every split.
- Combining predictions from all trees.

For Classification:
- Final prediction = Majority Voting

For Regression:
- Final prediction = Average of all tree predictions

---

# 🎯 Objectives

The main objectives of Random Forest are:

- Improve prediction accuracy.
- Reduce overfitting.
- Handle large datasets efficiently.
- Select important features.
- Build a robust predictive model.

---

# ⚙️ How Random Forest Works

### Step 1: Bootstrap Sampling

Random Forest randomly selects multiple samples from the original dataset with replacement.

Example

Dataset

```
1000 Rows
```

Tree 1

```
Random 1000 Samples
```

Tree 2

```
Random 1000 Samples
```

Tree 3

```
Random 1000 Samples
```

Each tree receives a different dataset.

---

### Step 2: Random Feature Selection

Instead of considering every feature at each split, Random Forest selects a random subset of features.

Example

Suppose there are

```
10 Features
```

Each tree may randomly consider only

```
3 Features
```

at every split.

This increases diversity among trees.

---

### Step 3: Build Multiple Decision Trees

Each sampled dataset is used to build a Decision Tree independently.

Example

```
Dataset

↓

Tree 1

↓

Tree 2

↓

Tree 3

↓

Tree 4

↓

Tree 5

↓

...

↓

Tree N
```

---

### Step 4: Final Prediction

For Classification

Every tree votes.

Example

```
Tree1 → Yes

Tree2 → Yes

Tree3 → No

Tree4 → Yes

Tree5 → Yes
```

Final Prediction

```
Yes
```

For Regression

Average prediction is calculated.

Example

```
Tree1 → 72

Tree2 → 75

Tree3 → 70

Tree4 → 74

Tree5 → 73
```

Final Prediction

```
(72+75+70+74+73)/5 = 72.8
```

---

# 📊 Types of Random Forest

## 1. Random Forest Classifier

Used when the target variable is categorical.

Examples

- Disease Prediction
- Spam Detection
- Customer Churn Prediction
- Loan Approval
- Fraud Detection

---

## 2. Random Forest Regressor

Used when the target variable is numerical.

Examples

- House Price Prediction
- Wine Quality Prediction
- Sales Prediction
- Salary Prediction
- Temperature Forecasting

---

# 📚 Advantages

- High prediction accuracy
- Reduces overfitting
- Works with both classification and regression
- Handles missing values effectively
- Performs well on large datasets
- Handles nonlinear relationships
- Provides feature importance
- Robust to noise and outliers
- Supports parallel processing

---

# ⚠️ Disadvantages

- Slower training compared to a single Decision Tree
- Uses more memory
- Less interpretable than a Decision Tree
- Large models may take longer to predict

---

# 📈 Hyperparameters

Common hyperparameters include:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf
- max_features
- bootstrap
- random_state

Example

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
```

---

# 📊 Evaluation Metrics

## Classification

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

## Regression

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

# 🛠 Python Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

---

# 🚀 Applications

Random Forest is widely used in many industries:

Healthcare
- Disease Prediction
- Heart Disease Detection
- Diabetes Prediction

Finance
- Credit Risk Analysis
- Loan Approval
- Fraud Detection

Marketing
- Customer Segmentation
- Customer Churn Prediction
- Sales Forecasting

Manufacturing
- Quality Control
- Demand Forecasting

Agriculture
- Crop Yield Prediction
- Soil Quality Prediction

Real Estate
- House Price Prediction

Food Industry
- Wine Quality Prediction

---

# 📌 Why Use Random Forest?

Random Forest is one of the most popular machine learning algorithms because it:

- Produces high accuracy.
- Handles large datasets efficiently.
- Reduces overfitting compared to Decision Trees.
- Identifies important features.
- Works well with numerical and categorical data.
- Requires minimal preprocessing.

---

# 🏁 Conclusion

Random Forest is a powerful ensemble learning algorithm that combines multiple Decision Trees to improve prediction accuracy and model stability. It is suitable for both classification and regression tasks and performs well on complex, real-world datasets. Due to its robustness, ability to reduce overfitting, and feature importance capability, Random Forest is widely used across healthcare, finance, marketing, manufacturing, and many other domains. It remains one of the most reliable and widely adopted machine learning algorithms for predictive analytics.

---

# 👩‍💻 Author

**Mahima Adhale**

Data Analytics | Machine Learning | Python | SQL | Power BI
