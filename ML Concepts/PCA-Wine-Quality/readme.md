# Principal Component Analysis (PCA) From Scratch using NumPy

A complete implementation of **Principal Component Analysis (PCA)** from scratch using **NumPy** on the **Wine Quality Dataset**. This project demonstrates the mathematical foundation of PCA without using `sklearn.PCA()` and compares Machine Learning model performance before and after dimensionality reduction.

---

## Project Overview

Principal Component Analysis (PCA) is one of the most widely used dimensionality reduction techniques in Machine Learning and Data Science.

In this project, PCA is implemented manually by calculating:

- Mean
- Mean Centering
- Covariance Matrix
- Eigenvalues
- Eigenvectors
- Principal Components
- Data Projection

After implementing PCA, Logistic Regression is trained on:

- Original Dataset
- PCA Reduced Dataset

Finally, the results are compared based on:

- Accuracy
- Training Time
- Number of Features

---

## Dataset

**Dataset:** Wine Quality Dataset

Source:
https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

Dataset Information

- Samples : 1599
- Features : 11
- Target : Quality

---

## Technologies Used

- Python
- NumPy
- Pandas
- Plotly
- Scikit-learn
- Jupyter Notebook

---

## Project Workflow

```text
Load Dataset
      │
      ▼
Data Exploration
      │
      ▼
Standardization
      │
      ▼
Mean Calculation
      │
      ▼
Mean Centering
      │
      ▼
Covariance Matrix
      │
      ▼
Eigenvalues
      │
      ▼
Eigenvectors
      │
      ▼
Select Principal Components
      │
      ▼
Data Projection
      │
      ▼
2D & 3D Plotly Visualization
      │
      ▼
Logistic Regression
(Original Dataset)
      │
      ▼
Logistic Regression
(PCA Dataset)
      │
      ▼
Performance Comparison
```

---

## Mathematical Concepts Covered

This project covers the following mathematical concepts:

- Mean
- Mean Centering
- Variance
- Covariance
- Covariance Matrix
- Eigenvalues
- Eigenvectors
- Explained Variance
- Data Projection
- Dimensionality Reduction

---

## Features

- Manual PCA implementation using NumPy
- No use of `sklearn.PCA()` during implementation
- Covariance Matrix calculation
- Eigenvalue & Eigenvector computation
- Principal Component selection
- Data projection
- Interactive Plotly 2D visualization
- Interactive Plotly 3D visualization
- Logistic Regression before PCA
- Logistic Regression after PCA
- Performance comparison

---

## Project Structure

```text
PCA-From-Scratch/

│── data/
│     └── winequality-red.csv

│── PCA_From_Scratch.ipynb

│── README.md

│── requirements.txt

│── images/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/PCA-From-Scratch.git
```

Move into the project directory

```bash
cd PCA-From-Scratch
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## Results

The PCA implementation successfully:

- Reduced the dimensionality of the dataset
- Preserved most of the important information
- Reduced computational complexity
- Improved training efficiency
- Made visualization easier using two and three principal components

---

## Learning Outcomes

After completing this project, you will understand:

- Why PCA is required
- How covariance matrix is calculated
- Why mean centering is necessary
- How eigenvalues are computed
- How eigenvectors define principal directions
- How PCA reduces dimensionality
- Why PCA speeds up machine learning models
- When PCA should and should not be used

---

## Future Improvements

- Scree Plot
- Explained Variance Plot
- PCA using Scikit-learn for comparison
- Comparison with t-SNE
- Comparison with UMAP
- More Machine Learning algorithms
- Hyperparameter tuning

---

## Author

**Rohit Sachidanand Joshi**

Bachelor of Engineering (Artificial Intelligence & Data Science)

Interested in Machine Learning, Data Science, Artificial Intelligence, and Python Development.

---

## License

This project is licensed under the MIT License.

---

## If you found this project useful

⭐ Star this repository

🍴 Fork this repository

📢 Share it with others

Happy Learning!