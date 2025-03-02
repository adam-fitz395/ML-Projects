# Schizophrenia Diagnosis Prediction

![url](http://psychapprentice.weebly.com/uploads/1/3/6/7/13671711/4818521_orig.jpg)
## DISCLAIMER
The machine learning model developed in this project is intended for research and informational purposes only 
and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Project Description
The purpose of this project was to create a machine learning model 
that can use various lifestyle aspects to predict a diagnosis on schizophrenia.
While this model explores correlations between lifestyle factors and potential diagnoses, its predictions are based on limited datasets and statistical patterns, 
which may not account for all individual clinical, genetic, or contextual factors.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/asinow/schizohealth-dataset).

## Pre-processing
The data for this project can be found [here](https://www.kaggle.com/datasets/asinow/schizohealth-dataset). 
Once the data has been imported we drop all rows that contain an empty or NaN value. 
After this we rename the columns, converting them from Turkish to English. 
The `Age` column is then converted into categories (1–6) representing age groups.
Similarly, the symptom score (`Positive_Symptom_Score`, `Negative_Symptom_Score`) 
and the `GAF_Score` (a mental health assessment metric) columns are also put 
into numbered categories based on severity ranges (e.g., scores ≤20 become category 1,
20–40 become category 2). 
This helps to simplify the data and make it easier for analysis.

## Data Understanding
The data for this model consists of 10,000 rows and 20 columns, where each row is a diagnosis for an individual 
and each column is a factor in their lifestyle. Listed below are the various columns and their definitions:
- `Patient_ID`: Unique identifier assigned to each patient in the dataset.
- `Age`: Patient’s age in years (range: 18–80).
- `Gender`: Biological sex of the patient (categories: Male, Female).
- `Education_Level`: Highest educational attainment (1 = Primary, 2 = Middle School, 3 = High School, 4 = University, 5 = Postgraduate).
- `Marital_Status`: Relationship status (0 = Single, 1 = Married, 2 = Divorced, 3 = Widowed).
- `Occupation`: Employment status (0 = Unemployed, 1 = Employed, 2 = Retired, 3 = Student).
- `Income_Level`: Socioeconomic status based on income (0 = Low, 1 = Medium, 2 = High).
- `Diagnosis`: Schizophrenia diagnosis status (0 = Not diagnosed, 1 = Diagnosed).
- `Disease_Duration`: Duration of illness (in years) for schizophrenia patients (1–40 years).
- `Hospitalizations`: Total number of hospital admissions (ranges from 0 to 10).
- `Family_History`: Presence of schizophrenia in immediate family (0 = No, 1 = Yes).
- `Substance_Use`: History of substance use (e.g., tobacco, alcohol, drugs) (0 = No, 1 = Yes).
- `Suicide_Attempt`: History of suicide attempts (0 = No, 1 = Yes).
- `Positive_Symptom_Score`: Severity of positive symptoms (e.g., hallucinations, delusions), scaled 0–100 (higher = more severe).
- `Negative_Symptom_Score`: Severity of negative symptoms (e.g., apathy, social withdrawal), scaled 0–100 (higher = more severe).
- `GAF_Score`: Global Assessment of Functioning score (0–100, lower scores indicate poorer psychological/social functioning).
- `Social_Support`: Perceived level of social support (0 = Low, 1 = Medium, 2 = High).
- `Stress_Factors`: Severity of external stressors (e.g., financial, relational) (0 = Low, 1 = Medium, 2 = High).
- `Medication_Adherence`: Consistency in following prescribed medication (0 = Poor, 1 = Moderate, 2 = Good).

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
https://www.kaggle.com/datasets/asinow/schizohealth-dataset

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

https://www.geeksforgeeks.org/smote-for-imbalanced-classification-with-python/

https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE

https://www.geeksforgeeks.org/ml-one-hot-encoding/

https://www.geeksforgeeks.org/what-is-standardscaler/

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Scikit-learn (Sklearn)
- Imblearn