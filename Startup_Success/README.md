
# 🚀 Startup Success Prediction — End-to-End Machine Learning Project

A machine learning-based web application that predicts the likelihood of startup success or failure using business, financial, founder, and market-related features.

The project demonstrates an end-to-end machine learning workflow, including Exploratory Data Analysis (EDA), data preprocessing, feature engineering, model comparison, evaluation, pipeline development, and deployment through Streamlit.

## 📊 Project Highlights

| Feature | Details |
|---|---|
| Project Name | Startup Success Prediction |
| Domain | Data Science, Machine Learning |
| Problem Type | Binary Classification |
| Dataset Size | 5,000 Startup Records |
| Original Features | 23 Features + Target |
| Final Input Features | 16 |
| Training Records | 4,000 |
| Testing Records | 1,000 |
| Final Model | Gradient Boosting Classifier |
| Final Test Accuracy | **81.7%** |
| Best Accuracy in Model Comparison | 83.4% — Logistic Regression |
| Programming Language | Python |
| ML Framework | Scikit-learn |
| Web Application | Streamlit |
| Model Serialization | Pickle |

**Final Pipeline Accuracy: 81.7%**

The saved pipeline uses Gradient Boosting. Although Logistic Regression achieved a higher test score of 83.4% during model comparison, Gradient Boosting was selected for the final application.

---

## 1. Project Overview

Predicting startup success is a challenging business problem because a startup's performance depends on several interconnected factors.

These include:

- Founder experience
- Funding availability
- Funding stage
- Team size
- Business sector
- Monthly revenue growth
- Customer retention
- Market competition
- Monthly burn rate
- Customer satisfaction

This project uses historical startup records to train a supervised machine learning classification model.

The final model is integrated into a Streamlit web application where users can enter startup details and receive a predicted outcome.

### Project Objectives

1. Understand startup performance data through EDA.
2. Identify features associated with startup success.
3. Clean and preprocess numerical and categorical data.
4. Build multiple machine learning classification models.
5. Evaluate and compare model performance.
6. Develop a reusable Scikit-learn prediction pipeline.
7. Save the trained model for future inference.
8. Build an interactive Streamlit prediction interface.

---

## 2. Problem Statement

Startup founders and investors analyze various indicators when evaluating business potential.

However, combining numerous financial, operational, and market-related factors can be complex.

The goal of this project is to develop a machine learning system that predicts the binary success outcome recorded in the provided startup dataset.

### Target Variable

The target column is:

`success`

| Value | Meaning |
|---|---|
| 0 | Startup Failure |
| 1 | Startup Success |

The model learns relationships between historical startup characteristics and these outcome labels.

**Important:** The prediction is a statistical estimate based on the supplied dataset, not a guarantee that a real startup will succeed or fail.

---

## 3. Technologies Used

### Programming
- Python

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn
- Logistic Regression
- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)
- Decision Tree

### Data Preprocessing
- SimpleImputer
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- Pipeline

### Model Evaluation
- Accuracy Score
- Precision
- Recall
- F1-Score
- Classification Report

### Web Development
- Streamlit

### Development Tools
- Jupyter Notebook
- Pickle

---

## 4. Dataset Description

**Dataset:** `startup_success_dataset.csv`

The dataset provided with this project contains 5,000 startup records and 24 columns, including the target.

### Dataset Summary

| Property | Value |
|---|---:|
| Total Records | 5,000 |
| Total Columns | 24 |
| Input Columns Before Feature Removal | 23 |
| Target Columns | 1 |
| Duplicate Rows | 0 |
| Startup Sectors | 12 |
| Countries | 8 |
| Funding Stages | 5 |

### Dataset Features

The original dataset contains:

| Feature | Description |
|---|---|
| startup_id | Unique startup identifier |
| founded_year | Startup founding year |
| sector | Startup industry |
| country | Country of operation |
| city_tier | City category |
| num_founders | Number of founders |
| founder_avg_experience_years | Average founder experience |
| has_prior_startup_experience | Previous startup experience indicator |
| has_technical_cofounder | Technical cofounder indicator |
| team_size | Number of team members |
| funding_stage | Current funding stage |
| total_funding_usd_million | Total funding in USD millions |
| num_funding_rounds | Number of funding rounds |
| monthly_burn_rate_usd_k | Monthly burn rate in USD thousands |
| market_size_billion_usd | Estimated market size |
| num_active_competitors | Number of active competitors |
| product_launch_months_after_founding | Time until product launch |
| num_patents_filed | Number of patents filed |
| has_female_founder | Female founder indicator |
| monthly_active_users_k | Monthly active users in thousands |
| mom_revenue_growth_pct | Month-over-month revenue growth |
| customer_retention_rate_pct | Customer retention percentage |
| nps_score | Net Promoter Score |
| success | Target variable |

The dataset is included in the uploaded project materials. Its original collection methodology and representativeness of real-world startups have not been independently established.

---

## 5. Complete Machine Learning Workflow

```text
START
  |
  v
Load Startup Dataset
  |
  v
Data Understanding
  |
  v
Exploratory Data Analysis
  |
  v
Missing Value Analysis
  |
  v
Duplicate and Outlier Checks
  |
  v
Feature Engineering
  |
  v
Feature Selection Analysis
  |
  v
Identify Numerical and Categorical Features
  |
  v
Train-Test Split (80:20)
  |
  v
Fit Preprocessing on Training Data
  |
  +---------------------------+
  |                           |
  v                           v
Numerical Features        Categorical Features
  |                           |
  v                           v
Median Imputation         Mode Imputation
  |                           |
  v                           v
Standard Scaling          One-Hot Encoding
  |                           |
  +-------------+-------------+
                |
                v
        Model Training
                |
                v
        Model Comparison
                |
                v
       Gradient Boosting
                |
                v
        Model Evaluation
                |
                v
     Scikit-learn Pipeline
                |
                v
       Save as model.pkl
                |
                v
      Streamlit Application
                |
                v
       Startup Data Input
                |
                v
         Prediction
                |
                v
       Success / Failure
```

---

## 6. Step 1 — Data Loading

The dataset is loaded into Python using Pandas.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("startup_success_dataset.csv")

df.head()
```

### Initial Data Understanding

```python
df.shape
df.info()
df.describe()
df.dtypes
df.isnull().sum()
```

These operations help identify:

- Dataset dimensions
- Column names
- Feature data types
- Missing values
- Statistical distributions
- Potential data quality issues

The initial dataset contains 5,000 rows and 24 columns.

---

## 7. Step 2 — Exploratory Data Analysis (EDA)

EDA was conducted to understand the data before building the machine learning models.

### Major EDA Activities

**1. Statistical Summary**

Explored the distributions of numerical features such as funding, founder experience, revenue growth, and monthly burn rate.

**2. Missing Value Analysis**

Identified columns containing missing observations.

**3. Target Distribution**

Analyzed the number of successful and failed startups.

**4. Correlation Analysis**

Examined relationships between numerical startup characteristics and the target variable.

**5. Outlier Visualization**

Used boxplots to inspect extreme values in financial and operational features.

**6. Feature Importance Analysis**

Used a Decision Tree classifier to explore which numerical features contributed most to classification.

---

## 8. Target Variable Distribution

The target classes are nearly balanced.

| Outcome | Records | Percentage |
|---|---:|---:|
| Failure (0) | 2,521 | 50.42% |
| Success (1) | 2,479 | 49.58% |
| Total | 5,000 | 100% |

### Observation

Because the outcome classes are approximately balanced, the project did not implement class resampling.

### Target Distribution Code

```python
print(df["success"].value_counts())

df["success"].value_counts().plot(
    kind="bar",
    title="Startup Success Distribution"
)

