# 🚗 Used Car Price Prediction Using Machine Learning

## 📌 Project Overview

This project predicts the selling price of used cars using Machine Learning Regression algorithms. The notebook includes data preprocessing, exploratory data analysis (EDA), feature encoding, model training, regularization techniques, and model evaluation to identify the best-performing regression model.

---

# 📌 Problem Statement

The price of a used car depends on multiple factors such as:

- Car Brand
- Manufacturing Year
- Fuel Type
- Engine Type
- Body Style
- Drive Wheels
- Engine Location
- Horsepower
- Engine Size
- Mileage
- Various Technical Specifications

The objective of this project is to build a machine learning regression model capable of accurately predicting the price of a used car based on these features.

---

# 🏗️ Workflow Architecture

```
                    Used Car Dataset
                           │
                           ▼
                  Data Loading (Pandas)
                           │
                           ▼
                 Data Understanding
        (Shape, Info, Describe, Head, Tail)
                           │
                           ▼
                  Data Quality Check
        (Missing Values, Duplicate Records)
                           │
                           ▼
              Exploratory Data Analysis
      • Boxplots
      • Pairplots
      • Bar Charts
      • Feature Relationships
                           │
                           ▼
                 Feature Engineering
      • Binary Mapping
      • One-Hot Encoding
                           │
                           ▼
            Feature Selection (X & y)
                           │
                           ▼
              Train-Test Split (80:20)
                           │
                           ▼
               Model Training
      • Linear Regression
      • Lasso Regression
      • Ridge Regression
      • ElasticNet Regression
                           │
                           ▼
            Hyperparameter Tuning
          (Different Alpha Values)
                           │
                           ▼
              Final ElasticNet Model
                           │
                           ▼
                  Model Prediction
                           │
                           ▼
               Performance Evaluation
      • MAE
      • MSE
      • RMSE
      • R² Score
                           │
                           ▼
                 Final Price Prediction
```

---

# 📂 Dataset Information

The dataset contains information related to used cars, including:

- Car Make
- Fuel Type
- Engine Location
- Body Style
- Drive Wheels
- Engine Type
- Horsepower
- Engine Size
- Price (Target Variable)

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

# 📚 Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import (
    LinearRegression,
    Lasso,
    Ridge,
    ElasticNet
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
```

---

# 🔍 Data Preprocessing

The following preprocessing steps were performed:

- Loaded dataset using Pandas
- Checked dataset dimensions
- Displayed statistical summary
- Verified data types
- Checked missing values
- Removed duplicate records (if any)
- Explored categorical features
- Prepared data for modeling

---

# 📊 Exploratory Data Analysis (EDA)

EDA was performed to understand the relationships between variables using:

- Box Plot
- Pair Plot
- Fuel Type vs Engine Location Analysis
- Statistical Summary
- Distribution Analysis

---

# 🔄 Feature Engineering

### Binary Encoding

- Fuel Type
- Engine Location

### One-Hot Encoding

Applied on:

- Make
- Body Style
- Drive Wheels
- Engine Type

---

# 🤖 Machine Learning Models

The following regression models were implemented:

1. Linear Regression
2. Lasso Regression
3. Ridge Regression
4. ElasticNet Regression

---

# ⚙️ Hyperparameter Tuning

Regularization models were trained with multiple alpha values to identify the optimal model.

Algorithms tuned:

- Lasso
- Ridge
- ElasticNet

---

# 🧪 Model Evaluation Metrics

The trained model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 📈 Final Model

The final model selected in this notebook is:

**ElasticNet Regression**

Reason:

- Handles overfitting effectively
- Balances L1 and L2 regularization
- Provides stable performance

---

# 📁 Project Structure

```
Used-Car-Price-Prediction/
│
├── Cars.ipynb
├── cars.csv
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Used-Car-Price-Prediction.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Notebook

```bash
jupyter notebook Cars.ipynb
```

---

# 📌 Future Improvements

- Feature Scaling
- Cross Validation
- Random Forest Regressor
- XGBoost Regressor
- LightGBM
- CatBoost
- Model Deployment using Flask or Streamlit
- Hyperparameter Optimization using GridSearchCV

---

# 🎯 Conclusion

This project demonstrates a complete machine learning workflow for predicting used car prices. The notebook includes data preprocessing, visualization, feature encoding, regression model training, regularization techniques, and performance evaluation. Among the implemented models, ElasticNet Regression was selected as the final model after experimenting with different alpha values, providing a balanced approach to reducing overfitting while maintaining predictive performance.

---

# 👨‍💻 Author

**Mahima Adhale**

B.Tech Computer Science & Engineering

Machine Learning | Data Science | AI Enthusiast