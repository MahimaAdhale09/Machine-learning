# DBSCAN Clustering Project

## 📌 Project Overview

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised machine learning algorithm used for clustering data points based on density. Unlike K-Means, DBSCAN does not require specifying the number of clusters beforehand and can identify clusters of arbitrary shapes while detecting noise (outliers).

This project applies DBSCAN clustering to discover hidden patterns, group similar observations, and identify anomalies within the dataset.

---

## 🎯 Objectives

- Understand the structure of the dataset.
- Perform data cleaning and preprocessing.
- Scale numerical features.
- Apply DBSCAN clustering.
- Identify dense regions in the data.
- Detect outliers and noise points.
- Evaluate clustering performance.
- Visualize clusters and insights.

---

## 📂 Project Structure

DBSCAN-Clustering-Project/

├── data/

│ ├── raw_data.csv

│ └── processed_data.csv

│

├── notebooks/

│ └── DBSCAN_Clustering.ipynb

│

├── outputs/

│ ├── cluster_visualization.png

│ ├── silhouette_score.txt

│ └── clustered_data.csv

│

├── README.md

├── requirements.txt

└── .gitignore

---

## 📊 Dataset Description

The dataset contains observations collected from a specific domain such as customer behavior, internet usage, healthcare, retail, finance, or marketing.

### Dataset Components

| Feature Type | Description |
|-------------|-------------|
| Numerical Features | Continuous numeric variables |
| Categorical Features | Category labels |
| Target Variable | Not required in clustering |
| Observations | Individual records used for grouping |

---

## 🔍 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is performed to understand data distribution and identify potential issues.

### Steps Performed

- Dataset Shape Analysis
- Data Type Inspection
- Missing Value Analysis
- Duplicate Record Detection
- Statistical Summary
- Outlier Detection
- Distribution Analysis
- Correlation Analysis

### Visualizations

- Histogram
- Box Plot
- Scatter Plot
- Heatmap
- Pair Plot

---

## 🛠 Data Preprocessing

Proper preprocessing improves clustering performance.

### Missing Value Handling

- Mean Imputation
- Median Imputation
- Mode Imputation

### Duplicate Removal

Duplicate records are removed to prevent biased clustering.

### Outlier Handling

Since DBSCAN naturally identifies outliers as noise points, extreme values are generally retained.

### Feature Scaling

DBSCAN is distance-based and requires scaling.

#### Standardization

Formula:

z = (x − μ) / σ

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### Normalization

Formula:

x' = (x − xmin) / (xmax − xmin)

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🤖 DBSCAN Algorithm

DBSCAN groups points based on density.

### Key Parameters

#### eps (Epsilon)

Maximum distance between two points for them to be considered neighbors.

#### min_samples

Minimum number of points required to form a dense region.

---

## How DBSCAN Works

1. Select a point.
2. Find neighboring points within eps distance.
3. If neighbors ≥ min_samples, create a cluster.
4. Expand the cluster recursively.
5. Mark isolated points as noise.
6. Repeat until all points are processed.

---

## Types of Points in DBSCAN

### Core Point

A point having at least min_samples neighbors within eps.

### Border Point

A point connected to a core point but having fewer than min_samples neighbors.

### Noise Point

An outlier that does not belong to any cluster.

---

## Implementation

### Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
```

### Feature Scaling

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Train DBSCAN Model

```python
dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)

clusters = dbscan.fit_predict(X_scaled)
```

### Cluster Labels

```python
print(clusters)
```

---

## Cluster Visualization

```python
plt.scatter(
    X_scaled[:,0],
    X_scaled[:,1],
    c=clusters
)

plt.title("DBSCAN Clustering")
plt.show()
```

---

## Model Evaluation

### Silhouette Score

Measures how well-separated clusters are.

Range:

-1 to +1

Interpretation:

| Silhouette Score | Interpretation |
|-----------------|---------------|
| > 0.70 | Excellent Clustering |
| 0.50 - 0.70 | Good Clustering |
| 0.25 - 0.50 | Reasonable Clustering |
| < 0.25 | Weak Clustering |

Example:

```python
score = silhouette_score(
    X_scaled,
    clusters
)

print(score)
```

---

## Advantages of DBSCAN

- No need to specify the number of clusters.
- Detects outliers automatically.
- Works with arbitrarily shaped clusters.
- Robust to noise.
- Suitable for anomaly detection.

---

## Limitations of DBSCAN

- Sensitive to eps value.
- Performance decreases in high-dimensional data.
- Struggles when clusters have varying densities.
- Computationally expensive for large datasets.

---

## Applications of DBSCAN

- Customer Segmentation
- Fraud Detection
- Anomaly Detection
- Image Processing
- Geographic Data Analysis
- Social Network Analysis
- Market Basket Analysis
- Internet Usage Pattern Discovery

---

## 📦 Requirements

```txt
numpy
pandas
matplotlib
seaborn
scikit-learn
scipy
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📈 Results

The DBSCAN algorithm successfully grouped data points based on density and identified noise points that did not belong to any cluster. The clustering process revealed hidden structures within the dataset and highlighted potential outliers.

Key Findings:

- Dense regions were identified as clusters.
- Noise points were automatically detected.
- No predefined cluster count was required.
- Meaningful patterns were extracted from the dataset.

---

## 🔮 Future Improvements

- Hyperparameter Optimization
- Automated Epsilon Selection
- Dimensionality Reduction using PCA
- Large-Scale Clustering Optimization
- Advanced Cluster Validation Techniques

---

## 🏆 Conclusion

This project demonstrates the implementation of the DBSCAN clustering algorithm for unsupervised learning. By clustering data based on density rather than distance from centroids, DBSCAN effectively discovers meaningful patterns and identifies anomalies. It is particularly useful when the number of clusters is unknown and when datasets contain noise or irregularly shaped clusters.