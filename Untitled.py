#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


data = pd.read_csv('company_data.csv')


total_revenue = data['Revenue'].sum()
total_cost = data['Cost'].sum()
gross_margin = (total_revenue - total_cost) / total_revenue


vendor_profit = data.groupby('Vendor')['Profit'].sum()
most_profitable_vendor = vendor_profit.idxmax()


customer_profit = data.groupby('Customer')['Profit'].sum()
least_profitable_customer = customer_profit.idxmin()


data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])
data['DayOfWeek'] = data['TransactionDate'].dt.day_name()
day_of_week_profit = data.groupby('DayOfWeek')['Profit'].sum()
most_profitable_day = day_of_week_profit.idxmax()

least_profitable_day = day_of_week_profit.idxmin()


average_profit_per_transaction = data['Profit'].mean()


top_selling_product = data.groupby('Product')['Units Sold'].sum().idxmax()


customer_total_sales = data.groupby('Customer')['Revenue'].sum()
customer_highest_sales = customer_total_sales.idxmax()


total_expenses = data['Expenses'].sum()


net_profit = total_revenue - total_expenses


print(f"1. Overall Gross Margin: {gross_margin:.2%}")
print(f"2. Most Profitable Vendor: {most_profitable_vendor}")
print(f"3. Least Profitable Customer: {least_profitable_customer}")
print(f"4. Most Profitable Day of the Week: {most_profitable_day}")
print(f"5. Least Profitable Day of the Week: {least_profitable_day}")
print(f"6. Average Profit per Transaction: ${average_profit_per_transaction:.2f}")
print(f"7. Top-Selling Product: {top_selling_product}")
print(f"8. Customer with Highest Total Sales: {customer_highest_sales}")
print(f"9. Total Expenses: ${total_expenses:.2f}")
print(f"10. Net Profit: ${net_profit:.2f}")


# In[ ]:




