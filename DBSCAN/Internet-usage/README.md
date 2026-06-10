# Internet Usage Segmentation using DBSCAN Clustering

## 📌 Project Overview

This project applies the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm to an Internet Usage dataset containing the percentage of individuals using the Internet across various countries from **2000 to 2023**.

The goal is to identify groups of countries with similar internet adoption patterns over time and detect any countries that exhibit unusual behavior (outliers/noise).

DBSCAN was chosen because it can discover clusters of arbitrary shapes and automatically identify noise points without requiring the number of clusters to be specified in advance.

---

## 🎯 Problem Statement

The objective of this project is to analyze internet usage data and identify distinct groups of countries based on their internet adoption trends from 2000–2023.

Using DBSCAN clustering, countries with similar growth patterns are grouped together, allowing for better understanding of global internet penetration trends and the identification of exceptional cases.

---

## 📂 Project Structure

```text
Internet-Usage-DBSCAN/
│
├── data/
│   └── internet_usage.csv
│
├── notebooks/
│   └── DBSCAN-internet-usage.ipynb
│
├── outputs/
│   ├── k_distance_plot.png
│   ├── cluster_results.csv
│   └── silhouette_score.txt
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset Description

The dataset contains information about the percentage of individuals using the Internet across different countries over multiple years.

### Dataset Characteristics

| Attribute | Description |
|------------|-------------|
| Rows | 217 Countries |
| Columns | 26 Variables |
| Time Period | 2000 – 2023 |
| Data Type | Numerical Time-Series Data |
| Target Variable | None (Unsupervised Learning) |

### Features

- Country Name
- Country Code
- Internet Usage (%) for each year:
  - 2000
  - 2001
  - 2002
  - ...
  - 2023

Each row represents a country and each yearly column represents the percentage of individuals using the internet in that year.

---

## 🏗 Workflow Architecture

```text
Import Libraries
       ↓
Load Dataset
       ↓
Data Understanding
       ↓
Data Quality Checks
       ↓
Missing Value Treatment
       ↓
Feature Selection
       ↓
Exploratory Data Analysis
       ↓
Feature Scaling
       ↓
DBSCAN Clustering
       ↓
Hyperparameter Tuning
       ↓
Model Evaluation
       ↓
Conclusion
```

---

## 🔍 Data Understanding

Initial analysis was performed to understand:

- Dataset dimensions
- Data types
- Statistical summary
- Missing values
- Duplicate records

Methods used:

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
```

---

## 🛠 Data Quality Checks

### Missing Value Handling

Invalid entries such as:

```python
'@'
'#'
''
' '
'?'
'/'
'empty'
'..'
0
```

were replaced with NaN values.

```python
df.replace(
    ['@','#','',' ','?','/','empty','..',0],
    np.nan,
    inplace=True
)
```

---

### Data Type Conversion

All yearly columns were converted into numeric format.

```python
for i in df.loc[:, '2000':]:
    df[i] = pd.to_numeric(df[i])
```

---

### Duplicate Check

```python
df.duplicated().sum()
```

---

### Missing Value Imputation

Mean imputation was used.

```python
from sklearn.impute import SimpleImputer

si = SimpleImputer(strategy='mean')

df.loc[:, '2000':'2022'] = si.fit_transform(
    df.loc[:, '2000':'2022']
)
```

---

### Feature Selection

The following columns were removed:

```python
Country Name
Country Code
2023
```

These columns were excluded because clustering requires only numerical features.

---

## 📈 Exploratory Data Analysis (EDA)

A boxplot was generated to identify:

- Distribution of values
- Outliers
- Data spread

```python
df.boxplot()
plt.show()
```

### Key Observations

- Internet usage increased significantly over the years.
- Several countries showed unusually high or low adoption rates.
- Variation exists among countries, making clustering appropriate.

---

## ⚖ Feature Scaling

DBSCAN relies on distance calculations.

Therefore, StandardScaler was applied.

### Standardization Formula

\[
z = \frac{x-\mu}{\sigma}
\]

Implementation:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)
```

---

## 🤖 DBSCAN Clustering

### Why DBSCAN?

Advantages:

- No need to specify the number of clusters.
- Detects noise automatically.
- Handles irregular cluster shapes.
- Suitable for anomaly detection.

---

## Hyperparameter Tuning

### Determining Epsilon (eps)

Nearest Neighbors method was used.

```python
from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(
    n_neighbors=3
)

neigh.fit(scaled_data)
```

### K-Distance Calculation

```python
dist, index = neigh.kneighbors(
    scaled_data
)

distance = np.sort(
    dist[:,2]
)
```

### K-Distance Graph

```python
plt.plot(distance)
plt.xlabel('Distance')
plt.ylabel('EPS')
plt.title('K Distance')
plt.show()
```

The elbow point on the graph suggested an epsilon value close to **2.5**.

---

## Final Model

```python
from sklearn.cluster import DBSCAN

db = DBSCAN(
    eps=2.5,
    min_samples=24
)

clusters = db.fit_predict(
    scaled_data
)
```

### Selected Parameters

| Parameter | Value |
|------------|--------|
| eps | 2.5 |
| min_samples | 24 |

---

## 📊 Model Evaluation

### Silhouette Score

The clustering quality was evaluated using the Silhouette Score.

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(
    scaled_data,
    clusters
)

print(score)
```

### Interpretation

| Score Range | Interpretation |
|-------------|---------------|
| > 0.70 | Excellent |
| 0.50 – 0.70 | Good |
| 0.25 – 0.50 | Reasonable |
| < 0.25 | Weak |

The obtained silhouette score indicates the effectiveness of DBSCAN in separating countries based on internet usage patterns.

---

## 📦 Libraries Used

```python
numpy
pandas
matplotlib
seaborn
scikit-learn
```

Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

---

## 📈 Results

DBSCAN successfully grouped countries with similar internet adoption trends from 2000–2022.

Key findings:

- Countries with similar internet growth rates were clustered together.
- Dense regions of countries sharing adoption characteristics were identified.
- Noise points highlighted countries with unique internet usage patterns.
- No predefined cluster count was required.
- Meaningful patterns were extracted from historical internet usage data.

---

## 🌍 Business Applications

- Digital Development Analysis
- Country Segmentation
- Technology Adoption Studies
- Market Expansion Planning
- Internet Infrastructure Assessment
- Policy Decision Support

---

## 🔮 Future Improvements

- Apply PCA before clustering.
- Compare with K-Means and Hierarchical Clustering.
- Automate epsilon selection.
- Analyze cluster characteristics in detail.
- Incorporate socioeconomic indicators.

---

## 🏆 Conclusion

The DBSCAN clustering algorithm was successfully applied to the Internet Usage dataset to segment countries based on their internet adoption behavior over time. After data preprocessing, feature scaling, and hyperparameter tuning, DBSCAN identified meaningful clusters and detected outlier countries. The analysis demonstrates the effectiveness of density-based clustering for discovering hidden structures in longitudinal internet usage data without requiring a predefined number of clusters.