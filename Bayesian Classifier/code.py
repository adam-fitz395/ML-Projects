import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import OrdinalEncoder
import ipywidgets as widgets

df = pd.read_csv('Road Accident Data.csv', dtype = str)
df = df.dropna(axis=0)

df = df.drop('Accident_Index', axis=1)
df = df.drop('Accident Date', axis=1)
df = df.drop('Month', axis=1)
df = df.drop('Year', axis=1)
df = df.drop('Day_of_Week', axis=1)
df = df.drop('Junction_Control', axis=1)
df = df.drop('Junction_Detail', axis=1)

df.head()
# Get the number of rows and columns
rows = len(df.axes[0])
cols = len(df.axes[1])

# Print the number of rows and columns
print("Number of Rows: " + str(rows))
print("Number of Columns: " + str(cols))


print(df['Light_Conditions'].value_counts())
print(df['Accident_Severity'].value_counts())

print(df['Road_Surface_Conditions'].value_counts())

X = df[['Light_Conditions', 'Road_Surface_Conditions', 'Road_Type', 'Speed_limit', 'Urban_or_Rural_Area', 'Weather_Conditions', 'Vehicle_Type']]
y = df['Accident_Severity']

# Encode data numerically to deal with categorical data values
encoder = OrdinalEncoder()
X_encoded = encoder.fit_transform(X)

# Synthetic Minority Oversampling Technique - Generates new minority instances to balance class distribution
smote = SMOTE(sampling_strategy="not majority", random_state=42) # Do not sample majority, no need as it is imbalanced
X_resampled, y_resampled = smote.fit_resample(X_encoded, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.8, random_state=42)

gnb = CategoricalNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)

surface_conditions = df['Road_Surface_Conditions'].dropna().unique()
light_conditions = df['Light_Conditions'].dropna().unique()
speed_limits = df['Speed_limit'].dropna().unique()
urbanOrRural = df['Urban_or_Rural_Area'].dropna().unique()
weatherConditions = df['Weather_Conditions'].dropna().unique()
vehicleType = df['Vehicle_Type'].dropna().unique()

# Create dropdown widgets
surface_dropdown = widgets.Dropdown(
    options=surface_conditions,
    description="Road Surface:",
    value=surface_conditions[0]  # Default value
)

light_dropdown = widgets.Dropdown(
    options=light_conditions,
    description="Light Conditions:",
    value=light_conditions[0]
)

speed_dropdown = widgets.Dropdown(
    options=sorted(speed_limits),  # Sort numerical values
    description="Speed Limit:",
    value=speed_limits[0]
)

urban_dropdown = widgets.Dropdown(
    options=urbanOrRural,
    description="Urban or Rural Area:",
    value=urbanOrRural[0]
)

weather_dropdown = widgets.Dropdown(
    options=weatherConditions,
    description="Weather Conditions:",
    value=weatherConditions[0]
)

vehicleType_dropdown = widgets.Dropdown(
    options=vehicleType,
    description="Vehicle Type:",
    value=vehicleType[0]
)

def make_prediction(df):


# Display the widgets
display(surface_dropdown, light_dropdown, speed_dropdown, urban_dropdown, weather_dropdown, vehicleType_dropdown)

predict_button = widgets.Button(description="Predict Severity")
predict_button.on_click(make_prediction())
display(predict_button)