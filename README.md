# AQI-Project
# 🌍 Air Quality Index (AQI) Prediction Web App

This project is a machine learning-based web application that predicts the **Air Quality Index (AQI)** using pollutant concentrations. It is built using **Python**, **Streamlit**, and trained using environmental data from Indian air monitoring stations.

## 📌 Features

- 🎯 Predicts AQI based on:
  - CO (Carbon Monoxide)
  - O₃ (Ozone)
  - NO₂ (Nitrogen Dioxide)
  - SO₂ (Sulfur Dioxide)
  - PM2.5
  - PM10
- 💡 Displays AQI category with interpretation
- 🎨 Clean and interactive Streamlit-based UI
- 📊 Machine learning model trained on real environmental data from 2023

## 🗂️ Project Structure

├── Finaltstproject.py # Streamlit front-end for AQI prediction
├── project.ipynb # Backend model development and training (Jupyter Notebook)
├── finalmodel.pkl # Trained regression model (used in frontend)
├── YEARLY_2023_CAAQMS_...csv # Source dataset used for training
├── screenshots/ # UI screenshots of the web application
└── README.md # You're reading it!

## 🛠️ Tech Stack
- **Python 3.x**
- **Streamlit**
- **scikit-learn**
- **pandas**, **numpy**
- **matplotlib / seaborn** (for EDA in the notebook)

##📈 Dataset
Source: Central Pollution Control Board (CPCB) - 2023

File: YEARLY_2023_CAAQMS_FINAL_UPLOAD_merged 2.csv

Contains pollutant concentrations and corresponding AQI values used for model training.


