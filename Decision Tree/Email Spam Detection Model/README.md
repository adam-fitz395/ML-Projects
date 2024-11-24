# Email Spam Detection

![alt](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.smythacademy.com%2Fwordpress%2Fwp-content%2Fuploads%2F2016%2F06%2Fspam.png&f=1&nofb=1&ipt=efd6755b52bf697d989d3aea506d1c55286591caf30e05b899f4c97359dd8475&ipo=images)
## Project Description
The purpose of this project is to create a machine learning model that uses a Random Forest classifier 
to predict whether an email is "Spam" or "Not Spam" based on features extracted from the email data.

## Data Source
The data for this project can be downloaded from https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv/.

## Pre-processing
This dataset is relatively clean and as such only a minial amount of pre-processing is required.
The first thing we do is drop all rows that contain a NaN value. This helps to prevent any errors when 
fitting the model. After this we drop the `Email No.` column as it is unnecessary for our predictions.

After this we extract the features (independent variables) and target (dependant variable) for our predictions. 
We use `df.iloc` for index-based selection in our dataframe. For our features, the colon `:` selects all rows, 
with the `:-1` slicing up to, but not including, the last row. For our target we change this to `-1` 
as we only want the last row.

## Data Understanding
This dataset contains a number of emails, where each row is a separate email. The reason this dataset has so many 
columns is that each one, bar the first (`Email No.`) and last (`Prediction`), are a count of each time a single word 
(such as `the`, `you`, `within`, etc.) occurs within the email.

## Algorithms
The main algorithm used in this model is a Random Forest classifier. A Random Forest is a method that uses many 
decision trees to make predictions. Each tree is trained on a random part of the data and looks 
at different features to make decisions. When making a prediction, the forest combines the results 
from all the trees, usually by voting for the most common outcome in classification tasks. 
This approach helps the model make more accurate predictions and avoid mistakes that a 
single tree might make, especially when the data is complex.

## Online & Sources
https://www.kaggle.com/datasets/balaka18/email-spam-classification-dataset-csv/

https://matplotlib.org/stable/users/index

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

## Tools & Technologies Used
Listed below are some the tools and technologies I used when creating this model:
