# Create a comprehensive DAX formulas reference document
dax_formulas = """
# Power BI DAX Formulas for Supermarket Sales Dashboard

## Basic Measures

### Revenue Calculations
```dax
Total Revenue = SUM(Sales[Total])

Total Gross Income = SUM(Sales[Gross Income])

Total COGS = SUM(Sales[COGS])

Average Transaction Value = DIVIDE([Total Revenue], [Total Transactions])

Gross Margin % = DIVIDE([Total Gross Income], [Total Revenue])
```

### Transaction Metrics
```dax
Total Transactions = COUNTROWS(Sales)

Unique Customers = DISTINCTCOUNT(Sales[Customer ID])

Average Items per Transaction = DIVIDE(SUM(Sales[Quantity]), [Total Transactions])

Average Rating = AVERAGE(Sales[Rating])
```

## Time Intelligence

### Year-over-Year Analysis
```dax
Revenue YTD = TOTALYTD([Total Revenue], Sales[Date])

Revenue Previous Year = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR(Sales[Date]))

YoY Growth % = DIVIDE([Total Revenue] - [Revenue Previous Year], [Revenue Previous Year])

YoY Growth Amount = [Total Revenue] - [Revenue Previous Year]
```

### Month-over-Month Analysis
```dax
Revenue MTD = TOTALMTD([Total Revenue], Sales[Date])

Revenue Previous Month = CALCULATE([Total Revenue], PREVIOUSMONTH(Sales[Date]))

MoM Growth % = DIVIDE([Total Revenue] - [Revenue Previous Month], [Revenue Previous Month])

Rolling 3-Month Revenue = 
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(Sales[Date], LASTDATE(Sales[Date]), -3, MONTH)
)
```

### Quarter Analysis
```dax
Revenue QTD = TOTALQTD([Total Revenue], Sales[Date])

Revenue Previous Quarter = CALCULATE([Total Revenue], PREVIOUSQUARTER(Sales[Date]))

QoQ Growth % = DIVIDE([Total Revenue] - [Revenue Previous Quarter], [Revenue Previous Quarter])
```

## Advanced Analytics

### Customer Segmentation
```dax
High Value Customers = 
CALCULATE(
    [Unique Customers],
    FILTER(
        SUMMARIZE(Sales, Sales[Customer ID], "Customer Revenue", [Total Revenue]),
        [Customer Revenue] > 1000
    )
)

Customer Lifetime Value = 
DIVIDE(
    [Total Revenue],
    [Unique Customers]
)

Member vs Normal Revenue = 
CALCULATE(
    [Total Revenue],
    Sales[Customer Type] = "Member"
) - 
CALCULATE(
    [Total Revenue],
    Sales[Customer Type] = "Normal"
)
```

### Product Analysis
```dax
Top Product Line = 
CALCULATE(
    FIRSTNONBLANK(
        TOPN(1, 
            SUMMARIZE(Sales, Sales[Product Line], "Revenue", [Total Revenue]),
            [Revenue], DESC
        ),
        Sales[Product Line]
    )
)

Product Performance Rank = 
RANKX(
    ALL(Sales[Product Line]),
    [Total Revenue],
    ,
    DESC
)

Above Average Products = 
COUNTROWS(
    FILTER(
        SUMMARIZE(Sales, Sales[Product Line], "Revenue", [Total Revenue]),
        [Revenue] > [Total Revenue] / DISTINCTCOUNT(Sales[Product Line])
    )
)
```

### Branch Analysis
```dax
Best Performing Branch = 
CALCULATE(
    FIRSTNONBLANK(
        TOPN(1, 
            SUMMARIZE(Sales, Sales[Branch], "Revenue", [Total Revenue]),
            [Revenue], DESC
        ),
        Sales[Branch]
    )
)

Branch Market Share = 
DIVIDE(
    [Total Revenue],
    CALCULATE([Total Revenue], ALL(Sales[Branch]))
)

Branch vs Average = [Total Revenue] - DIVIDE([Total Revenue], DISTINCTCOUNT(Sales[Branch]))
```

### Payment Method Analysis
```dax
Digital Payment % = 
DIVIDE(
    CALCULATE([Total Revenue], Sales[Payment] IN {"Ewallet", "Credit Card"}),
    [Total Revenue]
)

Cash Transaction % = 
DIVIDE(
    CALCULATE([Total Revenue], Sales[Payment] = "Cash"),
    [Total Revenue]
)

Most Popular Payment = 
CALCULATE(
    FIRSTNONBLANK(
        TOPN(1, 
            SUMMARIZE(Sales, Sales[Payment], "Revenue", [Total Revenue]),
            [Revenue], DESC
        ),
        Sales[Payment]
    )
)
```

## Conditional Formatting

### Status Indicators
```dax
Revenue Status = 
SWITCH(
    TRUE(),
    [YoY Growth %] > 0.1, "Excellent",
    [YoY Growth %] > 0.05, "Good",
    [YoY Growth %] > 0, "Fair",
    "Poor"
)

Performance Color = 
SWITCH(
    [Revenue Status],
    "Excellent", "Green",
    "Good", "Yellow",
    "Fair", "Orange",
    "Red"
)

KPI Trend = 
IF([YoY Growth %] > 0, "↗", "↘")
```

### Alerts and Thresholds
```dax
Low Inventory Alert = 
IF([Current Stock] < [Reorder Point], "⚠ Low Stock", "")

High Performance Branch = 
IF([Branch Market Share] > 0.35, "🏆 Top Performer", "")

Customer Satisfaction Alert = 
IF([Average Rating] < 6.5, "📉 Below Target", "")
```

## Dynamic Titles and Labels

### Dynamic Chart Titles
```dax
Revenue Chart Title = 
"Total Revenue: " & FORMAT([Total Revenue], "$#,##0")

Selected Period Title = 
"Analysis Period: " & 
MIN(Sales[Date]) & " to " & MAX(Sales[Date])

Dynamic KPI Label = 
"Revenue Growth: " & 
FORMAT([YoY Growth %], "0.0%") & 
" vs Previous Year"
```

### Contextual Measures
```dax
Filtered Context Info = 
"Showing " & [Total Transactions] & " transactions" &
IF(
    HASONEFILTER(Sales[Branch]),
    " for Branch " & SELECTEDVALUE(Sales[Branch]),
    " across all branches"
)

Selection Summary = 
"Current Selection: " &
CONCATENATEX(
    FILTERS(Sales[Product Line]),
    Sales[Product Line],
    ", "
)
```

## Performance Optimization

### Optimized Calculations
```dax
-- Use SUMX for complex calculations
Revenue with Tax Calculation = 
SUMX(
    Sales,
    Sales[Unit Price] * Sales[Quantity] * 1.05
)

-- Use CALCULATE for context modification
Branch A Revenue = CALCULATE([Total Revenue], Sales[Branch] = "A")

-- Use DIVIDE to handle division by zero
Safe Percentage = DIVIDE([Numerator], [Denominator], 0)
```

### Variables for Performance
```dax
Complex Calculation = 
VAR TotalRev = [Total Revenue]
VAR TotalCost = [Total COGS]
VAR Margin = TotalRev - TotalCost
VAR MarginPercent = DIVIDE(Margin, TotalRev)
RETURN
    IF(MarginPercent > 0.3, "High Margin", "Standard Margin")
```

## Usage Notes

### Best Practices
1. Always use DIVIDE() instead of / to avoid division by zero errors
2. Use VAR statements for complex calculations to improve performance
3. Apply proper formatting using FORMAT() function
4. Use ALL() carefully to remove filters when needed
5. Test time intelligence functions with different date selections

### Common Patterns
- Use CALCULATE() to modify filter context
- Use SUMX() for row-by-row calculations
- Use FILTER() for complex conditional logic
- Use RELATED() for lookups across relationships
- Use CONCATENATEX() for text aggregations

### Performance Tips
- Minimize use of calculated columns in large datasets
- Use measures instead of calculated columns when possible
- Avoid complex DAX in visual-level filters
- Use proper data types for optimal performance
- Consider using aggregation tables for large datasets
"""

# Save the DAX formulas to a file
with open('dax_formulas_reference.md', 'w') as f:
    f.write(dax_formulas)

print("DAX Formulas Reference Created!")
print("\nFile Contents Preview:")
print(dax_formulas[:1000] + "...")

# Create a simple summary of what we've built
project_summary = {
    "Dataset": "1,200 supermarket transactions with 17 attributes",
    "Key Metrics": {
        "Total Revenue": "$385,522.02",
        "Total Gross Income": "$127,724.25", 
        "Average Transaction": "$321.27",
        "Top Branch": "Branch B (Los Angeles)",
        "Best Product Line": "Fashion Accessories"
    },
    "Visualizations Created": [
        "Branch Performance Bar Chart",
        "Product Line Revenue Analysis", 
        "Monthly Sales Trend Line Chart"
    ],
    "Files Generated": [
        "supermarket_sales_data.xlsx",
        "project-report.md", 
        "dax_formulas_reference.md",
        "summary_analytics.txt"
    ]
}

print(f"\n\nProject Summary:")
for key, value in project_summary.items():
    print(f"{key}: {value}")