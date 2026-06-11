# 🍽️ FlavorSense: Lifestyle-Based Taste Preference Prediction using KNN Classification

## 📌 Project Overview

FlavorSense is a Machine Learning Classification project that predicts an individual's preferred taste category based on various lifestyle and environmental factors.

The project utilizes the K-Nearest Neighbors (KNN) Classification algorithm to analyze patterns in user behavior and accurately classify taste preferences into categories such as Salty, Sweet, Sour, and Spicy.

This project demonstrates the complete Machine Learning workflow including data preprocessing, feature engineering, exploratory data analysis, model training, hyperparameter tuning, and performance evaluation.

---

# 🎯 Problem Statement

Food preferences vary from person to person and are often influenced by lifestyle habits, environmental conditions, and personal experiences.

The objective of this project is to build a machine learning model capable of predicting an individual's preferred taste category based on factors such as age, sleep cycle, exercise habits, climate zone, and historical cuisine exposure.

The model aims to identify hidden relationships between lifestyle characteristics and taste preferences, enabling accurate classification and potential applications in personalized food recommendation systems.

---

# 🔄 Workflow Architecture

```text
Data Collection
      │
      ▼
Dataset Loading
      │
      ▼
Data Understanding
├── Shape Analysis
├── Data Types
├── Statistical Summary
└── Missing Value Check
      │
      ▼
Data Cleaning
├── Handle Missing Values
├── Remove Duplicate Records
└── Validate Data Quality
      │
      ▼
Exploratory Data Analysis (EDA)
├── Taste Distribution
├── Sleep Cycle Analysis
├── Climate Zone Analysis
├── Exercise Habit Analysis
└── Feature Relationship Analysis
      │
      ▼
Feature Engineering
├── Ordinal Encoding
│   ├── Sleep Cycle
│   └── Exercise Habits
├── One-Hot Encoding
│   ├── Climate Zone
│   └── Historical Cuisine Exposure
└── Label Encoding
    └── Preferred Taste
      │
      ▼
Feature Selection
(X Features)
      │
      ▼
Target Selection
(y Target)
      │
      ▼
Feature Scaling
(StandardScaler)
      │
      ▼
Train-Test Split
(80% Training | 20% Testing)
      │
      ▼
Hyperparameter Tuning
(Test Multiple K Values)
      │
      ▼
Model Training
(KNN Classifier)
      │
      ▼
Prediction
(y_pred)
      │
      ▼
Model Evaluation
├── Accuracy Score
├── Precision
├── Recall
├── F1-Score
└── Classification Report
      │
      ▼
Final Taste Preference Prediction
```

---

# 📊 Dataset Information

### Dataset Description

The dataset contains information about individuals and their lifestyle characteristics that may influence food taste preferences.

### Features

| Feature | Description |
|----------|-------------|
| Age | Age of Individual |
| Sleep Cycle | Sleeping Pattern |
| Exercise Habits | Physical Activity Level |
| Climate Zone | Environmental Region |
| Historical Cuisine Exposure | Previous Cuisine Experience |

### Target Variable

| Target |
|----------|
| Preferred Taste |

Possible Categories:

- Salty
- Sweet
- Sour
- Spicy

---

# 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

---

# 📋 Data Preprocessing

The following preprocessing steps were performed:

### Missing Value Handling

- Numerical Features → Mean Imputation
- Categorical Features → Mode Imputation

### Duplicate Handling

- Duplicate records were identified and removed.

### Data Validation

- Checked data types
- Verified null values
- Inspected feature distributions

---

# 📈 Exploratory Data Analysis (EDA)

Several visualizations and statistical analyses were performed to understand the dataset:

- Distribution of Preferred Taste
- Sleep Cycle Distribution
- Climate Zone Distribution
- Exercise Habit Analysis
- Age Distribution
- Relationship between Features and Target Variable
- Outlier Detection using Boxplots

---

# 🔧 Feature Engineering

## Ordinal Encoding

Applied to ordered categorical features:

### Sleep Cycle

| Category | Encoding |
|-----------|----------|
| Early Bird | 0 |
| Irregular | 1 |
| Night Owl | 2 |

### Exercise Habits

| Category | Encoding |
|-----------|----------|
| Light | 0 |
| Moderate | 1 |
| Heavy | 2 |

---

## One-Hot Encoding

Applied to:

- Climate Zone
- Historical Cuisine Exposure

---

## Label Encoding

Applied to:

- Preferred Taste (Target Variable)

---

# ⚖️ Feature Scaling

Since KNN is a distance-based algorithm, StandardScaler was applied to normalize feature values before model training.

Benefits:

- Prevents dominance of larger numerical values
- Improves distance calculations
- Enhances model performance

---

# 🤖 Model Building

## Algorithm Used

### K-Nearest Neighbors (KNN) Classifier

KNN is a supervised machine learning algorithm that classifies data points based on the majority class of their nearest neighbors.

### Hyperparameter Tuning

Different K values were tested to determine the optimal number of neighbors for classification.

The K value producing the highest testing accuracy was selected as the final model.

---

# 📊 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Classification Report

### Evaluation Process

```python
classification_report(y_test, y_pred)
accuracy_score(y_test, y_pred)
```

---

# ✅ Results

The KNN classifier successfully learned the relationship between lifestyle factors and taste preferences.

Key observations:

- Good classification performance across multiple taste categories.
- Feature scaling improved prediction accuracy.
- Hyperparameter tuning helped identify the optimal K value.
- The model demonstrated strong capability in predicting preferred taste classes.

---

# 📌 Conclusion

This project successfully developed a K-Nearest Neighbors (KNN) classification model capable of predicting an individual's preferred taste category using lifestyle and environmental factors.

The workflow included data preprocessing, exploratory analysis, feature engineering, scaling, model training, and evaluation. The results demonstrate that lifestyle characteristics such as sleep habits, exercise routines, climate conditions, and cuisine exposure significantly influence taste preferences.

The project highlights the effectiveness of KNN Classification in solving multi-class prediction problems and provides a strong foundation for developing intelligent food recommendation systems.

---

# 🚀 Future Scope

- Implement GridSearchCV for advanced hyperparameter optimization.
- Compare KNN with:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine
  - XGBoost
- Handle class imbalance using SMOTE.
- Deploy the model using Streamlit.
- Build a personalized food recommendation engine.

---

# 👨‍💻 Author

**Mahima Adhale**

Machine Learning | Data Science | Artificial Intelligence Enthusiast

---

## ⭐ Skills Demonstrated

- Data Cleaning
- Missing Value Treatment
- Exploratory Data Analysis
- Feature Engineering
- Feature Encoding
- Feature Scaling
- KNN Classification
- Hyperparameter Tuning
- Model Evaluation
- Machine Learning Workflow Design