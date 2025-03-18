# Melanoma Cancer Detection Model

## DISCLAIMER
The machine learning model developed in this project is intended for research and informational purposes only 
and must not be used as a substitute for professional medical advice, diagnosis, or treatment.

## Project Description
This project aims to attempt to predict whether a lesion is benign or malignant using a Multi-layer Perceptron (MLP) model.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset).

## Pre-processing
Once the data has been imported we define the `load_and_flatten` function which loads images from a directory, 
converts them to greyscale, 
resizes it to 48x48 pixels and stores it into a 1 dimensional array.
We do this to ensure that all images are a similar size and look, and to prepare the image for our MLP model.
After loading training and test datasets, pixel values are normalized to [0, 1], 
and string labels (e.g. "Malignant") are encoded as integers (e.g., 0, 1) using the LabelEncoder for model compatibility.
We normalize our pixel values to ensure that they are proportional and to ensure that it is easier for the model to handle images. 
We encode our labels as the neural network model cannot process raw text. 
The same is applied to the test and training data to ensure label consistency. 

## Data Understanding 
Melanoma is a form of skin cancer caused by exposure to ultraviolet (UV) light, typically from the sun or sun beds. 
Melanoma, if detected early enough, is usually treated through surgery. 

This dataset consists of 13,900 images of benign and malignant lesions related to melanoma.
Benign tumors are made up of cells that don't threaten to invade other tissues. 
They are usually harmless unless they are near a vital area.
Malignant tumors are made of cancer cells that can invade other nearby tissues.
They tend to be abnormal and different to the usual surrounding tissue.

## Algorithms
### Multi-layer Perceptron
An MLP is a foundational type of artificial neural network (ANN) designed for supervised learning tasks. 
This algorithm consists of an input layer, one or more hidden layers of interconnected neurons,
and an output layer. Each neuron applies a nonlinear activation function 
(a mathematical function applied to the output of a neuron that introduces non-linearity into the model, 
allowing the network to learn and represent complex patterns in the data) 
to weighted inputs, enabling the network to model complex relationships in data. 
MLPs leverage backpropagation (a technique used in deep learning that iteratively adjusts weights and bias)
to minimize prediction errors during training.
### Grid Search Cross Validation (CV)
Grid Search CV (Cross-Validation) is a hyperparameter tuning technique used to systematically evaluate combinations of 
model parameters to identify the optimal configuration for a machine learning algorithm.
This is done by training and validating the model based on each parameter combination and scoring each combination. 
The search then returns the parameter set with the best average validation score.

## Online & Sources
https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset

https://scikit-learn.org/stable/modules/neural_networks_supervised.html

https://scikit-learn.org/stable/api/

https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html

https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/

https://www.geeksforgeeks.org/opencv-python-tutorial/

https://www.geeksforgeeks.org/activation-functions-neural-networks/

https://www.geeksforgeeks.org/backpropagation-in-neural-network/

https://en.wikipedia.org/wiki/Lesion

https://www2.hse.ie/conditions/skin-cancer-melanoma/

## Tools & Technologies Used
- Jupyter Notebook
- Scikit-learn (Sklearn)
- CV2 (OpenCV)
- Matplotlib
- Scipy