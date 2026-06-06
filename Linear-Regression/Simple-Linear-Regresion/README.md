# Simple Linear Regression

## Overview
Simple Linear Regression is a statistical technique used to model the relationship between one independent variable (X) and one dependent variable (Y). It helps predict the value of the dependent variable based on the independent variable by fitting a straight line through the data.

### Regression Equation

y = mx + c

Where:
- y = Predicted value of the dependent variable
- x = Independent variable
- c = Intercept
- m = Slope of the regression line

---

## Objective
The main objectives of Simple Linear Regression are:
- To understand the relationship between two variables.
- To predict future outcomes.
- To identify trends in data.

---

## How It Works
1. Collect data for the independent and dependent variables.
2. Fit the best straight line using the least squares method.
3. Calculate the slope and intercept.
4. Use the regression equation to make predictions.

---

## Assumptions
Simple Linear Regression assumes:
1. Linear relationship between X and Y.
2. Independence of observations.
3. Constant variance of errors (Homoscedasticity).
4. Normally distributed residuals.
5. No significant outliers.

---

## Example

### Dataset

| Study Hours (X) | Exam Score (Y) |
|----------------|---------------|
| 1 | 50 |
| 2 | 55 |
| 3 | 65 |
| 4 | 70 |
| 5 | 80 |

### Fitted Equation

y = 42 + 7.5x

### Prediction

For 6 study hours:

y = 42 + (7.5 × 6)

y = 87

Predicted Exam Score = 87

---

## Python Implementation

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [50, 55, 65, 70, 80]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict for 6 study hours
prediction = model.predict([[6]])

print("Predicted Score:", prediction[0])

# Model parameters
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
```

---

## Advantages
- Easy to understand and implement.
- Fast and computationally efficient.
- Useful for prediction and trend analysis.
- Provides interpretable results.

---

## Limitations
- Assumes a linear relationship.
- Sensitive to outliers.
- Cannot model complex relationships.
- Depends heavily on data quality.

---

## Applications
- Sales forecasting
- House price prediction
- Stock market analysis
- Academic performance prediction
- Business analytics
- Healthcare research

---

## Evaluation Metrics
- R² Score (Coefficient of Determination)
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## Conclusion
Simple Linear Regression is one of the most fundamental machine learning algorithms used for predicting continuous values. It is easy to implement, interpretable, and serves as the foundation for many advanced regression techniques.