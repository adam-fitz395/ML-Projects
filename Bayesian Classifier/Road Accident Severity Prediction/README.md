# Road Accident Severity Prediction

![alt](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.motionpictures.org%2Fwp-content%2Fuploads%2F2017%2F04%2FCars358dd6f1c65330.jpg&f=1&nofb=1&ipt=8eff2967cbe7cfa63b32e69b9bc51d0c054783ee855f82db662bd7e9d547fc1f&ipo=images)
## Project Description
The purpose of this project was to create a machine learning model 
that can use various elements involved in a crash to predict what the severity 
of a crash would be.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/xavierberge/road-accident-dataset).

## Pre-processing
When pre-processing this data the first thing we do is 
drop all rows containing a **null** or **NaN** value. This helps to ensure that the data 
is of a higher quality and to help avoid errors when using our algorithms. 
Once these empty rows have been dropped, we drop any columns containing data 
that is not relevant to the model, such as the `Accident_Index` and `Accident_Date` columns.

## Data Understanding
This dataset contains data about road accidents and the various conditions that they have occurred under. 
The data set contains **23 columns** and **over 5,000 rows**. Each column is a different factor involved in a crash, 
while each row is a singular instance of a crash.

The `Light_Conditions` column records the lighting environment at the time of the accident.
The `Road_Surface_Conditions` column lists the state of the road, in regard to weather, at the time of the crash.
The `Speed_limit` column indicates the maximum legal speed allowed in the area where the accident occurred.
The `Urban_or_Rural_Area` distinguishes if the accident occurred in an **urban** or **rural** area.
The `Weather_Conditions` column details the weather at the time of the accident and finally 
the `Vehicle_Type` column identifies the type of vehicle involved.

The count of data for this model ended up being imbalanced, 
due to there being more *Slight* severity accidents than Serious or Fatal. To address this imbalance 
***[Synthetic Minority Over-Sampling Technique (SMOTE)](#synthetic-minority-over-sampling-technique-smote)***  is used to generate new data for the Serious and Fatal severities.

## Algorithms
### Naive Bayes
The main algorithm used for this model is a Classification Naive Bayes algorithm. This algorithm is based on Bayes' Theorem, 
a mathematical formula used to calculate the probability of an event occurring 
based on prior knowledge of conditions related to the event. The algorithm is considered "naive" 
as it assumes that all features are independent, even though that may not be the case.
### Synthetic Minority Over-Sampling Technique (SMOTE)
Another algorithm that was used for this model was SMOTE. 
SMOTE is a method used in machine learning to help address imbalanced datasets by generating new data.
It does this by picking a minority class sample, finding its nearest neighbors, 
and generating new points along the line between them.
### Ordinal Encoding
Ordinal Encoding is used to convert categorical data into numerical values so that machine learning models can process it. 
It assumes that the categories have a natural ranking and assigns them an integer value as such.
## Online & Sources
https://www.kaggle.com/datasets/xavierberge/road-accident-dataset

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

https://www.geeksforgeeks.org/smote-for-imbalanced-classification-with-python/

https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE

https://www.geeksforgeeks.org/how-to-perform-ordinal-encoding-using-sklearn/
## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Scikit-learn (Sklearn)
- Imblearn
- Ipywidgets
