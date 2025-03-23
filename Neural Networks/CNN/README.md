# Rock, Paper, Scissors

## Project Description
This project aims to create a Convolutional Neural Network that is capable of accurately recognizing 
and classifying hand gestures in rock, paper, scissors games.

## Data Source
The data for this model can be found [here](https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset/data).

## Pre-processing
The data for this model can be found [here](https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset/data). In this section we preprocess our images for training and testing. Using the `image_dataset_from_directory`, 
images are automatically loaded from structured directories. Once all images are loaded, 
they are resized to IMAGE_SIZE (48px by 48px), converted to grayscale, and batched. 
The `label_mode='categorical'` parameter converts labels to one-hot encoded vectors for multi-class classification. 
Pixel values are then normalized to [0,1] using a rescaling layer. 
The `prefetch(tf.data.AUTOTUNE)` method optimizes data loading by preparing batches in the background during training.
## Data Understanding
This dataset contains 2,892 images of a variety of different hands, from different ages, 
races and genders, performing the various poses involved in rock, paper scissors.

## Algorithms
### Convolutional Neural Network
Convolutional Neural Networks (CNNs) are specialized deep learning models designed to process grid-structured data, 
such as images, by hierarchically extracting spatial patterns. They begin with convolutional layers, 
which apply learnable filters (kernels) to the input, detecting edges, textures, 
and shapes through weighted sums of pixel values. These filters slide across the image, 
producing feature maps that highlight detected patterns. Pooling layers (e.g. max-pooling) then downsample these maps, 
reducing dimensionality while preserving critical features, 
improving computational efficiency and translation invariance. 
Deeper layers combine simpler features into complex structures (e.g. entire hands or objects). 
Finally, fully connected layers interpret these high-level features for classification. 
## Online & Sources
https://www.kaggle.com/datasets/sanikamal/rock-paper-scissors-dataset/data

https://keras.io/guides/

https://matplotlib.org/stable/index.html

https://www.tensorflow.org/api_docs

https://numpy.org/doc/stable/

https://www.geeksforgeeks.org/introduction-convolution-neural-network/

https://learnopencv.com/understanding-convolutional-neural-networks-cnn/

https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939/
## Tools & Technologies Used
- Jupyter Notebook
- Tensorflow
- Matplotlib
- Numpy
- Keras