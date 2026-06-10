# 🍷 Wine Segmentation using DBSCAN Clustering

## 📌 Project Overview

This project applies the **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** algorithm to the Wine dataset containing the chemical composition of different wine samples.

The goal is to identify natural groups of wines with similar chemical characteristics and detect any unusual wine samples (noise/outliers).

DBSCAN was selected because it can discover clusters of arbitrary shapes and automatically identify noise points without requiring the number of clusters to be specified beforehand.

---

## 🎯 Problem Statement

The objective of this project is to analyze wine characteristics and identify distinct groups of wines based on their chemical properties.

Using DBSCAN clustering, wine samples with similar compositions are grouped together, helping uncover hidden patterns within the dataset and detect anomalous observations.

---

## 📂 Project Structure

```text
Wine-DBSCAN/
│
├── data/
│   └── wine.csv
│
├── notebooks/
│   └── DBSCAN-wine.ipynb
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

The dataset contains chemical analysis results of wines grown in the same region but derived from different cultivars.

### Dataset Characteristics

| Attribute       | Description           |
| --------------- | --------------------- |
| Rows            | 178 Wine Samples      |
| Columns         | 13 Features           |
| Dataset Type    | Numerical Data        |
| Learning Type   | Unsupervised Learning |
| Target Variable | None                  |

### Features

* Alcohol
* Malic Acid
* Ash
* Alcalinity of Ash
* Magnesium
* Total Phenols
* Flavanoids
* Nonflavanoid Phenols
* Proanthocyanins
* Color Intensity
* Hue
* OD280/OD315 of Diluted Wines
* Proline

Each row represents a wine sample, while each column represents a specific chemical property.

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
Missing Value Check
       ↓
Duplicate Check
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

* Dataset dimensions
* Data types
* Statistical summary
* Missing values
* Duplicate records

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

### Missing Value Check

```python
df.isnull().sum()
```

No missing values were found in the dataset.

---

### Duplicate Check

```python
df.duplicated().sum()
```

Duplicate records were checked and handled if present.

---

## 📈 Exploratory Data Analysis (EDA)

A boxplot was generated to identify:

* Data distribution
* Outliers
* Feature spread

```python
df.boxplot(figsize=(12,6))
plt.show()
```

### Key Observations

* Features are measured on different scales.
* Several variables contain extreme values.
* Scaling is necessary before applying DBSCAN.
* Data exhibits varying distributions across features.

---

## ⚖ Feature Scaling

DBSCAN relies on distance calculations.

Therefore, StandardScaler was applied.

### Standardization Formula

z = (x − μ) / σ

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

* No need to specify the number of clusters.
* Detects noise automatically.
* Handles irregular cluster shapes.
* Effective for outlier detection.

---

## Hyperparameter Tuning

### Determining Epsilon (eps)

Nearest Neighbors method was used.

```python
from sklearn.neighbors import NearestNeighbors

neigh = NearestNeighbors(
    n_neighbors=5
)

neigh.fit(scaled_data)
```

### K-Distance Calculation

```python
distances, indices = neigh.kneighbors(
    scaled_data
)

distance = np.sort(
    distances[:,4]
)
```

### K-Distance Graph

```python
plt.plot(distance)
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.title('K-Distance Graph')
plt.show()
```

The elbow point on the graph was selected as the optimal epsilon value.

---

## Final Model

```python
from sklearn.cluster import DBSCAN

db = DBSCAN(
    eps=1.5,
    min_samples=5
)

clusters = db.fit_predict(
    scaled_data
)
```

### Selected Parameters

| Parameter   | Value |
| ----------- | ----- |
| eps         | 1.5   |
| min_samples | 5     |

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
| ----------- | -------------- |
| > 0.70      | Excellent      |
| 0.50 – 0.70 | Good           |
| 0.25 – 0.50 | Reasonable     |
| < 0.25      | Weak           |

### Obtained Result

**Silhouette Score = 0.6955**

The score indicates that the clusters are well-separated and compact, demonstrating good clustering performance using DBSCAN.

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

DBSCAN successfully grouped wine samples based on their chemical characteristics.

Key findings:

* Wines with similar chemical compositions were clustered together.
* Dense regions of similar wine samples were identified.
* Outlier wine samples were detected automatically.
* No predefined number of clusters was required.
* Meaningful hidden patterns were extracted from the dataset.

---

## 🌍 Business Applications

* Wine Quality Analysis
* Product Segmentation
* Food & Beverage Research
* Market Basket Analysis
* Quality Control Systems
* Anomaly Detection

---

## 🔮 Future Improvements

* Apply PCA before clustering.
* Compare DBSCAN with K-Means Clustering.
* Compare DBSCAN with Hierarchical Clustering.
* Perform automated hyperparameter tuning.
* Visualize clusters using 2D and 3D projections.

---

## 🏆 Conclusion

The DBSCAN clustering algorithm was successfully applied to the Wine dataset to segment wine samples based on their chemical properties. After data preprocessing, feature scaling, and hyperparameter tuning, DBSCAN identified meaningful clusters and automatically detected outlier wine samples.

The obtained Silhouette Score of **0.6955** indicates strong cluster separation and validates the effectiveness of density-based clustering for discovering hidden structures in wine data without requiring predefined class labels.

---

## 👨‍💻 Author

**Mahima Adhale**

Master's in Artificial Intelligence & Machine Learning

Skills:

* Machine Learning
* Data Science
* Python
* Deep Learning
* Data Analytics

⭐ If you found this project useful, don't forget to star the repository.
