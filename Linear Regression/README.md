# US Housing: Sale vs Assessed Value - Linear Regression Model
## Project Description
The purpose of this project is to predict the sale and assessed values of single family residential properties in the US using a linear regression model.

## Data Source
The data for this project can be downloaded from https://catalog.data.gov/dataset/real-estate-sales-2001-2018

## Pre-processing
Once the data has been downloaded we need to clean it. The first thing we do is ensure that the `Sale Amount`, `Assessed Value` and `List Year` columns all contain only numeric data. After this we filter the properties so that we only see entries that are residential and single family. After this we drop any rows in the `OPM remarks` column that contains the phrase "INCORRECT SALE AMOUNT" as it will cause incorrect data to be entered. Next we drop all rows in the `Sale Amount`, `Assessed Value` and `List Year` columns that contain a NaN value. Finally we filter the `Sale Amount` and `Assessed Value` columns so that we only see real estate that has a value between $100,000 and $419,300 as this filters the data to be within the [median sale price of a house in America in 2024](https://fred.stlouisfed.org/series/MSPUS).

## Data Understanding

## Algorithms
The main algorithm used in this project is linear regression. Linear regression consists of two main steps, training the model and then using it to make predictions. During the training phase, the algorithm is provided with historical data containing both the independent variables (what we're changing) and the dependent variable (what we're trying to find). The goal is to find the best-fitting line that minimizes the error between the predicted and actual target values. Once the model is trained, it can be used to make future predictions. One of the main drawbacks of this algorithim is that the data needs to have somewhat of a linear relationship, otherwise the model will perform poorly.
## Online & Sources
https://catalog.data.gov/dataset/real-estate-sales-2001-2018
https://matplotlib.org/stable/users/index
https://pandas.pydata.org/docs/user_guide/index.html#user-guide
https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LinearRegression.html
## Tools & Technologies Used
Listed below are some of the new technologies and tools I had the opportunity to use while working on this project:
### Pandas
Pandas, one such technology, is a widely-used open-source Python library designed for data manipulation and analysis. It provides data structures like DataFrames (2D labeled data) and Series (1D labeled data) that allow users to easily manage, clean, and analyze data, similar to a spreadsheet or SQL table. It offers a wide range of tools for handling data such as filtering rows and merging datasets, which was use-ful for the pre-processing of my data.
### Sklearn
Another library I learned how to use is the Sklearn library, a popular open-source Python library for machine learning and data analysis. It provides simple tools for a wide range of machine learning tasks, including classification, regression, and preprocessing. I utilised this library for it's linear regression model and to fit my data to the model.
### Matplotlib
Matplotlib is a comprehensive and widely-used Python library for creating static, animated, and interactive visualizations. It provides tools for generating a wide variety of plots and graphs, including line charts, bar charts, histograms and scatter plots, making it an essential tool for data visualization in Python. For this project I used it create a scatter plot of my data and visualise the line of best fit for the data.
