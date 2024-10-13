# Cell 1: Imports
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Cell 2: Load and Pre-process the dataset
# Load the dataset from a CSV file
df = pd.read_csv('Real_Estate_Sales_2001-2022_GL.csv')

# Convert necessary columns to numeric and handle invalid data by converting it to NaN
df['Sale Amount'] = pd.to_numeric(df['Sale Amount'], errors='coerce')
df['List Year'] = pd.to_numeric(df['List Year'], errors='coerce')

# Filter for residential single-family homes
df = df[df['Property Type'].str.contains("Residential", na=False)]
df = df[df['Residential Type'].str.contains("Single Family", na=False)]

# Remove rows with incorrect sale amounts
df = df[~df['OPM remarks'].str.contains('INCORRECT SALE AMOUNT', na=False)]

# Drop rows with missing data in the important columns
df = df.dropna(subset=['Sale Amount', 'List Year'])

# Filter out extreme sale amounts (only keep values between 100k and 419.3k)
df = df[(df['Sale Amount'] >= 100000) & (df['Sale Amount'] <= 419300)]

# Cell 3: Build and train the model (Sale Amount vs List Year)
# Independent variable (List Year)
X_year = df[['List Year']]  

# Dependent variable (Sale Amount)
y_sale = df['Sale Amount']  

# Initialize and fit the linear regression model
year_sale_model = LinearRegression()
year_sale_model.fit(X_year, y_sale)

# Cell 4: Define a function to predict future sale amounts
def predict_sale_for_year(year):
    # Predict Sale Amount for the given year
    predicted_sale_amount = year_sale_model.predict([[year]])[0]
    return predicted_sale_amount

# Cell 5: Get user input and make predictions
year_input = 0  # Initialize with an invalid value

# Loop until a valid year between 2022 and 2050 is entered
while year_input < 2022 or year_input > 2050:
    try:
        # Get user input and convert to integer
        year_input = int(input("Enter the year you want to predict sales for (2022 - 2050): "))
        
        # Validate the input
        if year_input < 2022:
            raise ValueError('Year must be greater than 2022.')
        if year_input > 2050:
            raise ValueError('Year must be 2050 or less.')
    
    except ValueError as e:
        print(f"Error: {e}. Please try again.\n")

# Make predictions once a valid year is entered
predicted_sale = predict_sale_for_year(year_input)

# Display the predictions
print(f"Predicted Sale Amount for {year_input}: ${predicted_sale:,.2f}")

# Cell 6: Visualization of Sale Amount vs List Year with Future Predictions
import numpy as np  # Import numpy for numerical operations

# Prepare the future years for prediction (2023 to 2050)
future_years = np.arange(2023, 2051).reshape(-1, 1)  # Reshape for model input
predicted_future_sale = year_sale_model.predict(future_years)  # Predict future sale amounts

# Create a figure for plotting
plt.figure(figsize=(12, 6))

# Scatter plot for actual data
plt.scatter(df['List Year'], df['Sale Amount'], color='blue', label='Actual Data', alpha=0.6)

# Plot the fitted line for historical data
plt.plot(df['List Year'], year_sale_model.predict(X_year), color='red', label='Fitted Line', linewidth=2)

# Plot future predictions
plt.plot(future_years, predicted_future_sale, color='green', linestyle='--', label='Future Predictions', linewidth=2)

# Set labels and title
plt.title('Sale Amount vs List Year with Future Predictions', fontsize=16)
plt.xlabel('List Year', fontsize=14)
plt.ylabel('Sale Amount ($)', fontsize=14)

# Set axis limits if needed
plt.xlim(df['List Year'].min() - 1, future_years[-1][0] + 1)  # Extend x-axis to future year
plt.ylim(df['Sale Amount'].min() - 50000, predicted_future_sale.max() + 50000)  # Extend y-axis for predictions

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout
plt.show()

