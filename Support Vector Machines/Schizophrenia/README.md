# Schizophrenia

## DISCLAIMER

## Project Description
The purpose of this project was to create a machine learning model 
that can use various lifestyle aspects to predict a diagnosis on schizophrenia.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/asinow/schizohealth-dataset).

## Pre-processing
The data for this project can be found [here](https://www.kaggle.com/datasets/asinow/schizohealth-dataset). Once the data has been imported we drop all rows that contain an empty or NaN value. 
After this we rename the columns, converting them from Turkish to English. 
The `Age` column is then converted into categories (1–6) representing age groups.
Similarly, the symptom score (`Positive_Symptom_Score`, `Negative_Symptom_Score`) 
and the `GAF_Score` (a mental health assessment metric) columns are also put 
into numbered categories based on severity ranges (e.g., scores ≤20 become category 1,
20–40 become category 2). 
This helps to simplify the data and make it easier for analysis.

## Data Understanding
The data for this model consists of 10,000 rows and 20 columns, where each row is x. 

## Algorithms
### Support Vector Machines
Support Vector Machines (SVM) is a machine learning algorithm that finds the best possible "line" (or hyperplane) to separate classes in the data. 
An SVM tries to draw a boundary that maximizes the gap between the closest points of different classes (support vectors).
For non-linear data, it uses "kernels" to transform the data into a higher-dimensional space where separation is easier.
The C parameter controls how strictly it avoids mis-classifications where lower values allow some errors to prevent overfitting.
### Synthetic Minority Over-Sampling Technique (SMOTE)
Another algorithm that was used for this model was SMOTE. 
SMOTE is a method used in machine learning to help address imbalanced datasets by generating new data.
It does this by picking a minority class sample, finding its nearest neighbors, 
and generating new points along the line between them.

## Online & Sources


https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

https://www.geeksforgeeks.org/smote-for-imbalanced-classification-with-python/

https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE

## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Scikit-learn (Sklearn)
- Imblearn