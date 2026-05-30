# House_Price_Prediction
A linear regression model to predict the prices of houses based on their square footage and the number of bedrooms and bathrooms.
README file:
---

# House Price Prediction with Linear Regression

## Overview

This project implements a linear regression model to predict house prices based on square footage, number of bedrooms, and bathrooms. The model utilizes the "House Prices: Advanced Regression Techniques" dataset from Kaggle, which includes features like living area, bedrooms above ground, bathrooms, and sale prices.

## Requirements

- Python 3.x
- Libraries:
  - pandas
  - numpy
  - scikit-learn

## Installation

1. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Download the dataset from Kaggle:
   - Register or log in to Kaggle and download the dataset files (`train.csv` and `test.csv`) from [Bengaluru House price data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data).
   - Place the downloaded files in the project directory.

## Usage

1. Run the Jupyter notebook `House_Pricing.ipynb`.
   
   ```bash
   jupyter notebook House_pricing.ipynb
   ```


2. Follow the instructions in the notebook/script to:
   - Load and preprocess the dataset.
   - Train a linear regression model using features (`GrLivArea`, `BedroomAbvGr`, `FullBath`) to predict house prices (`SalePrice`).
   - Evaluate the model's performance using metrics like Mean Squared Error (MSE) and R-squared.
   - Make predictions for new data points.

## File Descriptions

- `House_Pricing.ipynb`: Jupyter notebook containing the implementation of the linear regression model.
- `HP_app.py`: Python script for the same implementation as the notebook in a streamlit.
- `Bengaluru_House_dat.csv`: Dataset used for training the model.
- `Cleaned_dataset.csv`: Dataset used for testing the model.
- `README.md`: This file, providing an overview of the project, installation instructions, usage guide, and file descriptions.

## Credits

Crafted With Love by **Komal Tiwari**

- Kaggle for providing the "Bengaluru House price data" dataset.
- [Scikit-learn](https://scikit-learn.org/) and [Pandas](https://pandas.pydata.org/) libraries for their machine learning and data manipulation functionalities.



---
