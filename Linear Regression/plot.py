import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
df = pd.read_csv('average-hourly-pay.csv')

df = df.replace("n/a", np.nan)
df = df.dropna(subset=['Value'])

df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Year'] = pd.to_numeric(df['Time'], errors='coerce')

x = pd.get_dummies(df[['Ethnicity', 'Year']], drop_first=True)
y = df['Value']

model = LinearRegression()
model.fit(x, y)

predicted_pay = model.predict(x)

results = pd.DataFrame(
    {
        'Ethnicity': df['Ethnicity'], 
        'Year': df['Year'], 
        'Predicted Pay': predicted_pay,
        'Actual Pay': y
    })
print(results)

plt.figure(figsize=(12, 6))
plt.scatter(y, predicted_pay, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')  # Line of equality
plt.xlabel('Actual Average Hourly Pay')
plt.ylabel('Predicted Average Hourly Pay')
plt.title('Actual vs. Predicted Average Hourly Pay by Ethnicity and Year')
plt.grid(True)
plt.show()

coefficients = pd.DataFrame(model.coef_, x.columns, columns=['Coefficient'])
print(coefficients)