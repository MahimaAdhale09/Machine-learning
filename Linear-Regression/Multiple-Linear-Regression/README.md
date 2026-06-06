# Social Network Ads Purchase Prediction using Logistic Regression

## 📌 Project Overview
This project uses **Logistic Regression** to predict whether a customer will purchase a product based on demographic and social network advertising data.

The dataset contains information such as:
- Age
- Estimated Salary
- Gender
- Purchase Status (Target Variable)

The goal is to build a classification model that predicts customer purchasing behavior.

---

## 📂 Dataset Information

| Feature | Description |
|----------|-------------|
| User ID | Unique customer identifier |
| Gender | Male/Female |
| Age | Customer age |
| Estimated Salary | Annual estimated salary |
| Purchased | Target variable (0 = Not Purchased, 1 = Purchased) |

---

## 🛠️ Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 🔍 Data Preprocessing

### 1. Data Loading
- Loaded dataset using Pandas.

### 2. Data Exploration
- Checked data types
- Generated descriptive statistics

### 3. Duplicate Check
- Verified duplicate records using:
```python
df.duplicated().sum()
```

### 4. Missing Value Check
- Checked for null values using:
```python
df.isna().sum()
```

### 5. Outlier Detection
- Visualized outliers using boxplots.

### 6. Encoding
- Converted the categorical **Gender** column into numerical format using One-Hot Encoding.

```python
df = pd.get_dummies(df, columns=['Gender'], dtype=int)
```

### 7. Feature Selection
- Removed the `User ID` column since it does not contribute to prediction.

---

## 🤖 Model Building

### Defining Features and Target

```python
X = df.drop(columns=['Purchased'])
y = df['Purchased']
```

### Train-Test Split

```python
train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
```

- Training Data: 75%
- Testing Data: 25%

### Logistic Regression Model

```python
lr = LogisticRegression()
lr.fit(X_train, y_train)
```

---

## 📈 Prediction

```python
y_pred = lr.predict(X_test)
```

The trained model predicts whether a customer is likely to purchase the product.

---

## 📊 Model Evaluation

### Confusion Matrix

```python
confusion_matrix(y_test, y_pred)
```

### Heatmap Visualization

```python
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
plt.show()
```

### Classification Report

```python
classification_report(y_test, y_pred)
```

Evaluation metrics include:
- Accuracy
- Precision
- Recall
- F1-Score

---

## 🚀 Project Workflow

1. Import Libraries
2. Load Dataset
3. Explore Data
4. Check Duplicates
5. Handle Missing Values
6. Detect Outliers
7. Encode Categorical Features
8. Remove Unnecessary Columns
9. Split Data into Train & Test Sets
10. Train Logistic Regression Model
11. Make Predictions
12. Evaluate Model Performance

---

## 🎯 Conclusion

A Logistic Regression classifier was developed to predict customer purchase behavior from social network advertisement data. After preprocessing the dataset and encoding categorical variables, the model was trained and evaluated using classification metrics and a confusion matrix. The project demonstrates how Logistic Regression can be effectively applied to binary classification problems in marketing and customer analytics.

---

## 📁 Repository Structure

```text
├── Logistic Regression maam task.ipynb
├── Social_Network_Ads.csv
├── README.md
```

---

## 👩‍💻 Author

Mahima Adhale

**Domain:** Machine Learning & Data Analytics