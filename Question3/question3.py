import numpy as np
import pandas as pd

# Step 1: Generate random sales data between 0 and 6 for 4 companies (HP, Lenovo, Asus, Dell)
np.random.seed(42)  # Set seed for reproducibility
sales_data = np.random.randint(0, 7, size=(4, 5))  # Random sales between 0 and 6 for 4 companies over 5 days

# Step 2: Create a DataFrame
companies = ['HP', 'Lenovo', 'Asus', 'Dell']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
df = pd.DataFrame(sales_data, index=companies, columns=days)

# Step 3: Calculate the total sales for each day and add it as a new row
df.loc['Total Sales'] = df.sum(axis=0)

# Step 4: Prices for each manufacturer
prices = np.array([40000, 45000, 55000, 35000])

# Step 5: Calculate total revenue for each manufacturer and add it as a new column
revenue_per_manufacturer = (sales_data * prices[:, np.newaxis]).sum(axis=1)
df['Revenue'] = np.append(revenue_per_manufacturer, 0)  # Adding 0 for the 'Total Sales' row

# Step 6: Save the DataFrame to a CSV file
df.to_csv('sales_data_ques3.csv')

# Step 7: Read the CSV file back into a DataFrame
df_read = pd.read_csv('sales_data_ques3.csv', index_col=0)

# Step 8: Find the company with the best sales performance
# Find the index of the highest total sales (excluding 'Total Sales' row)
total_sales = df_read.loc['Total Sales', days].tolist()  # Get the total sales per day as a list
best_sales_index = total_sales.index(max(total_sales))  # Find the company with the maximum sales
best_company = companies[best_sales_index]  # Get the company name corresponding to the best sales

# Display the DataFrame and the best company
print("Sales DataFrame:\n", df_read)
print(f"The company with the best sales performance is: {best_company}")