plt.xlabel("Startup Outcome")
plt.ylabel("Count")
plt.show()
```

---

## 9. Step 3 — Missing Value Analysis

Missing values were identified in four numerical columns.

| Column | Missing Values |
|---|---:|
| mom_revenue_growth_pct | 156 |
| monthly_active_users_k | 151 |
| num_patents_filed | 147 |
| nps_score | 142 |

### Handling Strategy

The project uses median imputation for numerical model features.

The `monthly_active_users_k` column was removed during feature engineering.

The remaining missing values were handled through the preprocessing pipeline.

### Why Median Imputation?

Median imputation provides a simple way to fill missing numeric values and is less affected by extreme values than mean imputation.

```python
SimpleImputer(strategy="median")
```

Imputation was fitted on training data to avoid introducing test-set information into the preprocessing statistics.

---

## 10. Step 4 — Data Cleaning

The data cleaning workflow includes:

- Duplicate detection
- Duplicate removal
- Missing value identification
- Data type inspection
- Outlier analysis

### Duplicate Check

```python
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
```

### Result

**Duplicate Records Found: 0**

The dataset retained all 5,000 records.

### Outlier Detection

Outliers were visually inspected in:

- Team size
- Monthly burn rate
- Total funding
- Monthly active users

```python
outlier_check_cols = [
    "team_size",
    "monthly_burn_rate_usd_k",
    "total_funding_usd_million",
    "monthly_active_users_k"
]

df[outlier_check_cols].boxplot()

plt.show()
```

The notebook visualizes outliers but does not implement outlier removal or capping.

---

## 11. Step 5 — Feature Engineering

Feature engineering was performed to reduce unnecessary input columns.

### Removed Features

```python
drop_cols = [
    "startup_id",
    "founded_year",
    "market_size_billion_usd",
    "has_female_founder",
    "product_launch_months_after_founding",
    "monthly_active_users_k",
    "num_founders"
]

df_fe = df.drop(columns=drop_cols)
```

### Reason for Removal

- `startup_id` acts as an identifier rather than a meaningful predictive variable.
- Other features were removed based on exploratory correlation analysis.

After removing these columns:

**16 input features remained, along with the target.**

Feature removal was exploratory; a stronger evaluation would validate these choices using training-only cross-validation.

---

## 12. Step 6 — Feature Importance Analysis

The project uses a Decision Tree classifier to explore numerical feature importance.

```python
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_rank, y_rank)

feature_scores = pd.Series(
    dt.feature_importances_,
    index=numeric_cols
).sort_values(ascending=False)
```

### Feature Importance Results

| Feature | Importance |
|---|---:|
| Total Funding | 0.2449 |
| Founder Experience | 0.2049 |
| Revenue Growth | 0.0852 |
| Active Competitors | 0.0850 |
| Monthly Burn Rate | 0.0825 |
| Customer Retention | 0.0762 |
| NPS Score | 0.0561 |
| Prior Startup Experience | 0.0544 |

### Interpretation

Total funding and founder experience received the highest importance scores in this exploratory Decision Tree.

These scores represent the behavior of that particular trained tree, not proof of causal influence.

**Implementation Note:** The exploratory Decision Tree was fitted before the train-test split. Its results should not be treated as leakage-free evidence for model selection. The final evaluation would be stronger if feature selection were performed entirely within training folds.

---

## 13. Step 7 — Data Transformation

The dataset contains both numerical and categorical features.

Different preprocessing methods were applied to each type.

### Numerical Features

There are 12 numerical input features.

Processing steps:

1. Median imputation
2. Standard scaling

```python
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
```

### Categorical Features

There are four categorical features:

- Sector
- Country
- City Tier
- Funding Stage

Processing steps:

1. Most-frequent value imputation
2. One-hot encoding

```python
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
```

### ColumnTransformer

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)
```

The `ColumnTransformer` combines numerical and categorical transformations into one preprocessing component.

### Benefits

- Consistent preprocessing
- Handling of missing values
- Encoding of categorical variables
- Reduced risk of preprocessing mistakes
- Reusable transformations during prediction

---

## 14. Step 8 — Train-Test Split

The processed feature table is divided into training and testing datasets.

