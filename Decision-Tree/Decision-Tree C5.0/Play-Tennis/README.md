# 🎾 Play Tennis Prediction using Decision Tree Classification

## 📌 Project Overview

Weather conditions play a significant role in determining whether outdoor sports activities can be conducted. This project uses a Decision Tree Classifier to predict whether a tennis match can be played based on different weather conditions such as outlook, temperature, humidity, and wind.

The project demonstrates how Decision Tree algorithms can be used to solve classification problems by learning decision rules from historical weather data and predicting whether the outcome will be "Play Tennis" or "Do Not Play Tennis".

---

## 🎯 Problem Statement

The objective of this project is to build a machine learning classification model that predicts whether a tennis match can be played based on weather conditions. The dataset contains meteorological attributes such as outlook, temperature, humidity, and wind conditions that influence the decision to play tennis.

By analyzing these weather-related factors, the model learns patterns from historical data and classifies whether the conditions are suitable for playing tennis. This helps demonstrate the application of Decision Tree Classification for decision-making and predictive analytics.

---

# 🔄 Workflow Architecture

```text
Play Tennis Dataset
          │
          ▼
Data Collection
(play_tennis.csv)
          │
          ▼
Data Understanding
(Shape, Info,
Data Types)
          │
          ▼
Data Cleaning
(Check Missing Values
and Duplicates)
          │
          ▼
Exploratory Data Analysis
(Category Analysis,
Target Distribution)
          │
          ▼
Feature Encoding
(Label Encoding /
Ordinal Encoding)
          │
          ▼
Feature Selection
(X = Features,
Y = Play Tennis)
          │
          ▼
Train-Test Split
          │
          ▼
Decision Tree Classifier
          │
          ▼
Model Training
          │
          ▼
Prediction
          │
          ▼
Model Evaluation
(Accuracy Score,
Confusion Matrix)
          │
          ▼
Decision Tree Visualization
          │
          ▼
Final Tennis Play
Prediction Model
```

---

## 📊 Dataset Structure

- The dataset contains weather-related information used to predict whether a tennis match can be played.
- Each row represents a weather condition record and the corresponding decision to play tennis.

### Independent Variables

1. Outlook
2. Temperature
3. Humidity
4. Wind

### Target Variable

- Play Tennis

### Problem Type

- Classification Problem

### Algorithm Used

- Decision Tree Classifier

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

---

## 📈 Exploratory Data Analysis

The following analyses were performed:

- Dataset Inspection
- Data Type Analysis
- Missing Value Analysis
- Duplicate Value Analysis
- Target Variable Distribution
- Feature Distribution Analysis

---

## ⚙️ Data Preprocessing

### Encoding Techniques

Applied encoding techniques on categorical variables:

- Outlook
- Temperature
- Humidity
- Wind

Converted categorical features into numerical values suitable for machine learning algorithms.

---

## 🤖 Model Building

### Train-Test Split

- Training Dataset
- Testing Dataset

### Model Used

- Decision Tree Classifier

### Model Training

- Fitted Decision Tree on training data.
- Generated predictions on testing data.

---

## 📊 Model Evaluation

Performance metrics used:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📌 Conclusion

The Decision Tree Classifier successfully learned the relationships between weather conditions and tennis-playing decisions. By analyzing outlook, temperature, humidity, and wind conditions, the model can accurately predict whether a tennis match should be played.

The model provides an interpretable decision-making process through tree-based rules, making it easy to understand how weather factors influence the final prediction.

---

## 🚀 Future Improvements

- Apply Random Forest Classifier
- Apply Gradient Boosting Techniques
- Perform Hyperparameter Tuning
- Compare Multiple Classification Algorithms
- Deploy Model using Streamlit
- Build an Interactive Prediction Dashboard

---

## 📂 Project Structure

```text
Play-Tennis-Prediction/
│
├── play_tennis.csv
├── Decision Tree-playtennis.ipynb
├── README.md
│
├── Data Preprocessing
├── Exploratory Data Analysis
├── Feature Encoding
├── Decision Tree Modeling
├── Model Evaluation
└── Tree Visualization
```

---

## 👨‍💻 Author

**Mahima Adhale
**

Machine Learning & Data Science Enthusiast

Focused on Predictive Analytics, AI/ML, and Data Science Projects.