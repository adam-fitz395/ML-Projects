# US Housing: Sale vs Assessed Value - Linear Regression Model
## Project Description
The purpose of this project is to predict the sale and assessed values of single family residential properties in the US using a linear regression model.

## Data Source
The data for this project can be downloaded from https://catalog.data.gov/dataset/real-estate-sales-2001-2018

## Pre-processing
Once the data has been downloaded we need to clean it. The first thing we do is ensure that the `Sale Amount`, `Assessed Value` and `List Year` columns all contain only numeric data. After this we filter the properties so that we only see entries that are residential and single family. After this we drop any rows in the `OPM remarks` column that contains the phrase "INCORRECT SALE AMOUNT" as it will cause incorrect data to be entered. Next we drop all rows in the `Sale Amount`, `Assessed Value` and `List Year` columns that contain a NaN value. Finally we filter the `Sale Amount` and `Assessed Value` columns so that we only see real estate that has a value between $100,000 and $419,300 as this filters the data to be within the [median sale price of a house in America in 2024](https://fred.stlouisfed.org/series/MSPUS).

## Data Understanding

## Algorithms

## Online & Sources

## Tools & Technologies Used
