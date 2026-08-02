# 💳 Credit Card Fraud Detection using Machine Learning

## 📌 Project Overview

Credit card fraud is one of the biggest challenges in the financial industry. This project builds a **Machine Learning classification model** to identify whether a credit card transaction is **Fraudulent** or **Legitimate**.

Since the dataset is highly imbalanced, **under-sampling** is used to create a balanced training dataset before building the model.

---

## 🚀 Features

* Data preprocessing and exploration
* Handling highly imbalanced data
* Under-sampling technique
* Train-Test Split
* Logistic Regression model
* Fraud prediction
* 

---

## 📂 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── Credit Card Fraud Detection project.ipynb
├── credit_data.csv
├── README.md

```

---

## 📊 Dataset

The dataset contains credit card transactions with the following information:

* Time
* V1 to V28 (PCA transformed features)
* Amount
* Class

### Target Variable

| Class | Meaning                |
| ----- | ---------------------- |
| 0     | Legitimate Transaction |
| 1     | Fraudulent Transaction |

> **Note:** The dataset is highly imbalanced because fraudulent transactions are much fewer than legitimate transactions.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Jupyter Notebook

---

## ⚙️ Machine Learning Workflow

1. Import required libraries
2. Load the dataset
3. Explore the dataset
4. Check missing values
5. Analyze class distribution
6. Apply under-sampling
7. Split the dataset into training and testing sets
8. Train a Logistic Regression model
9. Predict transaction classes
10. Evaluate model performance using accuracy score

---

## 🤖 Machine Learning Model

**Algorithm Used**

* Logistic Regression

The model learns patterns from historical transactions and predicts whether a new transaction is fraudulent.

---

## 📈 Evaluation Metric

The notebook evaluates the model using:

* Accuracy Score

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/Rohit-JS18/Credit-Card-Fraud-Detection.git
```

Move into the project folder:

```bash
cd Credit-Card-Fraud-Detection
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```
Credit Card Fraud Detection project.ipynb
```

Run all cells sequentially.

---

## 📋 Requirements

```
numpy
pandas
scikit-learn
jupyter
```

You can generate the requirements file using:

```bash
pip freeze > requirements.txt
```

---

## 📷 Project Workflow

```
Dataset
    │
    ▼
Data Loading
    │
    ▼
Data Exploration
    │
    ▼
Class Distribution
    │
    ▼
Under Sampling
    │
    ▼
Train-Test Split
    │
    ▼
Logistic Regression
    │
    ▼
Prediction
    │
    ▼
Accuracy Evaluation
```

---

## 🎯 Future Improvements

* Use SMOTE instead of under-sampling
* Try Random Forest and XGBoost
* Hyperparameter tuning
* Cross-validation
* Precision, Recall, F1-Score, and ROC-AUC evaluation
* Deploy the model using Streamlit or Flask

---

## 👨‍💻 Author

**Rohit Joshi**

---

## ⭐ If you found this project helpful

Give this repository a **⭐ Star** on GitHub!