```python
from sklearn.model_selection import train_test_split

X = df_fe.drop(columns=["success"])
y = df_fe["success"]

xtrain, xtest, ytrain, ytest = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Dataset Split

| Dataset | Records | Percentage |
|---|---:|---:|
| Training | 4,000 | 80% |
| Testing | 1,000 | 20% |

### Why Use a Test Set?

The training data is used to fit the machine learning model.

The test data is used to estimate performance on records not used to fit the model.

The notebook uses a fixed random state of 42 to make the split reproducible.

The split does not explicitly use stratification.

---

## 15. Step 9 — Model Training

Four machine learning classifiers were trained and evaluated.

### Models Used

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier
4. Support Vector Machine (SVM)

### Model Training Code

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)
from sklearn.svm import SVC

candidates = {
    "Logistic Regression": LogisticRegression(),

    "Random Forest": RandomForestClassifier(
        random_state=42
    ),

    "Gradient Boosting": GradientBoostingClassifier(
        random_state=42
    ),

    "Support Vector Machine": SVC()
}

for name, model in candidates.items():
    model.fit(X_train_transformed, ytrain)

    print(name)
    print("Training Accuracy:", model.score(
        X_train_transformed, ytrain
    ))
    print("Testing Accuracy:", model.score(
        X_test_transformed, ytest
    ))
```

All four models were compared on the same train-test split.

---

## 16. Model Comparison Results

The notebook recorded the following results:

| Algorithm | Train Accuracy | Test Accuracy |
|---|---:|---:|
| Logistic Regression | 80.58% | **83.40%** |
| Random Forest | 100.00% | 80.20% |
| Gradient Boosting | 85.18% | 81.70% |
| Support Vector Machine | 85.65% | 80.50% |

### Observations

**Logistic Regression**

Achieved the highest test accuracy among the four compared models.

**Random Forest**

Achieved perfect training accuracy but lower test accuracy, suggesting overfitting.

**Gradient Boosting**

Achieved 81.7% test accuracy and was selected for the final pipeline.

**Support Vector Machine**

Achieved 80.5% test accuracy.

### Final Model Selection

The implementation uses:

```python
GradientBoostingClassifier(random_state=42)
```

Although the notebook calls it the selected model, it is not the best-performing model by recorded test accuracy.

The notebook does not contain a completed hyperparameter tuning search for this classifier.

---

## 17. Step 10 — Final Model Evaluation

The selected Gradient Boosting classifier was evaluated using the test dataset.

### Final Test Accuracy

**81.7%**

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| Failure (0) | 0.82 | 0.83 | 0.82 | 517 |
| Success (1) | 0.81 | 0.81 | 0.81 | 483 |
| Macro Average | 0.82 | 0.82 | 0.82 | 1,000 |
| Weighted Average | 0.82 | 0.82 | 0.82 | 1,000 |

These values are rounded as displayed in the notebook's classification report.

### Performance Metrics

**Accuracy**

Measures the percentage of correctly classified records.

**Precision**

Measures how often predictions of a particular class are correct.

**Recall**

Measures how many actual examples of a class were identified.

**F1-Score**

Combines precision and recall into one metric.

### Evaluation Code

```python
from sklearn.metrics import (
    accuracy_score,
    classification_report
)

y_pred = best_model.predict(X_test_transformed)

print("Test Accuracy:", accuracy_score(ytest, y_pred))

print(classification_report(ytest, y_pred))
```

### Result Interpretation

The final pipeline recorded an accuracy score of:

```text
0.8170
```

This corresponds to 81.7% test accuracy.

The notebook's closing markdown mentions 85%+, but the actual saved pipeline evaluation shows 81.7%. The measured result is used throughout this README.

---

## 18. Step 11 — Machine Learning Pipeline

The final model combines preprocessing and classification in a single Scikit-learn Pipeline.

### Pipeline Architecture

```text
Raw Startup Data
       |
       v
ColumnTransformer
       |
       +-------------------+
       |                   |
       v                   v
Numerical Pipeline    Categorical Pipeline
       |                   |
       v                   v
Median Imputer         Mode Imputer
       |                   |
       v                   v
StandardScaler         OneHotEncoder
       |                   |
       +---------+---------+
                 |
                 v
      Gradient Boosting Classifier
                 |
                 v
           Binary Prediction
                 |
                 v
         Success / Failure
```

