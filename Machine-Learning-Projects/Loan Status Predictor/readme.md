# 💰 Loan Status Prediction using Support Vector Classifier (SVC)

A Machine Learning project that predicts whether a loan application will be **Approved** or **Rejected** using the **Support Vector Classifier (SVC)** algorithm. The model analyzes applicant information such as income, education, credit history, loan amount, and property area to make predictions.

---

## 📌 Project Overview

Loan approval is one of the most important tasks for financial institutions. This project builds a classification model using **Support Vector Machine (SVM)** with the **Support Vector Classifier (SVC)** to predict loan approval status based on historical loan application data.

---

## 🎯 Objective

- Predict loan approval status accurately.
- Automate the loan verification process.
- Build a Machine Learning classification model using **SVC**.
- Evaluate model performance using standard metrics.

---

## 📂 Dataset

The dataset contains applicant details used for predicting loan approval.

### Features

| Feature | Description |
|----------|-------------|
| Loan_ID | Unique Loan ID |
| Gender | Applicant Gender |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Education Level |
| Self_Employed | Self Employment Status |
| ApplicantIncome | Applicant Income |
| CoapplicantIncome | Co-applicant Income |
| LoanAmount | Requested Loan Amount |
| Loan_Amount_Term | Loan Duration |
| Credit_History | Credit History |
| Property_Area | Urban / Semiurban / Rural |
| Loan_Status | Target Variable (Approved / Rejected) |

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📊 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Cleaning
4. Handle Missing Values
5. Encode Categorical Features
6. Exploratory Data Analysis (EDA)
7. Feature Selection
8. Train-Test Split
9. Train Support Vector Classifier (SVC)
10. Evaluate Model
11. Predict Loan Status

---

## 🤖 Machine Learning Model

### Support Vector Classifier (SVC)

The project uses **Support Vector Classifier (SVC)** from Scikit-learn.

**Why SVC?**
- Effective for binary classification problems.
- Performs well in high-dimensional feature spaces.
- Creates an optimal decision boundary (hyperplane).
- Handles complex classification tasks using kernel functions.

---

## 📈 Model Evaluation

The model performance is evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report
- Precision
- Recall
- F1 Score

---


---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Loan-Status-Prediction.git
```

Go to the project directory

```bash
cd Loan-Status-Prediction
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook

```bash
jupyter notebook
```

---

## 🚀 How to Run

1. Open the notebook.
2. Run all cells sequentially.
3. Train the SVC model.
4. Test the model using sample input.
5. View prediction results and evaluation metrics.

---

## 📊 Sample Prediction

**Input**

```text
Applicant Income      : 5000
Coapplicant Income    : 1500
Loan Amount           : 120
Credit History        : 1
Education             : Graduate
Property Area         : Urban
```

**Prediction**

```text
Loan Status : Approved ✅
```

---

## 📚 Libraries Used

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

---

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Compare SVC with Logistic Regression and Random Forest
- Build a Streamlit web application
- Deploy the model on the cloud
- Improve feature engineering for higher accuracy

---

## 🎓 Learning Outcomes

- Data preprocessing
- Handling missing values
- Feature encoding
- Exploratory Data Analysis (EDA)
- Support Vector Machine (SVC)
- Model evaluation
- Machine Learning workflow

---

## 👨‍💻 Author

**Rohit Joshi**  
B.E. Artificial Intelligence & Data Science  
Passionate about Machine Learning, Data Science, and Artificial Intelligence.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!