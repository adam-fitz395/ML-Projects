# Imports
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Read in CSV file and pre-process
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL.csv')

# Ensure columns with numeric values are only numeric
df['Sale Amount'] = pd.to_numeric(df['Sale Amount'], errors='coerce')
df['List Year'] = pd.to_numeric(df['List Year'], errors='coerce')
df['Assessed Value'] = pd.to_numeric(df['Assessed Value'], errors='coerce')

# Filter data by residential properties, but keep all columns
df = df[
    df['Property Type'].str.contains("Residential", na=False) &
    df['Residential Type'].str.contains("Single Family", na=False)
]

# Drop rows where 'OPM remarks' contains 'INCORRECT SALE AMOUNT'
df = df[~df['OPM remarks'].str.contains('INCORRECT SALE AMOUNT', na=False)]

# Drop all rows with NaN data in the relevant columns
df = df.dropna(subset=['Sale Amount', 'List Year', 'Assessed Value'])

# Drop rows with Sale Amount or Assessed Value less than 100,000 and greater than 419300 (the average median cost of a house in america in 2023)
df = df[(df['Sale Amount'] >= 100000) & (df['Assessed Value'] >= 100000)]
df = df[(df['Sale Amount'] <= 419300) & (df['Assessed Value'] <= 419300)]

# 1. Predict future Sale Amount based on List Year
# Prepare data for predicting Sale Amount using List Year
X_year = df[['List Year']]
y_sale = df['Sale Amount']

# Initialize the model to predict Sale Amount
year_sale_model = LinearRegression()

# Fit the model
year_sale_model.fit(X_year, y_sale)

# 2. Predict Assessed Value based on Sale Amount
# Prepare data for predicting Assessed Value using Sale Amount
X_sale = df[['Sale Amount']]
y_assessed = df['Assessed Value']

# Initialize the model to predict Assessed Value
sale_assessed_model = LinearRegression()

# Fit the model
sale_assessed_model.fit(X_sale, y_assessed)

# 3. Function to predict Sale Amount and Assessed Value for a given year
def predict_for_year(year):
    # Predict Sale Amount for the given year
    predicted_sale_amount = year_sale_model.predict([[year]])[0]

    # Predict Assessed Value based on the predicted Sale Amount
    predicted_assessed_value = sale_assessed_model.predict([[predicted_sale_amount]])[0]

    return predicted_sale_amount, predicted_assessed_value

# 4. Take user input for the year
year_input = 0  # Initializing year_input with an invalid value

# Loop until a valid year is entered (greater than 2022)
while year_input < 2022 or year_input > 2050:
    try:
        # Get user input and convert to integer
        year_input = int(input("Enter the year you want to predict sales for (2022 - 2050): "))
        
        # Check if the input year is valid
        if year_input < 2022:
            # Raise an IOError if the year is less than or equal to 2022
            raise IOError('Year must be greater than 2022')
        
        if year_input > 2050:
            # Raise an IOError if the year is less than or equal to 2022
            raise IOError('Year must 2050 or less')
    
    except IOError as e:
        # Print the error message and prompt the user to try again
        print(f"Error: {e}. Please try again.\n")
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input. Please enter a valid year.")

# Once a valid year is entered, proceed with the prediction
print(f"Valid year entered: {year_input}. Proceeding with predictions...")
# Call your prediction function here (e.g., predict_for_year(year_input))

            

# Predict Sale Amount and Assessed Value for the entered year
predicted_sale, predicted_assessed = predict_for_year(year_input)

# Print results
print(f"Predicted Sale Amount for {year_input}: ${predicted_sale:,.2f}")
print(f"Predicted Assessed Value for {year_input}: ${predicted_assessed:,.2f}")
print(df['List Year'].min(), df['List Year'].max())


# Step 1: Get user input for the year
end_year = 0  # Initialize with an invalid value

# Loop until a valid year is entered (greater than or equal to the last year in the dataset)
while end_year < df['List Year'].min() or end_year > 2050:
    try:
        end_year = int(input(f"Enter the year you want to see sales until (between {df['List Year'].min()} and 2050): "))
        
        # Validate the input
        if end_year < df['List Year'].min():
            raise ValueError(f'Year must be greater than or equal to {df["List Year"].min()}.')
        if end_year > 2050:
            raise ValueError('Year must be 2050 or less.')
    
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

# Step 2: Create a range of years from the minimum List Year to the user-specified year
years_to_predict = np.arange(df['List Year'].min(), end_year + 1, 1).reshape(-1, 1)  # Step by 1 year

# Step 3: Predict sale amounts for these years
predicted_sale_amounts = year_sale_model.predict(years_to_predict)

# Step 4: Plotting the predicted sale prices over the specified years
plt.figure(figsize=(12, 6))
plt.plot(years_to_predict, predicted_sale_amounts, color='green', linewidth=2, label='Predicted Sale Price', marker='o')  # Added marker for better visibility

# Plot the historical data for reference
plt.scatter(df['List Year'], df['Sale Amount'], color='blue', label='Actual Data', alpha=0.6)

# Set labels and title
plt.title(f'Sale Price Predictions from {df["List Year"].min()} to {end_year}', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Predicted Sale Price ($)', fontsize=14)

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout
plt.show()