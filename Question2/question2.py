import numpy as np
import pandas as pd

# Step 1: Define the sales data and prices
sales_data = np.array([
    [2, 1, 0, 3, 4],  # HP
    [3, 4, 5, 0, 2],  # Lenovo
    [4, 3, 2, 1, 0],  # Asus
    [1, 0, 3, 4, 2]   # Dell
])

prices = np.array([40000, 45000, 60000, 35000])

# Step 2: Calculate total sales per day
total_sales_per_day = sales_data.sum(axis=0)  # Sum along rows for each column
print(total_sales_per_day)

# Step 3: Calculate revenue per manufacturer
revenue_per_manufacturer = (sales_data * prices[:, np.newaxis]).sum(axis=1)

# Step 4: Append the revenue column to the original sales data
sales_data_with_revenue = np.hstack([sales_data, revenue_per_manufacturer[:, np.newaxis]])  # Append revenue column

# Step 5: Append the total sales row (with a placeholder for revenue)
total_sales_row = np.append(total_sales_per_day, 0)  # Total sales row with 0 as revenue
final_data = np.vstack([sales_data_with_revenue, total_sales_row])  # Add total sales row

# Step 6: Create a pandas DataFrame with proper labels
companies = ["HP", "Lenovo", "Asus", "Dell", "Total Sales"]
columns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Revenue"]
df = pd.DataFrame(final_data, index=companies, columns=columns)

# Display the DataFrame
print(df)