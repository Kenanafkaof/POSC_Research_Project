import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

# Load the data
data = pd.read_csv("./Gallup Approval.xlsx - Clean Gallup V2.csv")

# Display the first few rows to understand the structure and contents of the dataset
data.head()


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


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# % GDP Change vs. Approve
sns.regplot(x='Approve', y='% GDP Change', data=data, ax=axes[0, 0], scatter_kws={'s':10}, line_kws={'color':'red'}, ci=None)
axes[0, 0].set_title('% GDP Change vs. Approve')

# % RDI Change vs. Approve
sns.regplot(x='Approve', y='% RDI Change', data=data, ax=axes[0, 1], scatter_kws={'s':10}, line_kws={'color':'red'}, ci=None)
axes[0, 1].set_title('% RDI Change vs. Approve')

# Casualties vs. Approve
sns.regplot(x='Approve', y='Casualties', data=data, ax=axes[1, 0], scatter_kws={'s':10}, line_kws={'color':'red'}, ci=None)
axes[1, 0].set_title('Casualties vs. Approve')

# Boxplot for Democrat vs. Approve
sns.boxplot(x='Democrat', y='Approve', data=data, ax=axes[1, 1])
axes[1, 1].set_title('Democrat vs. Approve')

plt.tight_layout()
plt.show()

# Histogram and QQ-Plot for Residuals
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

# Histogram of residuals
sns.histplot(model.resid, kde=True, ax=axes[0])
axes[0].set_title('Histogram of Residuals')

# QQ-Plot for residuals
sm.qqplot(model.resid, fit=True, line='45', ax=axes[1])
axes[1].set_title('QQ-Plot of Residuals')

plt.tight_layout()
plt.show()

# Correlation Matrix Heatmap
correlation_matrix = X.corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()

rolling_avg = data['Approve'].rolling(window=50).mean()

# Plotting the rolling average of approval ratings
plt.figure(figsize=(12, 6))
rolling_avg.plot()
plt.title('Rolling Average of Approval Ratings')
plt.xlabel('Observation Index (as a proxy for time)')
plt.ylabel('Rolling Average Approval Rating')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()



# Plotting Year in Office against Approval Rating and Casualties
plt.figure(figsize=(15, 8))

# Plotting Approval Rating
plt.subplot(2, 1, 1)
plt.plot(data['YRinTerm'], data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
plt.title('Year in Office vs Approval Rating and Casualties')
plt.ylabel('Approval Rating')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plotting Casualties
plt.subplot(2, 1, 2)
plt.plot(data['YRinTerm'], data['Casualties'], 'r-', label='Casualties', alpha=0.7)
plt.xlabel('Year in Office')
plt.ylabel('Casualties')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()


# Plotting Time Sequence against Approval Rating and Casualties

plt.figure(figsize=(15, 8))

# Plotting Approval Rating
plt.subplot(2, 1, 1)
plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
plt.title('Time Sequence vs Approval Rating and Casualties')
plt.ylabel('Approval Rating')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plotting Casualties
plt.subplot(2, 1, 2)
plt.plot(data.index, data['Casualties'], 'r-', label='Casualties', alpha=0.7)
plt.xlabel('Time Sequence')
plt.ylabel('Casualties')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()



# Plotting Approval Rating, % GDP Change, and % RDI Change over time

plt.figure(figsize=(15, 10))

# Plotting Approval Rating
plt.subplot(3, 1, 1)
plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
plt.title('Time Sequence vs Approval Rating, % GDP Change, and % RDI Change')
plt.ylabel('Approval Rating')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plotting % GDP Change
plt.subplot(3, 1, 2)
plt.plot(data.index, data['% GDP Change'], 'g-', label='% GDP Change', alpha=0.7)
plt.ylabel('% GDP Change')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Plotting % RDI Change
plt.subplot(3, 1, 3)
plt.plot(data.index, data['% RDI Change'], 'r-', label='% RDI Change', alpha=0.7)
plt.xlabel('Time Sequence')
plt.ylabel('% RDI Change')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
plt.show()


# Plotting Approval Rating and Party over time

plt.figure(figsize=(15, 7))

# Plotting Approval Rating
plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
plt.title('Time Sequence vs Approval Rating and Party')
plt.ylabel('Approval Rating')

# Highlighting periods where the President was a Democrat
plt.fill_between(data.index, 0, 100, where=data['Democrat'] == 1, color='blue', alpha=0.2, label='Democrat')
plt.fill_between(data.index, 0, 100, where=data['Democrat'] == 0, color='red', alpha=0.2, label='Republican')

plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
