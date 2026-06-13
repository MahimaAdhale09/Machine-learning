# 🌬️ Air Quality Ventilation Decision Prediction using Decision Tree Classification

## 📌 Project Overview

Maintaining good indoor air quality is essential for creating a healthy and comfortable learning environment. Factors such as carbon dioxide concentration (CO₂), particulate matter (PM2.5), temperature, humidity, occupancy, and classroom conditions significantly influence indoor air quality.

This project uses a Decision Tree Classifier to predict appropriate ventilation decisions based on classroom air quality measurements and environmental conditions. The model helps determine when ventilation actions are required to maintain a healthy indoor environment.

---

## 🎯 Problem Statement

The objective of this project is to build a machine learning classification model that predicts ventilation decisions using indoor air quality and environmental data collected from classrooms.

The dataset contains information such as CO₂ concentration, PM2.5 levels, temperature, humidity, student count, school period, and robot sensor positions. By analyzing these factors, the model learns patterns associated with ventilation requirements and predicts the appropriate ventilation action.

This predictive system can support smart classroom management, improve indoor air quality, and contribute to healthier learning environments.

---

# 🔄 Workflow Architecture

```text
Air Quality Dataset
          │
          ▼
Data Collection
(air_quality.csv)
          │
          ▼
Data Understanding
(Shape, Info,
Statistics)
          │
          ▼
Data Cleaning
(Check Missing Values
and Duplicates)
          │
          ▼
Exploratory Data Analysis
(Distribution Analysis,
Correlation Analysis,
Target Analysis)
          │
          ▼
Feature Encoding
(Label Encoding /
Ordinal Encoding)
          │
          ▼
Feature Selection
(X = Features,
Y = Ventilation Decision)
          │
          ▼
Train-Test Split
(Training & Testing Data)
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
Confusion Matrix,
Classification Report)
          │
          ▼
Decision Tree Visualization
          │
          ▼
Performance Analysis
          │
          ▼
Final Ventilation
Decision Prediction Model
```

---

## 📊 Dataset Structure

- The dataset contains classroom air quality and environmental information used to predict ventilation decisions.
- Each record represents a classroom observation collected through environmental sensors.

### Independent Variables

1. CO₂ Concentration
2. PM2.5 Concentration
3. Temperature
4. Humidity
5. Student Count
6. School Period
7. Robot Position X
8. Robot Position Y

### Target Variable

- Ventilation Decision

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
- Statistical Summary
- Missing Value Analysis
- Duplicate Value Analysis
- Feature Distribution Analysis
- Correlation Analysis
- Target Variable Analysis

---

## ⚙️ Data Preprocessing

### Data Cleaning

- Checked for Missing Values
- Checked for Duplicate Records

### Feature Encoding

- Encoded categorical variables into numerical format
- Prepared dataset for Decision Tree Classification

### Feature Selection

- Independent Variables (X)
- Target Variable (Y)

---

## 🤖 Model Building

### Train-Test Split

- Training Dataset
- Testing Dataset

### Model Used

- Decision Tree Classifier

### Model Training

- Fitted the model on training data
- Generated predictions on testing data

---

## 📊 Model Evaluation

Performance metrics used:

- Accuracy Score
- Confusion Matrix
- Classification Report
- Decision Tree Visualization

---

## 📌 Model Performance

| Metric | Value |
|----------|----------|
| Training Accuracy | 100% |
| Testing Accuracy | 100% |

---

## 📌 Conclusion

The Decision Tree Classifier achieved 100% training accuracy and 100% testing accuracy, demonstrating excellent predictive performance on the air quality dataset.

The model successfully learned the relationship between environmental conditions and ventilation decisions, accurately classifying all observations in both training and testing datasets. This indicates that the selected features contain strong predictive information for determining ventilation requirements.

The developed model can effectively support intelligent classroom ventilation management and contribute to maintaining healthier indoor environments.

---

## 🚀 Future Improvements

- Apply Random Forest Classifier
- Apply Gradient Boosting Models
- Perform Hyperparameter Tuning
- Use Cross Validation
- Deploy Using Streamlit
- Develop a Smart Air Quality Monitoring Dashboard
- Integrate Real-Time Sensor Data

---

## 📂 Project Structure

```text
Air-Quality-Ventilation-Prediction/
│
├── air_quality.csv
├── Decision-Tree-air_quality.ipynb
├── README.md
│
├── Data Preprocessing
├── Exploratory Data Analysis
├── Feature Encoding
├── Decision Tree Modeling
├── Model Evaluation
├── Prediction System
└── Tree Visualization
```

---

## 👨‍💻 Author

**Mahima Adhale**

Machine Learning & Data Science Enthusiast

Focused on Predictive Analytics, AI/ML, Environmental Data Science, and Smart Monitoring Systems.