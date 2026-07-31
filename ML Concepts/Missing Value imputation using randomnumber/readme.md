# Missing Value Imputation using Random Number Imputation

## Overview

Missing values are one of the most common problems in real-world datasets. Before building any machine learning model, it is important to handle these missing values correctly to avoid inaccurate predictions.

In this project, I demonstrate **Random Number Imputation**, a technique where missing values are replaced with randomly selected values from the existing observations of the same feature. Unlike Mean or Median Imputation, this approach helps preserve the original distribution and variance of the data.

This notebook explains the complete process with code, visualizations, and statistical comparisons.

---

## Objectives

- Understand why missing values should be handled.
- Learn how Random Number Imputation works.
- Implement the technique using Python.
- Compare the data before and after imputation.
- Analyze how the distribution and variance change after imputation.

---

## Dataset

This project uses the **Titanic Dataset** (`train.csv`).

The **Age** column contains missing values, making it a good example for demonstrating Random Number Imputation.

---

## Project Workflow

The notebook follows these steps:

1. Import required libraries
2. Load the dataset
3. Explore missing values
4. Calculate missing value percentage
5. Visualize the original distribution
6. Create a Random Number Imputation function
7. Fill missing values
8. Compare distributions before and after imputation
9. Compare descriptive statistics
10. Compare variance
11. Draw conclusions

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Key Learning

After completing this project, I learned that:

- Random Number Imputation preserves the original data distribution better than Mean Imputation.
- It helps maintain the variance of the feature.
- Setting a `random_state` makes the results reproducible.
- This technique is useful when missing values are assumed to be Missing Completely At Random (MCAR).

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/Missing-Value-Imputation-Random-Number.git
```

### Move into the project folder

```bash
cd Missing-Value-Imputation-Random-Number
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the notebook and run all cells.

---

## Project Structure

```
Missing-Value-Imputation-Random-Number/
│
├── Missing_Value_Imputation_Random_Number.ipynb
├── train.csv
├── requirements.txt
└── README.md
```

---

## Future Improvements

Some additional imputation techniques that can be explored include:

- Mean Imputation
- Median Imputation
- Mode Imputation
- End of Distribution Imputation
- KNN Imputation
- Iterative (MICE) Imputation
- Multiple Imputation
- Missing Indicator Technique

---

## References

- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Feature Engineering for Machine Learning by Alice Zheng

---

## Author

**Rohit Joshi**

If you found this project helpful or learned something new, feel free to ⭐ the repository.