### Pipeline Code

```python
from sklearn.pipeline import Pipeline

final_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", best_model)
])

final_pipeline.fit(xtrain, ytrain)
```

### Pipeline Evaluation

```python
pipeline_test_acc = accuracy_score(
    ytest,
    final_pipeline.predict(xtest)
)

print(pipeline_test_acc)
```

Recorded output:

```text
0.8170
```

### Why Use a Pipeline?

A pipeline ensures that the same preprocessing steps used during training are applied during prediction.

This makes application integration simpler because raw startup data can be passed directly to the trained pipeline.

---

## 19. Step 12 — Model Serialization

The final pipeline is saved using Python's Pickle module.

```python
import pickle

pickle.dump(
    final_pipeline,
    open("model.pkl", "wb")
)
```

### Saved Model

`model.pkl`

This file contains the fitted preprocessing pipeline and Gradient Boosting classifier.

### Loading the Model

```python
import pickle

model = pickle.load(open("model.pkl", "rb"))
```

**Security Note:** Pickle files should only be loaded from trusted sources because loading a malicious Pickle file can execute arbitrary code.

---

## 20. Step 13 — Streamlit Application Development

The machine learning model is integrated into a Streamlit web application.

**Application File:** `app (1).py`

The interface allows users to enter startup information and generate predictions.

### Application Inputs

The interface accepts 16 features:

| Input | Type |
|---|---|
| Sector | Dropdown |
| Country | Dropdown |
| City Tier | Dropdown |
| Funding Stage | Dropdown |
| Founder Experience | Slider |
| Prior Startup Experience | Checkbox |
| Technical Cofounder | Checkbox |
| Team Size | Slider |
| Total Funding | Number Input |
| Funding Rounds | Slider |
| Monthly Burn Rate | Number Input |
| Active Competitors | Slider |
| Monthly Revenue Growth | Number Input |
| Customer Retention | Slider |
| NPS Score | Slider |
| Patents Filed | Slider |

### Example Input

A user can specify:

```text
Sector: AI/ML
Country: India
City Tier: Tier-1 Hub
Funding Stage: Series A

Founder Experience: 8 Years
Previous Startup Experience: Yes
Technical Cofounder: Yes

Team Size: 20
Total Funding: $3 Million
Funding Rounds: 2

Monthly Burn Rate: $100K
Active Competitors: 5
Revenue Growth: 12%
Customer Retention: 80%
NPS Score: 45
Patents Filed: 1
```

These values demonstrate the application input format; they are not a validated successful-startup example.

---

## 21. Step 14 — Prediction Workflow

When the user clicks **Predict**, the application performs the following steps:

1. Collect startup information.
2. Convert input values into a Pandas DataFrame.
3. Pass the DataFrame to the saved pipeline.
4. Apply preprocessing automatically.
5. Run the Gradient Boosting classifier.
6. Generate a binary prediction.
7. Display the predicted result.

### Application Code

```python
prediction = model.predict(input_df)

if prediction == 1:
    st.success("Your startup will be successful! 🎉")
    st.balloons()
else:
    st.error("Your startup is likely to fail")
```

### Prediction Meaning

```text
Prediction = 1
    |
    v
Predicted Startup Success
```

```text
Prediction = 0
    |
    v
Predicted Startup Failure
```

The interface currently displays a class prediction rather than a calibrated probability or an explanation of the prediction.

---

## 22. Complete Application Workflow

```text
User Opens Web Application
            |
            v
Startup Success Predictor
            |
            v
Enter Startup Information
            |
            v
Select Industry and Location
            |
            v
Enter Founder Details
            |
            v
Enter Funding Information
            |
            v
Enter Revenue and Customer Metrics
            |
            v
Click Predict
            |
            v
Create Pandas DataFrame
            |
            v
Load Saved ML Pipeline
            |
            v
Apply Data Preprocessing
            |
            v
Gradient Boosting Prediction
            |
            v
   +--------+--------+
   |                 |
   v                 v
Success (1)       Failure (0)
   |                 |
   v                 v
Success Message   Failure Message
```

