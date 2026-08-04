# 🤖 Support Vector Machine (SVM) Classification

## 📌 Project Overview

This project demonstrates the implementation of the **Support Vector Machine (SVM)** algorithm for solving a **Binary Classification** problem using Python and Scikit-learn.

Support Vector Machine (SVM) is one of the most powerful supervised machine learning algorithms used for classification and regression tasks. It identifies the optimal hyperplane that maximizes the margin between different classes, resulting in better classification performance.

In this project, SVM is applied to classify water samples as **Potable** or **Not Potable** based on various physical and chemical properties.

---

# 🎯 Objective

The objective of this project is to:

- Understand the working of Support Vector Machine.
- Build an SVM Classification model.
- Perform data preprocessing.
- Handle class imbalance using ADASYN.
- Optimize model performance using GridSearchCV.
- Evaluate the model using different performance metrics.

---

# 🧠 What is Support Vector Machine (SVM)?

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression problems.

The primary goal of SVM is to find the **best decision boundary (hyperplane)** that separates different classes while maximizing the distance (margin) between them.

A larger margin generally improves the model's ability to classify unseen data.

---

# 📊 Features of SVM

- Supervised Machine Learning Algorithm
- Works well for Binary Classification
- Effective in High-Dimensional Data
- Finds Maximum Margin Hyperplane
- Uses Support Vectors for Classification
- Supports Linear and Non-Linear Classification
- Kernel Trick for Complex Decision Boundaries
- Good Generalization Performance

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook

---

# 📂 Dataset Information

The dataset consists of different physical and chemical properties used to determine water quality.

### Features

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

### Target

Potability

- 1 → Potable
- 0 → Not Potable

---

# 🔄 Machine Learning Workflow

```text
Start
   │
   ▼
Load Dataset
   │
   ▼
Data Preprocessing
   │
   ├── Missing Value Handling
   ├── Data Cleaning
   └── Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Feature Scaling
(StandardScaler)
   │
   ▼
Handle Imbalanced Dataset
(ADASYN)
   │
   ▼
Hyperparameter Tuning
(GridSearchCV)
   │
   ▼
Train SVM Model
   │
   ▼
Prediction
   │
   ▼
Model Evaluation
   │
   ├── Accuracy
   ├── Precision
   ├── Recall
   ├── F1 Score
   └── Confusion Matrix
   │
   ▼
End
```

---

# ⚙️ Data Preprocessing

The following preprocessing techniques were used:

- Missing Value Handling
- Feature Scaling using StandardScaler
- Train-Test Split
- ADASYN Oversampling
- Feature Transformation

---

# 🤖 Model Used

Support Vector Machine (SVM)

### Kernel Used

- Radial Basis Function (RBF)

### Hyperparameters

- Kernel = RBF
- C = 100
- Gamma = Auto

Hyperparameters were optimized using **GridSearchCV**.

---

# 📈 Evaluation Metrics

The model was evaluated using:

- Accuracy Score
- Classification Report
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 📦 Required Libraries

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
jupyter
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SVM-Classification.git
```

Move to project directory

```bash
cd SVM-Classification
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook

```bash
jupyter notebook
```

---

# 📁 Project Structure

```
SVM-Classification/
│
├── dataset.csv
├── SVC_water_potability.ipynb
├── README.md
├── requirements.txt
└── images/
```

---

# 📚 Advantages of SVM

- High Accuracy
- Works well with High-Dimensional Data
- Effective for Small and Medium Datasets
- Robust Against Overfitting
- Supports Multiple Kernel Functions
- Good Generalization Capability

---

# ⚠️ Limitations of SVM

- Slow Training on Large Datasets
- Sensitive to Parameter Selection
- Requires Feature Scaling
- Difficult to Interpret
- High Memory Usage for Large Data

---

# 🎯 Applications of SVM

- Disease Prediction
- Water Quality Prediction
- Spam Email Detection
- Face Recognition
- Image Classification
- Text Classification
- Fraud Detection
- Credit Risk Analysis
- Customer Churn Prediction

---

# 📖 Learning Outcomes

After completing this project, you will understand:

- Supervised Learning
- Binary Classification
- Support Vector Machine
- StandardScaler
- ADASYN Oversampling
- Hyperparameter Tuning
- GridSearchCV
- Model Evaluation
- Classification Metrics

---

# 👩‍💻 Author

**Mahima Adhale**

B.Tech Computer Science & Engineering

Machine Learning | Python | SQL | Data Analytics | Power BI

---

# ⭐ If you found this project useful, don't forget to Star this repository!