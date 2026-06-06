# Logistic Regression

## Project Overview
This project demonstrates the implementation of **Logistic Regression**, a supervised machine learning classification algorithm used to predict categorical outcomes. Logistic Regression estimates the probability of an observation belonging to a particular class and is widely used for binary classification problems.

---

## Problem Statement
The objective of this project is to build a Logistic Regression model that can classify observations into predefined categories based on input features. The model analyzes the relationship between independent variables and the target variable and predicts the probability of class membership.

---

## Dataset Information

### Dataset Shape
- Total Rows: *[Enter Number of Rows]*
- Total Columns: *[Enter Number of Columns]*

### Features

#### Independent Variables (X)
- Feature 1
- Feature 2
- Feature 3
- ...
- Feature n

#### Dependent Variable (Y)
- Target Variable (Binary/Categorical)

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Imported the required libraries.
2. Loaded the dataset.
3. Checked for missing values.
4. Removed duplicate records (if any).
5. Performed Exploratory Data Analysis (EDA).
6. Encoded categorical variables.
7. Handled outliers (if required).
8. Scaled numerical features.
9. Split the dataset into training and testing sets.

---

## Exploratory Data Analysis (EDA)

### Univariate Analysis
- Examined the distribution of individual features.
- Used histograms, count plots, and box plots.

### Bivariate Analysis
- Analyzed relationships between features and the target variable.
- Used bar charts, scatter plots, and correlation analysis.

### Correlation Analysis
- Generated a correlation heatmap to understand feature relationships.
- Identified important predictors affecting the target variable.

---

## Model Building

### Algorithm Used
**Logistic Regression**

### Steps
1. Split the data into training and testing sets.
2. Applied feature scaling where necessary.
3. Trained the Logistic Regression model.
4. Predicted class labels and probabilities.
5. Evaluated model performance using classification metrics.

---

## Logistic Regression Formula

The Logistic Regression model uses the Sigmoid Function:

\[
P(Y=1) = \frac{1}{1 + e^{-(b_0 + b_1X_1 + b_2X_2 + ... + b_nX_n)}}
\]

Where:

- \(P(Y=1)\) = Probability of the positive class
- \(b_0\) = Intercept
- \(b_1, b_2, ..., b_n\) = Coefficients
- \(X_1, X_2, ..., X_n\) = Independent Variables

---

## Model Evaluation Metrics

The model was evaluated using:

### Accuracy
Measures the proportion of correctly classified observations.

### Precision
Measures how many predicted positive cases are actually positive.

### Recall
Measures how many actual positive cases are correctly identified.

### F1-Score
Harmonic mean of Precision and Recall.

### Confusion Matrix
Provides a summary of prediction results.

---

## Results

| Metric | Value |
|---------|---------|
| Accuracy | *Enter Value* |
| Precision | *Enter Value* |
| Recall | *Enter Value* |
| F1-Score | *Enter Value* |

---

## Confusion Matrix

```text
                 Predicted
               0         1
Actual 0      TN        FP
Actual 1      FN        TP
```

Where:
- TN = True Negative
- TP = True Positive
- FN = False Negative
- FP = False Positive

---

## Conclusion

- Logistic Regression was successfully implemented for classification.
- The model learned the relationship between independent variables and the target variable.
- Performance was evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.
- Logistic Regression provides probability-based predictions, making it interpretable and effective for binary classification tasks.
- Further improvements can be achieved through feature engineering, hyperparameter tuning, and handling class imbalance.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Libraries Required

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
```

---

## Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Prediction
10. Conclusion

---

## Author

**Mahima Adhale**

Machine Learning & Data Analytics Project