import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

# Load the data
data = pd.read_csv("./Gallup Approval.xlsx - Clean Gallup V2.csv")

# Replace the bullet point character '•' with NaN and convert data types
data['% GDP Change'] = data['% GDP Change'].replace('•', float('nan')).astype(float)
data['% RDI Change'] = data['% RDI Change'].replace('•', float('nan')).astype(float)
data['Casualties'] = data['Casualties'].replace('•', float('nan')).astype(float)
data['Democrat'] = data['Democrat'].astype(int)

# Selecting the independent variables and the dependent variable
X = data[['% GDP Change', '% RDI Change', 'Casualties', 'Democrat']].dropna()
y = data['Approve'][X.index]

# Fit the regression model
model = sm.OLS(y, X).fit()


def plot_gdp_rdi_approval():
    plt.figure(figsize=(15, 10))
    plt.subplot(3, 1, 1)
    plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
    plt.title('Time Sequence vs Approval Rating, % GDP Change, and % RDI Change')
    plt.ylabel('Approval Rating')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(data.index, data['% GDP Change'], 'g-', label='% GDP Change', alpha=0.7)
    plt.ylabel('% GDP Change')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(data.index, data['% RDI Change'], 'r-', label='% RDI Change', alpha=0.7)
    plt.ylabel('% RDI Change')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def plot_approval_party():
    plt.figure(figsize=(15, 7))
    plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
    plt.title('Time Sequence vs Approval Rating and Party')
    plt.ylabel('Approval Rating')
    plt.fill_between(data.index, 0, 100, where=data['Democrat'] == 1, color='blue', alpha=0.2, label='Democrat')
    plt.fill_between(data.index, 0, 100, where=data['Democrat'] == 0, color='red', alpha=0.2, label='Republican')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_approval_casualties():
    plt.figure(figsize=(15, 8))
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
    plt.title('Time Sequence vs Approval Rating and Casualties')
    plt.ylabel('Approval Rating')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['Casualties'], 'r-', label='Casualties', alpha=0.7)
    plt.xlabel('Time Sequence')
    plt.ylabel('Casualties')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def plot_approval_gdp():
    plt.figure(figsize=(15, 8))
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
    plt.title('Time Sequence vs Approval Rating and % GDP Change')
    plt.ylabel('Approval Rating')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['% GDP Change'], 'g-', label='% GDP Change', alpha=0.7)
    plt.xlabel('Time Sequence')
    plt.ylabel('% GDP Change')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def plot_approval_rdi():
    plt.figure(figsize=(15, 8))
    plt.subplot(2, 1, 1)
    plt.plot(data.index, data['Approve'], 'b-', label='Approval Rating', alpha=0.7)
    plt.title('Time Sequence vs Approval Rating and % RDI Change')
    plt.ylabel('Approval Rating')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(data.index, data['% RDI Change'], 'r-', label='% RDI Change', alpha=0.7)
    plt.xlabel('Time Sequence')
    plt.ylabel('% RDI Change')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_approval_rdi()
    #plot_approval_gdp()
    #plot_approval_casualties()
    #plot_approval_party()
    #plot_gdp_rdi_approval()