---

## 23. Project Structure

The following is a suggested organized repository structure.

```text
Startup-Success-Prediction/
│
├── app.py
│
├── model.pkl
│
├── banner.png
│
├── startup_success_dataset.csv
│
├── Startup_Success_Model_Building.ipynb
│
├── test.ipynb
│
├── requirements.txt
│
└── README.md
```

### File Descriptions

**app.py**

Streamlit user interface and prediction logic.

Rename the supplied `app (1).py` to `app.py` if using the commands below.

**model.pkl**

Serialized machine learning pipeline.

Generate this file by running the model-building notebook.

**banner.png**

Application banner image referenced by the Streamlit app.

If this image is unavailable, remove or replace the `st.image("banner.png")` line.

**startup_success_dataset.csv**

Dataset containing 5,000 startup records.

**Startup_Success_Model_Building.ipynb**

Contains data analysis, preprocessing, model training, evaluation, and model saving.

**test.ipynb**

Contains an example of loading the saved model and predicting from a sample CSV.

This notebook expects an additional `sample.csv` file.

**requirements.txt**

Python dependency list. Create it using the dependencies listed in the installation section.

**README.md**

Project documentation.

### Uploaded File Status

The uploaded project materials include the dataset, application source, and two notebooks.

The application also expects `model.pkl` and `banner.png`, which were not included in those uploads.

---

## 24. Installation and Setup

### Prerequisites

- Python
- pip
- Jupyter Notebook
- Streamlit

### Step 1 — Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2 — Open the Project Directory

```bash
cd Startup-Success-Prediction
```

### Step 3 — Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4 — Activate the Environment

Windows:

```powershell
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

### Step 5 — Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit jupyter
```

Alternatively, create a `requirements.txt` file containing:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
jupyter
```

Then run:

```bash
pip install -r requirements.txt
```

For reproducible deployment, pin tested library versions after validating the application in your environment.

---

## 25. Train and Save the Model

Before running the application, generate the serialized model file.

### Step 1

Launch Jupyter Notebook:

```bash
jupyter notebook
```

### Step 2

Open:

`Startup_Success_Model_Building.ipynb`

### Step 3

Run the training notebook using the included dataset.

### Step 4

Execute the model-saving code.

```python
import pickle

with open("model.pkl", "wb") as file:
    pickle.dump(final_pipeline, file)
```

### Step 5

Verify that `model.pkl` exists in the directory used by the application.

The notebook's recorded pipeline evaluation is 81.7% test accuracy. Results from new training runs should be checked rather than assumed to match.

---

## 26. Run the Streamlit Application

Make sure the following files exist in the working directory:

```text
app.py
model.pkl
banner.png
```

If `banner.png` is not available, remove the image reference from the code.

### Start the Application

```bash
streamlit run app.py
```

Streamlit normally opens the application at:

```text
http://localhost:8501
```

Use the address displayed in your terminal.

### Using the Application

1. Select the startup's sector.
2. Select its country and city tier.
3. Enter founder and team details.
4. Enter funding information.
5. Enter revenue and retention metrics.
6. Click **Predict**.
7. View the predicted startup outcome.

---

## 27. Testing the Saved Model

The project contains a separate testing notebook named `test.ipynb`.

Its workflow is:

```text
Load model.pkl
       |
       v
Read sample.csv
       |
       v
Create Test DataFrame
       |
       v
Run model.predict()
       |
       v
Display Prediction
```

Example:

```python
import pandas as pd
import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

test = pd.read_csv("sample.csv")

prediction = model.predict(test)

