import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('Real_Estate_Sales_2001-2022_GL.csv')

df['Sale Amount'] = pd.to_numeric(df['Sale Amount'], errors='coerce')
df['List Year'] = pd.to_numeric(df['List Year'], errors='coerce')
df['Assessed Value'] = pd.to_numeric(df['Assessed Value'], errors='coerce')

print(df['List Year'].min(), df['List Year'].max())
df = df[df['Property Type'].str.contains("Residential", na=False)]
df = df[df['Residential Type'].str.contains("Single Family", na=False)]


df = df[~df['OPM remarks'].str.contains('INCORRECT SALE AMOUNT', na=False)]

df = df.dropna(subset=['Sale Amount', 'List Year', 'Assessed Value'])

print(df['List Year'].min(), df['List Year'].max())

df = df[(df['Sale Amount'] >= 100000) & (df['Assessed Value'] >= 100000)]
df = df[(df['Sale Amount'] <= 419300) & (df['Assessed Value'] <= 419300)]

# 1. Predict future Sale Amount based on List Year
# Prepare data for predicting Sale Amount using List Year
X_year = df[['List Year']]  # Independent variable (List Year)
y_sale = df['Sale Amount']  # Dependent variable (Sale Amount)

# Initialize the model to predict Sale Amount
year_sale_model = LinearRegression()

# Fit the model
year_sale_model.fit(X_year, y_sale)

# 2. Predict Assessed Value based on Sale Amount
# Prepare data for predicting Assessed Value using Sale Amount
X_sale = df[['Sale Amount']]  # Independent variable (Sale Amount)
y_assessed = df['Assessed Value']  # Dependent variable (Assessed Value)

print(X_sale.max())
print(y_assessed.max())

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

# Cell 6: Visualize Sale Amount vs List Year
plt.scatter(df['Sale Amount'], df['Assessed Value'], color='blue', label='Actual data')
plt.plot(df['List Year'], year_sale_model.predict(X_year), color='red', label='Predicted line')
plt.title('Sale Amount vs List Year')
plt.xlabel('List Year')
plt.ylabel('Sale Amount ($)')
plt.legend()
plt.show()