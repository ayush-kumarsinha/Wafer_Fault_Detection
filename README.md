# Wafer_Fault_Detection

# Wafer Fault Detection System

## Project Overview

The Wafer Fault Detection System is an end-to-end Machine Learning project developed to identify defective semiconductor wafers using sensor data. The application processes wafer sensor readings, performs data preprocessing, and predicts whether a wafer is Good or Bad using a trained Balanced Random Forest Classifier.

The project includes data preprocessing, feature engineering, model training, model deployment, and a web-based prediction interface built with Flask.

https://share.google/3ACrIsCA7XsYSsMWm

---

## Business Problem

In semiconductor manufacturing, wafer defects can significantly impact product quality and production costs. Early detection of faulty wafers helps manufacturers reduce waste, improve efficiency, and maintain product quality.

The objective of this project is to automate wafer quality inspection using machine learning techniques.

---

## Features

* Upload wafer sensor data in CSV format
* Automated data preprocessing
* Missing value handling using Simple Imputer
* Feature selection using Variance Threshold
* Balanced Random Forest model for classification
* Real-time prediction through Flask web application
* Displays count of Good and Bad wafers
* Easy-to-use web interface

---

## Dataset Information

The dataset contains sensor readings collected from semiconductor wafers.

### Input Features

* Sensor-1 to Sensor-590
* Wafer Identifier

### Target Variable

* Good/Bad

  * 1 = Good Wafer
  * -1 = Bad Wafer

---

## Machine Learning Pipeline

### Data Preprocessing

* Missing Value Treatment
* Removal of Constant Features
* Feature Selection using Variance Threshold

### Handling Class Imbalance

* SMOTE (Synthetic Minority Oversampling Technique)

### Model Training

Several machine learning models were evaluated, including:

* Logistic Regression
* Random Forest
* XGBoost
* Balanced Random Forest

Balanced Random Forest achieved the best performance and was selected as the final model.

---

## Technologies Used

* Python 3.13
* Pandas
* NumPy
* Scikit-Learn
* Imbalanced-Learn
* Flask
* Joblib
* Matplotlib
* Seaborn
* Google Colab
* VS Code

---

## Project Structure

```text
Wafer_Fault_Detection/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── wafer_fault_detection_model.pkl
│   ├── imputer.pkl
│   └── selector.pkl
│
├── dataset/
│   ├── Training_DataSet_Files/
│   └── Prediction_Batch_files/
│
├── notebook/
│   └── wafer_training.ipynb
│
├── templates/
│   └── index.html
│
├── uploads/
├── outputs/
└── screenshots/
```

---

## Model Performance

### Balanced Random Forest

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 92%   |
| Precision | 35%   |
| Recall    | 44%   |
| F1 Score  | 39%   |

The model effectively handles the highly imbalanced wafer dataset and provides reliable fault detection.

---

## How to Run the Project

### Clone Repository

```bash
git clone <repository-url>
cd Wafer_Fault_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

---

## Future Improvements

* Docker Deployment
* Cloud Deployment (AWS/Azure)
* Model Monitoring Dashboard
* Advanced Hyperparameter Tuning
* Deep Learning-Based Fault Detection
* Interactive Analytics Dashboard

---

## Author

Ayush Kumar

Computer Science Engineering Student

Skills:

* Python
* Machine Learning
* Data Analysis
* SQL
* Power BI
* Tableau
* Flask

---

This project demonstrates practical implementation of Machine Learning, Data Preprocessing, Model Deployment, and Web Application Development for semiconductor wafer fault detection.