print(prediction)
```

The recorded test notebook includes a sample that produces:

```text
array([1])
```

This shows the saved pipeline's prediction interface being used for a sample record.

It does not independently establish model accuracy.

---

## 28. Key Findings

### 1. Founder Experience

Founder experience showed a positive correlation with the success label in the supplied dataset.

### 2. Funding

Total funding and funding rounds were among the features showing stronger associations with startup outcomes.

### 3. Competition

The number of active competitors showed a negative correlation with success.

### 4. Model Performance

Logistic Regression achieved the highest test accuracy during the recorded four-model comparison.

### 5. Deployment

The Gradient Boosting pipeline was serialized and integrated into the Streamlit application code.

These findings describe associations in the supplied dataset, not proven causal relationships across real-world startups.

---

## 29. Project Limitations

### Model Accuracy

The selected final model achieved 81.7% test accuracy.

Other models may perform differently with additional evaluation and tuning.

### Model Selection

Logistic Regression achieved 83.4% test accuracy, outperforming the selected Gradient Boosting model.

Further comparison is needed before claiming Gradient Boosting is the optimal choice.

### Dataset Provenance

The source and sampling methodology of the supplied dataset have not been independently established.

Therefore, the model's real-world generalization is unknown.

### Feature Availability

Some model inputs, such as funding rounds, revenue growth, and customer retention, may only be available after a startup has begun operating.

The application should not be interpreted as predicting success at the idea stage without these data.

### Evaluation Limitations

The notebook uses a single 80:20 split for reported model comparison.

It does not include a completed cross-validation or hyperparameter optimization workflow.

Feature exploration was partially performed before the split, which may introduce selection bias.

### Binary Predictions

The current application displays only success or failure.

It does not provide probability calibration, prediction explanations, or uncertainty intervals.

### Deployment Readiness

The app requires its saved model and banner asset to run as written.

Additional input validation, dependency pinning, security testing, and monitoring would be needed for production use.

---

## 30. Future Improvements

Potential enhancements include:

- Use stratified train-test splitting.
- Perform cross-validation for more reliable model comparison.
- Tune Gradient Boosting using GridSearchCV or RandomizedSearchCV.
- Compare Gradient Boosting with XGBoost.
- Improve feature selection using training-only evaluation.
- Add ROC-AUC and confusion matrix analysis.
- Calibrate model probabilities.
- Display success probability alongside predictions.
- Add feature explanations using SHAP.
- Add input validation.
- Create automated tests for preprocessing and prediction.
- Pin tested dependency versions.
- Add error handling for missing model artifacts.
- Build a reproducible model training pipeline.
- Deploy the application using Streamlit Community Cloud or a supported hosting platform.

These features are suggested improvements and are not claimed as already implemented.

---

## 31. Skills Demonstrated

This project demonstrates practical knowledge of:

- Python Programming
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Data Preprocessing
- Classification Algorithms
- Model Comparison
- Train-Test Splitting
- Missing Value Imputation
- Feature Scaling
- One-Hot Encoding
- Model Evaluation
- Scikit-learn Pipelines
- Model Serialization
- Streamlit Development
- Machine Learning Application Integration

---

## 32. Resume-Ready Project Description

### Startup Success Prediction — Machine Learning

**Tech Stack:** Python, Scikit-learn, Gradient Boosting, Pandas, NumPy, Streamlit

- Developed a machine learning classification pipeline using 5,000 startup records, achieving **81.7% test accuracy** with Gradient Boosting.
- Built a Streamlit web application to predict startup success or failure using founder experience, funding, revenue growth, and customer retention metrics.

---

## 33. Conclusion

Startup Success Prediction is an end-to-end machine learning project focused on classifying startup outcomes using business and financial indicators.

The project covers:

- Dataset Understanding
- Exploratory Data Analysis
- Data Cleaning
- Feature Engineering
- Numerical and Categorical Preprocessing
- Machine Learning Model Comparison
- Classification Evaluation
- Pipeline Development
- Model Serialization
- Streamlit Application Integration

The selected Gradient Boosting pipeline achieved **81.7% test accuracy on 1,000 test records**.

The model comparison also identified Logistic Regression as a stronger performer on the same test split, with 83.4% accuracy.

The project serves as a demonstration of machine learning development and deployment workflows rather than a validated financial decision-making tool.

---

## Author

**Mahima Adhale**

Computer Science and Engineering Graduate

**Areas of Interest:**
Data Science, Machine Learning, Deep Learning, Generative AI, and Predictive Analytics.
