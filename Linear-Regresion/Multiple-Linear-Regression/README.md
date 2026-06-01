# Multiple Linear Regression

## Overview
Multiple Linear Regression is a statistical and machine learning technique used to model the relationship between one dependent variable (Y) and two or more independent variables (X1, X2, ..., Xn). It helps predict the value of the dependent variable based on multiple input features.

### Regression Equation

Y = b0 + b1X1 + b2X2 + ... + bnXn

Where:
- Y = Dependent variable (target)
- X1, X2, ..., Xn = Independent variables (features)
- b0 = Intercept
- b1, b2, ..., bn = Regression coefficients

---

## Objective
The main objectives of Multiple Linear Regression are:
- To understand the relationship between multiple independent variables and a dependent variable.
- To predict continuous outcomes.
- To determine the impact of each feature on the target variable.

---

## How It Works
1. Collect data containing multiple input features and a target variable.
2. Analyze relationships between variables.
3. Fit the regression model using the least squares method.
4. Estimate coefficients for each independent variable.
5. Use the model to make predictions.

---

## Assumptions
Multiple Linear Regression assumes:
1. Linear relationship between predictors and target variable.
2. Independence of observations.
3. Homoscedasticity (constant variance of errors).
4. Normal distribution of residuals.
5. No multicollinearity among independent variables.
6. No significant outliers.

---

## Example

### Dataset

| Study Hours | Attendance (%) | Assignments Completed | Exam Score |
|------------|---------------|----------------------|-----------|
| 2 | 70 | 5 | 55 |
| 4 | 80 | 7 | 68 |
| 6 | 85 | 8 | 78 |
| 8 | 90 | 9 | 88 |
| 10 | 95 | 10 | 96 |

### Sample Regression Equation

Exam Score = 15 + 3(Study Hours) + 0.4(Attendance) + 2(Assignments)

### Prediction

For:
- Study Hours = 7
- Attendance = 88%
- Assignments = 8

Exam Score = 15 + 3(7) + 0.4(88) + 2(8)

Exam Score = 15 + 21 + 35.2 + 16

Exam Score = 87.2

Predicted Exam Score = 87.2

---

## Python Implementation

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
data = {
    'Study_Hours': [2, 4, 6, 8, 10],
    'Attendance': [70, 80, 85, 90, 95],
    'Assignments': [5, 7, 8, 9, 10],
    'Exam_Score': [55, 68, 78, 88, 96]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Study_Hours', 'Attendance', 'Assignments']]
y = df['Exam_Score']

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[7, 88, 8]])

print("Predicted Score:", prediction[0])

# Model parameters
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
```

---

## Advantages
- Handles multiple input variables.
- Provides better predictions than simple linear regression.
- Easy to interpret coefficients.
- Useful for understanding feature importance.

---

## Limitations
- Assumes linear relationships.
- Sensitive to outliers.
- Performance decreases with multicollinearity.
- May underperform on complex non-linear data.

---

## Applications
- House price prediction
- Sales forecasting
- Stock market analysis
- Healthcare analytics
- Business performance prediction
- Economic forecasting

---

## Evaluation Metrics
- R² Score (Coefficient of Determination)
- Adjusted R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## Conclusion
Multiple Linear Regression is a powerful extension of Simple Linear Regression that uses multiple independent variables to predict a dependent variable. It is widely used in machine learning, statistics, and data analytics for forecasting, trend analysis, and decision-making.