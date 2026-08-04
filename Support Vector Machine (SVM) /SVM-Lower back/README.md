# 🩺 Vertebral Column Classification Using Support Vector Machine (SVM)

## 📌 Project Overview

Lower back disorders are among the most common musculoskeletal problems that affect millions of people worldwide. Early detection of vertebral abnormalities can help healthcare professionals provide timely treatment and improve patient outcomes.

This project implements a **Support Vector Machine (SVM)** classification model to predict whether a patient's vertebral column condition is **Normal** or **Abnormal** using biomechanical measurements of the spine.

The project includes data preprocessing, feature scaling, hyperparameter tuning, model training, prediction, and performance evaluation using various classification metrics.

---

# 🎯 Problem Statement

Diagnosing vertebral column disorders manually can be time-consuming and may depend on the expertise of medical professionals. Machine Learning provides an efficient approach for predicting spinal conditions using biomechanical measurements.

The objective of this project is to develop a **Support Vector Machine (SVM)** model capable of accurately classifying vertebral column conditions into **Normal** and **Abnormal** categories, thereby assisting in early diagnosis and improving clinical decision-making.

---

# 📂 Dataset Information

- **Dataset Name:** Vertebral Column Dataset (column_2C_weka.csv)

- **Total Rows:** 310

- **Total Columns:** 7

## Independent Variables

- Pelvic Incidence
- Pelvic Tilt
- Lumbar Lordosis Angle
- Sacral Slope
- Pelvic Radius
- Degree of Spondylolisthesis

## Target Variable

- Class

## Target Classes

- AB → Abnormal
- NO → Normal

## Problem Type

**Binary Classification**

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Support Vector Machine (SVM)
- GridSearchCV
- StandardScaler
- Jupyter Notebook

---

# 📊 Data Preprocessing

The following preprocessing steps were performed:

- Data Loading
- Data Exploration
- Checking Missing Values
- Feature Selection
- Label Encoding
- Train-Test Split
- Feature Scaling using StandardScaler

---

# 🤖 Machine Learning Model

**Support Vector Machine (SVM)**

The model was optimized using **GridSearchCV** to identify the best hyperparameters and improve classification performance.

---

# 📈 Model Performance

| Metric | Value |
|---------|-------|
| Training Accuracy | **91.27%** |
| Testing Accuracy | **80.65%** |

### Classification Report

| Class | Precision | Recall | F1-Score |
|------|-----------|--------|----------|
| Normal | 0.92 | 0.80 | 0.85 |
| Abnormal | 0.62 | 0.83 | 0.71 |

Overall Accuracy: **80.65%**

---

# 📊 Confusion Matrix

```
                Predicted

               Normal  Abnormal

Actual Normal      35        9

Actual Abnormal     3       15
```

---

# 🔄 Project Workflow

```text
                  Vertebral Column Dataset
                             │
                             ▼
                     Load Dataset
                             │
                             ▼
                  Data Exploration (EDA)
                             │
                             ▼
              Handle Missing Values (if any)
                             │
                             ▼
                    Feature Selection
                             │
                             ▼
                    Label Encoding
                             │
                             ▼
                    Train-Test Split
                             │
                             ▼
             Feature Scaling (StandardScaler)
                             │
                             ▼
        Hyperparameter Tuning (GridSearchCV)
                             │
                             ▼
          Train Support Vector Machine (SVM)
                             │
                             ▼
                  Predict Test Dataset
                             │
                             ▼
                 Evaluate Model Performance
                             │
          ┌──────────────────┼──────────────────┐
          ▼                  ▼                  ▼
     Accuracy          Classification     Confusion Matrix
                           Report
                             │
                             ▼
                Vertebral Column Prediction
```

---

# 📁 Project Structure

```
Vertebral-Column-Classification/
│
├── column_2C_weka.csv
├── SVC.ipynb
├── README.md
├── requirements.txt
└── images/
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Vertebral-Column-Classification.git
```

Go to the project directory

```bash
cd Vertebral-Column-Classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook

```bash
jupyter notebook
```

Open

```
SVC.ipynb
```

---

# 📦 Required Libraries

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter
```

---

# 🚀 Future Improvements

- Compare SVM with Random Forest, XGBoost, and Logistic Regression.
- Perform feature engineering to improve model performance.
- Deploy the model using Flask, FastAPI, or Streamlit.
- Develop a web application for real-time vertebral column prediction.
- Train the model using a larger medical dataset.

---

# 🎯 Key Features

- Binary Classification Problem
- Data Preprocessing
- Feature Scaling
- Support Vector Machine (SVM)
- Hyperparameter Tuning
- GridSearchCV
- Confusion Matrix
- Classification Report
- Accuracy Evaluation
- End-to-End Machine Learning Pipeline

---

# 📚 Learning Outcomes

This project demonstrates:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Label Encoding
- Feature Scaling
- Support Vector Machine (SVM)
- Hyperparameter Tuning using GridSearchCV
- Binary Classification
- Model Evaluation
- Confusion Matrix Interpretation

---

# 📌 Conclusion

The Support Vector Machine (SVM) model successfully classified vertebral column conditions into **Normal** and **Abnormal** categories. After preprocessing, feature scaling, and hyperparameter tuning, the model achieved a **training accuracy of 91.27%** and a **testing accuracy of 80.65%**.

The results indicate that the model generalizes well to unseen data and demonstrates reliable performance for classifying spinal conditions. This project highlights the effectiveness of SVM in medical diagnosis and can serve as a foundation for future healthcare applications.

---

# 👩‍💻 Author

**Mahima Adhale**

**B.Tech – Computer Science & Engineering**

**Skills:** Python | Machine Learning | SQL | Power BI | Data Analytics

---

# ⭐ If you found this project useful, don't forget to Star this repository!