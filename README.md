# House Price Prediction Project

## Project Overview

This project predicts house prices using Machine Learning techniques in Python. The model is trained on a housing dataset containing features such as area, number of bedrooms, bathrooms, floors, location, condition, garage availability, and year built.

The project was developed using Python in Visual Studio Code and follows a complete machine learning workflow including:

* Data loading
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature encoding
* Model training
* Model evaluation
* Model saving

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── housing_data.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── screenshots/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Dataset Features

The dataset contains the following features:

| Feature   | Description                   |
| --------- | ----------------------------- |
| Area      | Size of the house             |
| Bedrooms  | Number of bedrooms            |
| Bathrooms | Number of bathrooms           |
| Floors    | Number of floors              |
| YearBuilt | Year the house was built      |
| Location  | Area type of the property     |
| Condition | Overall house condition       |
| Garage    | Garage availability           |
| Price     | Target variable (house price) |

---

# Machine Learning Workflow

## 1. Data Loading

The dataset was loaded using Pandas.

## 2. Data Exploration

Performed:

* Dataset inspection
* Statistical summary
* Missing value checking
* Data type analysis

## 3. Data Preprocessing

Categorical columns were encoded using One-Hot Encoding.

## 4. Train-Test Split

The dataset was divided into training and testing sets.

## 5. Model Training

The following models were trained:

* Linear Regression
* Random Forest Regressor

## 6. Model Evaluation

Model performance was evaluated using:

* Mean Absolute Error (MAE)
* R2 Score

## 7. Model Saving

The trained model was saved using Pickle.

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/SaiVarun2107/house-price-prediction.git
```

## 2. Navigate to Project Folder

```bash
cd house-price-prediction
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4. Open the Notebook

Open:

```text
notebooks/house_price_prediction.ipynb
```

and run all cells.

---

# Results

The machine learning models successfully predicted house prices based on the provided housing features.

---

# Future Improvements

Possible future improvements:

* Build a Streamlit web application
* Deploy the model online
* Improve model accuracy
* Add more visualizations
* Use advanced machine learning algorithms
