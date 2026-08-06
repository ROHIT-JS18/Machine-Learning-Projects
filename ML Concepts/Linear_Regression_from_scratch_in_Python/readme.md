# 📈 Linear Regression from Scratch in Python

A complete implementation of **Linear Regression from scratch using NumPy**, without using Scikit-learn's `LinearRegression` model. This project demonstrates how the Gradient Descent optimization algorithm works internally to train a linear regression model.

---

## 📌 Project Overview

This notebook covers the complete workflow of building a Linear Regression model from scratch, including:

- Understanding the Linear Regression equation
- Understanding Gradient Descent
- Creating a custom `Linear_Regression` class
- Training the model using Gradient Descent
- Predicting outputs
- Testing the implementation on a real dataset
- Visualizing the regression line

---

## 🚀 Features

- ✅ Pure Python + NumPy implementation
- ✅ No use of Scikit-learn's Linear Regression algorithm
- ✅ Gradient Descent optimization
- ✅ Custom prediction function
- ✅ Train-Test Split
- ✅ Data preprocessing
- ✅ Regression visualization using Matplotlib

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Scikit-learn (only for dataset splitting and evaluation)

---

## 📚 Concepts Covered

- Linear Regression
- Machine Learning Basics
- Cost Function
- Gradient Descent
- Weight & Bias Update
- Model Training
- Prediction
- Data Preprocessing

---

## 📂 Project Structure

```
Linear_Regression_from_scratch_in_Python.ipynb
README.md
```

---

## 🧮 Linear Regression Formula

\[
Y = wX + b
\]

Where:

- **Y** → Dependent Variable
- **X** → Independent Variable
- **w** → Weight (Slope)
- **b** → Bias (Intercept)

---

## 📉 Gradient Descent Update Rule

The parameters are updated using:

```
w = w - α × dw
b = b - α × db
```

Where:

- **α** = Learning Rate
- **dw** = Gradient of weight
- **db** = Gradient of bias

Gradient Descent minimizes the loss function by updating the parameters iteratively.

---

## 🧠 Custom Linear Regression Class

The notebook implements a custom class that includes:

- Initialization
- Model Training (`fit`)
- Gradient Calculation
- Parameter Updates
- Prediction (`predict`)

No built-in Linear Regression algorithm is used.

---

## 📊 Workflow

1. Import Libraries
2. Load Dataset
3. Data Preprocessing
4. Split Training & Testing Data
5. Initialize Linear Regression Model
6. Train using Gradient Descent
7. Predict Values
8. Visualize Results

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Linear-Regression-from-Scratch.git
```

### Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

### Launch Notebook

```bash
jupyter notebook
```

Open:

```
Linear_Regression_from_scratch_in_Python.ipynb
```

---

## 📷 Expected Output

- Trained Linear Regression Model
- Predicted values
- Regression Line Visualization
- Learned Weight & Bias values

---

## 🎯 Learning Outcomes

After completing this project, you will understand:

- How Linear Regression works internally
- Mathematics behind Gradient Descent
- How model parameters are updated
- Difference between implementing an algorithm and using a library
- Building ML algorithms from scratch

---

## 📖 Future Improvements

- Multiple Linear Regression
- Feature Scaling
- Polynomial Regression
- Mini-batch Gradient Descent
- Stochastic Gradient Descent
- Model Evaluation Metrics (R², MAE, RMSE)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Rohit Joshi**

Learning Machine Learning by implementing algorithms from scratch 🚀

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!