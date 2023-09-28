import pandas as pd

# Load the data
data = pd.read_csv("./Gallup Approval.xlsx - Clean Gallup V2.csv")

# Display the first few rows to understand the structure and contents of the dataset
data.head()


import matplotlib.pyplot as plt

# Plot approval ratings over time
plt.figure(figsize=(14, 7))
plt.plot(data['DecYR'], data['Approve'], label='Approval Rating', color='blue', alpha=0.7)
plt.xlabel('Year')
plt.ylabel('Approval Rating (%)')
plt.title('Presidential Approval Ratings Over Time')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()



# Approval and casualties 
plt.figure(figsize=(10, 6))
plt.scatter(data['Casualties'], data['Approve'], alpha=0.5, color='red')
plt.xlabel('Casualties')
plt.ylabel('Approval Rating (%)')
plt.title('Approval Ratings vs. Casualties')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()


# GDP Change and Approval Rating
data['% GDP Change'] = pd.to_numeric(data['% GDP Change'], errors='coerce')

# Plot approval ratings against % GDP Change
plt.figure(figsize=(10, 6))
plt.scatter(data['% GDP Change'], data['Approve'], alpha=0.5, color='green')
plt.xlabel('% GDP Change')
plt.ylabel('Approval Rating (%)')
plt.title('Approval Ratings vs. % GDP Change')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()