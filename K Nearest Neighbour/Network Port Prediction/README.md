# Network Port Prediction
![url](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.lifewire.com%2Fthmb%2FMcCXj8idU5C0WTH7L6WHueZ93C0%3D%2F1280x847%2Ffilters%3Afill(auto%2C1)%2F152096934-56a1ad953df78cf7726cfc1b.jpg&f=1&nofb=1&ipt=5abd611a94950873967f376bd0c5658d3150b9e8dfc667111e8e24eae49b07d4&ipo=images)
## Project Description
The purpose of this project was to create a machine learning model 
that can use different information about network traffic to try and predict what port the traffic is coming from.

## Data Source
The data for this model can be found [here](https://archive.ics.uci.edu/dataset/542/internet+firewall+data).

## Pre-processing
The first thing that we do to this data set is drop 
all rows that have an empty or NaN value in them. This helps to ensure that our data is clean. After this we map the different types of ports to their respective port numbers. 
We then apply this map to the `Destination Port` column. This helps to make the ports more human-readable and also helps the model to perform better as KNN performs better with meaningful categorical features.
After this we encode the column with a label encoder. This is because K Nearest Neighbour requires numeric input for its distance calculations. The label encoder helps us to ensure that the data remains categorical, while still having a meaningful order.
Finally, we drop any columns that would be meaningless or unnecessary for traffic classification.

## Data Understanding
This dataset contains 65532 rows and 12 columns. Each row in this dataset is a piece of network traffic, 
where each column specifies a different piece of information about that piece of network traffic.

The `Source Port` and `Destination Port` columns indicate which ports traffic is coming from and going to.
The `NAT Source Port` and `NAT Destination` columns are the translated source and destination ports after Network Address Translation (NAT), which
masks the original port for routing.
The `Action` columns indicates the action taken by a firewall for the traffic flow (allowing or dropping the traffic).
The `Bytes` column is the total data volume transferred, or the overall traffic size.
The `Bytes Sent` and `Bytes Recieved` columns are the data transmitted from the source to the destination, and the data
sent back from the destination to the source respectively.
The `Packets` column is the total number of packets exchanged during the session.
The `Elapsed Time (sec)` column indications the duration of the network connection in seconds.
The `pkts_sent` and `pkts_received` columns are the number of packets sent from the source to the destination, 
and the destination to the source respectively.

## Algorithms
### K Nearest Neighbour
The K-Nearest Neighbors (KNN) algorithm works by finding the "closest" data points to a new sample 
and using their majority class (or average value) to make predictions. 
For example, if we set n_neighbors=3, the model checks the 3 nearest training examples to the new data point. 
The "distance" between points is measured, 
and neighbors with smaller distances have a stronger influence . This makes KNN flexible, as it adapts to local patterns 
in the data.
### Synthetic Minority Over-Sampling Technique (SMOTE)
Another algorithm that was used for this model was SMOTE. 
SMOTE is a method used in machine learning to help address imbalanced datasets by generating new data.
It does this by picking a minority class sample, finding its nearest neighbors, 
and generating new points along the line between them.

## Online & Sources
https://archive.ics.uci.edu/dataset/542/internet+firewall+data

https://scikit-learn.org/stable/api/

https://pandas.pydata.org/docs/user_guide/index.html

https://www.geeksforgeeks.org/smote-for-imbalanced-classification-with-python/

https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html#imblearn.over_sampling.SMOTE

## Tools & Technologies Used
- Jupyter Notebook
- Pandas
- Scikit-learn (Sklearn)
- Imblearn