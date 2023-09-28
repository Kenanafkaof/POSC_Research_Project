import pandas as pd

# Load the data
data = pd.read_csv("./Gallup Approval.xlsx - Clean Gallup V2.csv")

# Display the first few rows to understand the structure and contents of the dataset
data.head()


import statsmodels.api as sm

# Replace the bullet point character '•' with NaN
data['% GDP Change'] = data['% GDP Change'].replace('•', float('nan'))
data['% RDI Change'] = data['% RDI Change'].replace('•', float('nan'))
data['Casualties'] = data['Casualties'].replace('•', float('nan'))

# Convert columns to their appropriate data types
data['% GDP Change'] = pd.to_numeric(data['% GDP Change'], errors='coerce')
data['% RDI Change'] = pd.to_numeric(data['% RDI Change'], errors='coerce')
data['Casualties'] = pd.to_numeric(data['Casualties'], errors='coerce')
data['Democrat'] = data['Democrat'].astype(int)

# Selecting the independent variables and the dependent variable
X = data[['% GDP Change', '% RDI Change', 'Casualties', 'Democrat']]
y = data['Approve']

# Drop rows with nan values
X = X.dropna()
y = y[X.index]

# Fit the regression model again
model = sm.OLS(y, X).fit()

# Get the summary of the regression
model_summary = model.summary()
model_summary
print(model_summary)
