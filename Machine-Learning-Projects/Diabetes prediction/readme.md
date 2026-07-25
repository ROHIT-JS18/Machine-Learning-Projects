# 🩺 Diabetes Prediction using Machine Learning

A Machine Learning project that predicts whether a person is diabetic or non-diabetic based on medical parameters using the **Support Vector Machine (SVM)** algorithm.

---

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help in timely diagnosis and treatment.

This project uses the **PIMA Indians Diabetes Dataset** and applies Machine Learning techniques to classify patients as diabetic or non-diabetic.

---

## 🚀 Features

- Data Collection and Analysis
- Data Preprocessing
- Feature Standardization
- Train-Test Split
- Support Vector Machine (SVM) Model
- Model Evaluation
- Predict Diabetes for New Patient Data

---

## 📂 Dataset

**Dataset:** PIMA Indians Diabetes Dataset

The dataset contains **768 records** and **8 input features**.

### Input Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target Variable

- **0 → Non-Diabetic**
- **1 → Diabetic**

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Jupyter Notebook

---

## 📚 Libraries Used

```python
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
```

---

## ⚙️ Project Workflow

```
Load Dataset
      │
      ▼
Data Analysis
      │
      ▼
Feature & Target Separation
      │
      ▼
Standardization
      │
      ▼
Train-Test Split
      │
      ▼
Train SVM Model
      │
      ▼
Evaluate Accuracy
      │
      ▼
Predict New Patient
```

---

## 🧠 Machine Learning Model

**Algorithm Used**

- Support Vector Machine (SVM)
- Kernel: Linear

---

## 📈 Model Performance

| Metric | Accuracy |
|---------|----------|
| Training Accuracy | **78.66%** |
| Testing Accuracy | **77.27%** |

---

## 📋 Sample Prediction

Input:

```python
(5,166,72,19,175,25.8,0.587,51)
```

Output:

```
The person is diabetic
```

---

## 📁 Project Structure

```
Diabetes-Prediction/
│
├── diabetes.csv
├── Diabetes Prediction.ipynb
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Diabetes-Prediction.git
```

### 2. Move into Project Folder

```bash
cd Diabetes-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Notebook

Open Jupyter Notebook and execute all cells.

---

## 📊 Future Improvements

- Hyperparameter Tuning
- Compare Multiple ML Algorithms
- Feature Engineering
- Web Application using Streamlit
- Model Deployment
- Cross Validation
- ROC Curve & Confusion Matrix

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Data preprocessing techniques
- Feature standardization
- Train-test splitting
- Supervised Machine Learning
- Support Vector Machine (SVM)
- Model evaluation using accuracy score
- Building a predictive system

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Rohit Sachidanand Joshi**

Artificial Intelligence & Data Science Student

---
⭐ If you found this project useful, don't forget to star the repository!