````markdown
# Gradient Boosting Regressor

## Overview

Gradient Boosting Regressor is a supervised machine learning algorithm used for regression tasks. It is an ensemble learning technique that combines multiple weak learners (Decision Trees) sequentially to create a strong predictive model. Each new tree is trained to correct the errors made by the previous trees, resulting in highly accurate predictions.

---

## Features

- Supervised Machine Learning Algorithm
- Used for Regression Problems
- Ensemble Learning Technique
- Builds Trees Sequentially
- Minimizes Prediction Error
- Handles Non-Linear Relationships
- Provides Feature Importance
- High Prediction Accuracy
- Does Not Require Feature Scaling

---

## Applications

- House Price Prediction
- Sales Forecasting
- Medical Cost Prediction
- Insurance Cost Prediction
- Demand Forecasting
- Energy Consumption Prediction
- Stock Price Prediction
- Revenue Forecasting

---

## Prerequisites

Before running the project, install the following libraries:

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

Install them using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib
```

---

## Required Libraries

```python
import pandas as pd
import numpy as np

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib
```

---

## Workflow

### 1. Load Dataset

Load the dataset into a Pandas DataFrame.

### 2. Data Preprocessing

- Handle Missing Values
- Remove or Cap Outliers (Optional)
- Encode Categorical Variables
- Feature Selection (Optional)

### 3. Split Dataset

Split the dataset into training and testing sets.

### 4. Train Model

Train the Gradient Boosting Regressor using the training data.

### 5. Make Predictions

Predict target values using the trained model.

### 6. Evaluate Model

Evaluate model performance using regression metrics.

### 7. Save Model

Save the trained model for future use.

---

## Model Initialization

```python
model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
```

---

## Model Training

```python
model.fit(X_train, y_train)
```

---

## Prediction

```python
y_pred = model.predict(X_test)
```

---

## Model Evaluation

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE :", rmse)
print("R2 Score :", r2)
```

---

## Feature Importance

```python
feature_importance = pd.Series(
    model.feature_importances_,
    index=X_train.columns
).sort_values(ascending=False)

print(feature_importance.head(10))
```

---

## Save Model

```python
joblib.dump(model, "gradient_boosting_model.pkl")
```

---

## Load Saved Model

```python
model = joblib.load("gradient_boosting_model.pkl")
```

---

## Hyperparameters

| Parameter | Description |
|-----------|-------------|
| n_estimators | Number of boosting stages |
| learning_rate | Controls contribution of each tree |
| max_depth | Maximum depth of each tree |
| min_samples_split | Minimum samples required to split a node |
| min_samples_leaf | Minimum samples required at a leaf node |
| subsample | Fraction of samples used for training each tree |
| random_state | Ensures reproducibility |

---

## Advantages

- High Prediction Accuracy
- Works Well on Structured Data
- Handles Non-Linear Relationships
- Less Overfitting Than a Single Decision Tree
- Provides Feature Importance
- No Feature Scaling Required
- Effective for Regression Problems

---

## Limitations

- Slower Training Time
- Sensitive to Hyperparameters
- Computationally Expensive
- Can Overfit if Too Many Trees Are Used
- Requires Parameter Tuning for Best Performance

---

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Recommended Workflow

1. Import Libraries
2. Load Dataset
3. Handle Missing Values
4. Encode Categorical Variables
5. Split Dataset
6. Train Gradient Boosting Regressor
7. Predict Target Values
8. Evaluate Performance
9. Save Model
10. Deploy Model

---

## Project Structure

```
GradientBoostingProject/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── notebooks/
│   └── GradientBoosting.ipynb
│
├── models/
│   └── gradient_boosting_model.pkl
│
├── README.md
│
├── requirements.txt
│
└── LICENSE
```

---

## Conclusion

Gradient Boosting Regressor is one of the most powerful ensemble learning algorithms for regression tasks. It sequentially improves prediction accuracy by minimizing previous errors, making it suitable for real-world applications such as house price prediction, forecasting, and financial analysis. With proper preprocessing and hyperparameter tuning, Gradient Boosting can achieve excellent predictive performance on structured datasets.

---

## License

This project is licensed under the MIT License.

---

## Author

**MAHIMA ADHALE**

