# ❤️ Heart Disease Prediction using Decision Tree Classification

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection of heart disease can help healthcare professionals take preventive measures and provide timely treatment. This project uses a Decision Tree Classifier to predict whether a patient is likely to have heart disease based on various medical and clinical attributes.

The project includes data preprocessing, exploratory data analysis (EDA), feature encoding, model training, pre-pruning, post-pruning, and performance evaluation to build an accurate and interpretable classification model.

---

## 🎯 Problem Statement

The objective of this project is to develop a machine learning classification model that predicts the presence of heart disease using patient medical and clinical data. The dataset contains demographic information, cardiovascular measurements, ECG results, and exercise-related indicators that influence heart health.

By analyzing these factors, the model classifies patients into heart disease and non-heart disease categories, helping support early diagnosis and healthcare decision-making.

---

# 🔄 Workflow Architecture

```text
Heart Disease Dataset
          │
          ▼
Data Collection (heart.csv)
          │
          ▼
Data Understanding
(Shape, Info, Statistics)
          │
          ▼
Data Cleaning
(Check Missing Values &
Duplicate Records)
          │
          ▼
Exploratory Data Analysis
(Boxplots, Countplots,
Pairplots, Group Analysis)
          │
          ▼
Feature Encoding
(Ordinal Encoding +
Label Encoding)
          │
          ▼
Feature Selection
(X = Features,
Y = HeartDisease)
          │
          ▼
Train-Test Split
(75% Train, 25% Test)
          │
          ▼
Decision Tree Classifier
(Entropy Criterion)
          │
          ▼
Model Evaluation
(Accuracy, Classification Report)
          │
          ▼
Pre-Pruning
(GridSearchCV
Max Depth &
Min Samples Split)
          │
          ▼
Post-Pruning
(Cost Complexity Pruning)
          │
          ▼
Performance Comparison
          │
          ▼
Final Heart Disease
Prediction Model
```

---

## 📊 Dataset Structure

- The dataset contains medical and clinical information of patients used to predict the presence of heart disease.
- Total Rows: **918**
- Total Columns: **12**

### Independent Variables

1. Age
2. Sex
3. ChestPainType
4. RestingBP
5. Cholesterol
6. FastingBS
7. RestingECG
8. MaxHR
9. ExerciseAngina
10. Oldpeak
11. ST_Slope

### Target Variable

- HeartDisease

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

- Statistical Summary
- Data Type Inspection
- Missing Value Analysis
- Duplicate Value Detection
- Boxplot Visualization
- Countplot Analysis
- Pairplot Visualization
- Group-wise Aggregation Analysis

---

## ⚙️ Data Preprocessing

### Ordinal Encoding

Applied on:

- ChestPainType
- RestingECG

### Label Encoding

Applied on:

- Sex
- ExerciseAngina
- ST_Slope

---

## 🤖 Model Building

### Train-Test Split

- Training Data: 75%
- Testing Data: 25%
- Random State: 42

### Base Model

- Decision Tree Classifier
- Criterion: Entropy

### Pre-Pruning

Hyperparameter tuning performed using GridSearchCV:

- max_depth = [5, 6, 7, 8]
- min_samples_split = [3, 5, 7, 9]

### Post-Pruning

Performed using:

- Cost Complexity Pruning (ccp_alpha)

---

## 📊 Model Performance

| Model | Training Accuracy | Testing Accuracy |
|---------|---------|---------|
| Decision Tree (Without Pruning) | 100.00% | 79.57% |
| Pre-Pruned Decision Tree | 89.24% | 85.22% |
| Post-Pruned Decision Tree | 81.83% | 80.00% |

---

## 📌 Conclusion

The initial Decision Tree model achieved perfect training accuracy but showed lower testing accuracy, indicating overfitting. To improve generalization, both pre-pruning and post-pruning techniques were applied.

Among all models, the pre-pruned Decision Tree achieved the highest testing accuracy of 85.22%, providing the best balance between model complexity and predictive performance. Therefore, the pre-pruned Decision Tree is selected as the final model for heart disease prediction.

---

## 🚀 Future Improvements

- Apply Random Forest Classifier
- Apply Gradient Boosting Models
- Perform Feature Selection Techniques
- Use Cross Validation
- Deploy Model using Flask or Streamlit
- Build a Healthcare Prediction Dashboard

---

## 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── heart.csv
├── Decision Tree-heart.ipynb
├── README.md
│
├── Data Preprocessing
├── Exploratory Data Analysis
├── Feature Encoding
├── Decision Tree Modeling
├── Pre-Pruning
├── Post-Pruning
└── Model Evaluation
```

---

## 👨‍💻 Author

**Mahima Adhale**

Machine Learning & Data Science Enthusiast

Focused on Predictive Analytics, AI/ML, and Healthcare Data Science.