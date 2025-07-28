# Save the dataset to Excel
df.to_excel('supermarket_sales_data.xlsx', index=False)

# Create summary analytics for the dashboard insights
summary_stats = {}

# 1. Total Revenue and Gross Income
total_revenue = df['Total'].sum()
total_gross_income = df['Gross Income'].sum()
total_transactions = len(df)

summary_stats['Total Revenue'] = f"${total_revenue:,.2f}"
summary_stats['Total Gross Income'] = f"${total_gross_income:,.2f}"
summary_stats['Total Transactions'] = f"{total_transactions:,}"

# 2. Branch-wise Performance
branch_performance = df.groupby('Branch').agg({
    'Total': ['sum', 'count'],
    'Gross Income': 'sum'
}).round(2)

branch_performance.columns = ['Total_Revenue', 'Transaction_Count', 'Gross_Income']
branch_performance = branch_performance.sort_values('Total_Revenue', ascending=False)

print("Branch-wise Performance:")
print(branch_performance)

# 3. Product Line Performance
product_line_performance = df.groupby('Product Line').agg({
    'Total': ['sum', 'count'],
    'Gross Income': 'sum',
    'Rating': 'mean'
}).round(2)

product_line_performance.columns = ['Total_Revenue', 'Transaction_Count', 'Gross_Income', 'Avg_Rating']
product_line_performance = product_line_performance.sort_values('Total_Revenue', ascending=False)

print("\n\nProduct Line Performance:")
print(product_line_performance)

# 4. Customer Type Analysis
customer_analysis = df.groupby('Customer Type').agg({
    'Total': ['sum', 'count', 'mean'],
    'Gross Income': 'sum',
    'Rating': 'mean'
}).round(2)

customer_analysis.columns = ['Total_Revenue', 'Transaction_Count', 'Avg_Transaction', 'Gross_Income', 'Avg_Rating']

print("\n\nCustomer Type Analysis:")
print(customer_analysis)

# 5. Payment Method Analysis
payment_analysis = df.groupby('Payment').agg({
    'Total': ['sum', 'count'],
    'Gross Income': 'sum'
}).round(2)

payment_analysis.columns = ['Total_Revenue', 'Transaction_Count', 'Gross_Income']
payment_analysis = payment_analysis.sort_values('Total_Revenue', ascending=False)

print("\n\nPayment Method Analysis:")
print(payment_analysis)

# 6. Monthly Sales Trends
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()

monthly_trends = df.groupby(['Month', 'Month_Name']).agg({
    'Total': ['sum', 'count'],
    'Gross Income': 'sum'
}).round(2)

monthly_trends.columns = ['Total_Revenue', 'Transaction_Count', 'Gross_Income']
monthly_trends = monthly_trends.sort_values('Month')

print("\n\nMonthly Sales Trends:")
print(monthly_trends)

# Save summary analytics
with open('summary_analytics.txt', 'w') as f:
    f.write("SUPERMARKET SALES ANALYTICS SUMMARY\n")
    f.write("=" * 50 + "\n\n")
    f.write("Key Metrics:\n")
    for key, value in summary_stats.items():
        f.write(f"- {key}: {value}\n")
    
    f.write(f"\n\nBranch Performance:\n{branch_performance.to_string()}\n")
    f.write(f"\n\nProduct Line Performance:\n{product_line_performance.to_string()}\n")
    f.write(f"\n\nCustomer Analysis:\n{customer_analysis.to_string()}\n")
    f.write(f"\n\nPayment Method Analysis:\n{payment_analysis.to_string()}\n")
    f.write(f"\n\nMonthly Trends:\n{monthly_trends.to_string()}\n")

print(f"\n\nKey Insights:")
print(f"- Total Revenue: {summary_stats['Total Revenue']}")
print(f"- Total Gross Income: {summary_stats['Total Gross Income']}")
print(f"- Total Transactions: {summary_stats['Total Transactions']}")
print(f"- Average Transaction Value: ${df['Total'].mean():.2f}")
print(f"- Top Performing Branch: {branch_performance.index[0]}")
print(f"- Best Product Line: {product_line_performance.index[0]}")