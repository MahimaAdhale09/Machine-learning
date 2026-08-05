# House Price Prediction Using Gradient Boosting Regressor

## Project Overview

This project focuses on predicting residential house prices using the **Gradient Boosting Regressor** algorithm. The model is trained on the **Ames Housing Dataset**, which contains various structural, location-based, and property-related features that influence the selling price of a house.

The objective is to build an accurate regression model capable of estimating house prices based on historical housing data.

---

# Problem Statement

House prices are influenced by several factors such as location, construction quality, living area, garage capacity, basement area, neighborhood, and other property characteristics. Predicting house prices manually is difficult because of the large number of variables involved.

The aim of this project is to develop a machine learning model using the **Gradient Boosting Regressor** algorithm that accurately predicts the selling price of residential houses based on their features. The developed model can assist buyers, sellers, and real estate professionals in making informed pricing decisions.

---

# Objectives

- Predict the selling price of residential houses.
- Build an accurate Gradient Boosting Regression model.
- Analyze important housing features affecting house prices.
- Evaluate model performance using regression metrics.
- Generate price predictions for unseen test data.

---

# Dataset Information

**Dataset:** Ames Housing Dataset

### Training Dataset
- Records: **1460**
- Features: **81**
- Target Variable: **SalePrice**

### Testing Dataset
- Records: **1459**
- Features: **80**
- Used for prediction only.

---

# Target Variable

| Column | Description |
|---------|-------------|
| SalePrice | Selling price of the house |

---

# Data Structure

The dataset consists of the following categories:

- Property Identification
- Lot Information
- Property Location
- Building Information
- Construction Details
- Exterior Features
- Basement Information
- Heating & Utilities
- Living Area
- Bathrooms
- Bedrooms & Kitchen
- Fireplace Details
- Garage Information
- Outdoor Features
- Miscellaneous Features
- Sale Information
- Target Variable (SalePrice)

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

# Machine Learning Algorithm

- Gradient Boosting Regressor

---

# Project Workflow

### Step 1: Import Libraries
Import all required Python libraries for data manipulation, visualization, preprocessing, model building, and evaluation.

---

### Step 2: Load Dataset
- Load the training dataset.
- Load the testing dataset.

---

### Step 3: Data Understanding
- Display dataset information.
- Check shape of the dataset.
- Display first and last records.
- Generate descriptive statistics.

---

### Step 4: Data Preprocessing
- Handle missing values.
- Treat numerical missing values using appropriate imputation.
- Treat categorical missing values using most frequent values.
- Remove duplicate records (if any).
- Perform outlier analysis (if required).

---

### Step 5: Feature Engineering
- Apply Ordinal Encoding for ordered categorical variables.
- Apply One-Hot Encoding for nominal categorical variables.
- Align train and test datasets after encoding.

---

### Step 6: Prepare Data
- Separate independent and dependent variables.
- Define feature matrix (X).
- Define target variable (y).

---

### Step 7: Split Dataset
Split the training dataset into training and validation datasets using Train-Test Split.

---

### Step 8: Train Model
Train the Gradient Boosting Regressor using the training dataset.

---

### Step 9: Make Predictions
Predict house prices for:
- Validation dataset
- Testing dataset

---

### Step 10: Model Evaluation
Evaluate the model using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

### Step 11: Feature Importance
Analyze the most important features contributing to house price prediction.

---

### Step 12: Save Model
Save the trained model using Joblib or Pickle for future deployment.

---

# Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib
```

---

# Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# Advantages

- High prediction accuracy
- Handles complex non-linear relationships
- Robust ensemble learning algorithm
- Provides feature importance
- Suitable for structured/tabular datasets
- No feature scaling required

---

# Limitations

- Training can be computationally expensive.
- Requires hyperparameter tuning for optimal performance.
- Slower than a single Decision Tree.

---

# Project Structure

```
HousePricePrediction/
│
├── train.csv
├── test.csv
├── Home.ipynb
├── README.md
├── requirements.txt
├── model.pkl
└── submission.csv
```

---

# Expected Outcome

The trained Gradient Boosting Regressor predicts the selling price of residential houses with high accuracy by learning patterns from historical housing data. The model helps estimate property values and supports data-driven decision-making in the real estate industry.

---

# Future Enhancements

- Hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
- Compare with Random Forest, XGBoost, LightGBM, and CatBoost.
- Deploy the model using Flask, FastAPI, or Streamlit.
- Build a web-based house price prediction application.

---

# Author

**Mahima Adhale**

B.Tech – Computer Science & Engineering

Machine Learning & Data Science Enthusiast