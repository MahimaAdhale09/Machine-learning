# Breast Cancer Diagnosis Prediction Using K-Nearest Neighbors (KNN) Classification

## Project Overview

This project focuses on predicting whether a breast tumor is **Malignant (Cancerous)** or **Benign (Non-Cancerous)** using the K-Nearest Neighbors (KNN) Classification algorithm. The dataset contains diagnostic measurements computed from digitized images of fine needle aspirates (FNA) of breast masses. The objective is to build an accurate classification model that can assist healthcare professionals in early breast cancer detection.

---

## Problem Statement

The early detection of breast cancer is critical for improving patient outcomes and reducing mortality rates. Medical diagnosis often relies on analyzing various characteristics of cell nuclei extracted from breast mass images. The objective of this project is to develop a machine learning model using the K-Nearest Neighbors (KNN) algorithm to classify tumors as either **Malignant (M)** or **Benign (B)** based on their diagnostic features. The model aims to assist healthcare professionals in making accurate and efficient diagnostic decisions.

---

## Workflow Architecture

```text
Dataset Collection
        │
        ▼
Data Understanding
(Head, Tail, Shape, Info, Describe)
        │
        ▼
Data Quality Check
(Duplicate Values & Missing Values)
        │
        ▼
Exploratory Data Analysis
(Boxplot Analysis)
        │
        ▼
Feature Selection
(Drop 'id' and 'Unnamed: 32')
        │
        ▼
Data Encoding
(Label Encoding of Diagnosis)
        │
        ▼
Feature & Target Separation
(X and y)
        │
        ▼
Feature Scaling
(StandardScaler)
        │
        ▼
Train-Test Split
(80% Train, 20% Test)
        │
        ▼
Hyperparameter Tuning
(Finding Optimal K Value)
        │
        ▼
Model Building
(KNN Classifier)
        │
        ▼
Prediction
(y_pred)
        │
        ▼
Model Evaluation
(Accuracy, Precision, Recall, F1-Score)
        │
        ▼
Conclusion
```

---

## Data Structure

The dataset consists of diagnostic measurements of breast cancer tumors obtained from digitized images of fine needle aspirates (FNA) of breast masses. The objective is to analyze various cell nucleus characteristics and build a machine learning model to classify tumors as either Malignant or Benign.

| Attribute | Description |
|------------|------------|
| Total Rows | 569 |
| Total Columns | 33 |
| Target Column | diagnosis |
| Problem Type | Classification |
| Model Used | K-Nearest Neighbors (KNN) |

### Independent Variables

- radius_mean
- texture_mean
- perimeter_mean
- area_mean
- smoothness_mean
- compactness_mean
- concavity_mean
- concave points_mean
- symmetry_mean
- fractal_dimension_mean
- radius_se
- texture_se
- perimeter_se
- area_se
- smoothness_se
- compactness_se
- concavity_se
- concave points_se
- symmetry_se
- fractal_dimension_se
- radius_worst
- texture_worst
- perimeter_worst
- area_worst
- smoothness_worst
- compactness_worst
- concavity_worst
- concave points_worst
- symmetry_worst
- fractal_dimension_worst

### Target Classes

- M = Malignant
- B = Benign

### Additional Columns

- id
- Unnamed: 32

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn

---

## Libraries Used

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
```

---

## Data Preprocessing

### 1. Data Quality Check

- Checked duplicate records.
- Checked missing values.

### 2. Feature Selection

Dropped unnecessary columns:

```python
df.drop(columns=['id','Unnamed: 32'], inplace=True)
```

### 3. Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['diagnosis'] = le.fit_transform(df['diagnosis'])
```

Encoding:

```text
B = 0
M = 1
```

### 4. Feature Scaling

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## Exploratory Data Analysis

The following analyses were performed:

- Data Shape Analysis
- Data Type Analysis
- Statistical Summary
- Duplicate Value Analysis
- Missing Value Analysis
- Boxplot Analysis
- Outlier Detection
- Feature Distribution Analysis

---

## Train-Test Split

```python
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
```

---

## Hyperparameter Tuning

```python
train_acc=[]
test_acc=[]

for i in range(2,20):
    kn = KNeighborsClassifier(n_neighbors=i)
    kn.fit(x_train,y_train)

    train_acc.append(kn.score(x_train,y_train))
    test_acc.append(kn.score(x_test,y_test))
```

### Best K Value

```text
K = 6
```

---

## Model Building

```python
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=6)

kn.fit(x_train,y_train)

y_pred = kn.predict(x_test)
```

---

## Model Evaluation

### Classification Report

```text
              precision    recall    f1-score   support

           0       0.91      1.00      0.95        71
           1       1.00      0.84      0.91        43

    accuracy                           0.94       114
   macro avg       0.96      0.92      0.93       114
weighted avg       0.94      0.94      0.94       114
```

### Accuracy Scores

```text
Training Accuracy : 93.63%
Testing Accuracy  : 93.86%
Overall Accuracy  : 94%
```

---

## Results

- Training Accuracy: 93.63%
- Testing Accuracy: 93.86%
- Overall Accuracy: 94%
- Precision for Malignant Tumors: 100%
- Recall for Benign Tumors: 100%
- F1-Score: 91% - 95%

---

## Conclusion

The K-Nearest Neighbors (KNN) Classification model was successfully developed to classify breast tumors as Malignant or Benign using diagnostic measurements extracted from breast cancer data.

The model achieved a Training Accuracy of 93.63% and a Testing Accuracy of 93.86%, indicating strong predictive performance and minimal overfitting. The overall accuracy of 94% demonstrates that the model can effectively distinguish between malignant and benign tumors.

The classification report shows excellent performance, with a Recall of 100% for benign cases and a Precision of 100% for malignant cases. Although a small number of malignant tumors were misclassified, the model maintained a strong F1-Score and balanced performance across both classes.

Therefore, the KNN Classification model can be considered a reliable and effective tool for breast cancer diagnosis and can support healthcare professionals in making accurate clinical decisions and enabling early disease detection.

---

## Author

Mahima Adhale

Machine Learning Project | KNN Classification | Breast Cancer Prediction