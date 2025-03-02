# Emotion Detection Model

## Project Description
The purpose of this project was to create a machine learning model 
that attempts to detect patterns in faces to predict emotions.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer).

## Pre-processing
Once the data has been imported we define the `load_and_flatten` function which loads images from a directory, 
converts them to greyscale, 
resizes it to 48x48 pixels and stores it into a 1 dimensional array.
We do this to ensure that all images are a similar size and look, and to prepare the image for our K Means Cluster model. 
After loading training and test datasets, pixel values are normalized to [0, 1], 
and string emotion labels (e.g., "angry") are encoded as integers (e.g., 0, 1) using LabelEncoder for model compatibility.
We normalize our pixel values to avoid larger values from dominating K-means distance calculations. 
We encode our emotion labels as our mathematical modules cannot process raw text. 
The same is applied to the test and training data to ensure label consistency. 

## Data Understanding
This dataset consists of 35,685 images of faces divided into training and testing datasets. 
Each image is categorised based on the emotion shown in the facial expressions (happiness, neutral, sadness, anger, surprise, disgust and fear).
## Algorithms
### K Means Clustering
K-Means Clustering is an algorithm that aims to split data into K clusters (groups) where points in the same cluster are 
more similar to each other than to those in other clusters.
Firstly, you decide how many clusters you want, after which the algorithm picks K random starting points ("centroids") 
in the data. These act as temporary cluster centers.
Every data point is assigned to the closest centroid, usually using Euclidean distance.
New centroids are calculated as the average position of all points assigned to each cluster.
This is repeated until centroids stop changing (or change very little), meaning clusters have stabilized.

## Online & Sources
https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html

https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mode.html

https://www.geeksforgeeks.org/k-means-clustering-introduction/

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Scikit-learn (Sklearn)
- CV2 (OpenCV)
- Matplotlib
- Scipy