# Cardiovascular Disease Prediction
## DISCLAIMER
The information provided by this cardiovascular disease model is intended for educational purposes only 
and should not be used as a substitute for professional medical advice, diagnosis, or treatment. 
This model is intended to be a tool designed to assist healthcare providers in evaluating risk factors 
and making informed decisions. However, it does not account for all possible patient conditions, 
and clinical judgment must be exercised in all cases.

The creator of this model does not guarantee the accuracy, completeness, 
or applicability of its content for any specific individual. Users should consult with a qualified healthcare provider
for advice tailored to their personal health needs and circumstances. In case of emergency or urgent health concerns, 
please seek immediate medical attention from a licensed professional.

![alt text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fd2icp22po6iej.cloudfront.net%2Fwp-content%2Fuploads%2F2018%2F08%2FPD-AND-THE-HEART3.jpeg&f=1&nofb=1&ipt=bf3b2271b9805e4d026d0a0183c07a20bca35f442597babe5e26b8218948adfe&ipo=images)

## Project Description
The purpose of this project is to create a machine learning model that uses a Random Forest classifier 
to predict the likelihood of cardiovascular disease based on various features 
related to a patient's health and lifestyle.

## Data Source
The data for this project can be found at https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data.

## Pre-processing
Once we've read in our data, we drop all rows with empty values and the `id` column as it is not necessary for 
our pre-processing. After dropping, we take the `weight`, `height`, `ap_hi`, `ap_low` and `age` columns and 
convert them to be categorical.

For the `weight` and `height` columns, we categorize them by using the values to calculate and create the `BMI` column
and then categorizing those values. To do this we first divide the values in the `height` column by 100 to get the 
values in meters, putting them into the new `heights_m` column. Once this is done we get our `BMI` values using 
the sum `df['weight'] / (df['height_m'] ** 2)`. After this we drop the `heights_m` column as it is no longer needed.

With the `ap_hi` and `ap_low` columns we first get the average blood pressure by getting the mean value of the 
two columns combined. After this we categorize the data with a "High" blood pressure being above 120, "Medium" 
being between 80 and 120 and 'Low' being under 80.

For the `ages` column we first divide the column by 365 to convert the data from days into years. After this we once 
again split the data into the categories "Under 18", "18 - 21", "21 - 40", "41 - 60", "61 - 80" and "80+".

Finally, we use a LabelEncoder to convert our categorical labels into numerical labels. This is important as 
some of our data is ordinal (has an inherent order, for example `bp_category` has "Low", "Normal" 
and "High" categories which could be placed in a specific order). Once our ordinal categories have been encoded 
we drop any data that will not be used from this point (`age`, `gender`, `height`, `weight`, `ap_hi` and `ap_lo`).

## Data Understanding
The dataset for this project contains various factors about an individuals health, 
such as age, blood pressure, cholesterol levels. It also contains factors such as if they smoke or partake in physical
activity. The dependent variable, "cardio," indicates whether an individual is likely to have a cardiovascular disease (1) or not (0). 

The `age` column indicates the persons age in days. These ages are converted to years
after which it is categorized into age groups.

The `weight` and `height` columns are representative of the persons weight in kilograms and height in centimeters.
We use these to calculate the persons BMI (Body Mass Index), which is also categorized into groups like 
"Underweight," "Normal," "Overweight," 
and "Obese." 

The `api_hi` and `api_lo` columns are representative of both systolic (maximum pressure during one heartbeat) 
and diastolic (minimum pressure between two heartbeats) blood pressure respectively. 
These two columns combined are used to derive an average measure and classified into 
categories like "Low," "Normal," or "High,"

The `cholesterol` and `gluc` represent a persons cholesterol and glucose levels respectively. They contain a numerical value
with 1 being "normal", 2 being "above normal" and 3 "well above norma".

Smoking habits, alcohol consumption, and physical activity are also included to help assess the risk of 
developing cardiovascular diseases. These values are represented by a binary values (1 if present or 0 if absent)

According to [discussions about the data](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/discussion/206548), 
the highest achievable accuracy is roughly around 74-75%, depending on the type of classification used.

## Algorithms
The main algorithm used in this model is a Random Forest classifier. A Random Forest is a method that uses many 
decision trees to make predictions. Each tree is trained on a random part of the data and looks 
at different features to make decisions. When making a prediction, the forest combines the results 
from all the trees, usually by voting for the most common outcome in classification tasks. 
This approach helps the model make more accurate predictions and avoid mistakes that a 
single tree might make, especially when the data is complex.

## Online & Sources
https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data

https://en.wikipedia.org/wiki/Blood_pressure

https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings

https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php

https://matplotlib.org/stable/users/index

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Matplotlib
- Scikit-learn (Sklearn)