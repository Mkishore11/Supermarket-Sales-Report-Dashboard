import plotly.graph_objects as go
import plotly.io as pio

# Data from the provided JSON
data = {
    "product_lines": [
        {"Product_Line": "Fashion Accessories", "Revenue": 67564.27},
        {"Product_Line": "Food and Beverages", "Revenue": 65929.88},
        {"Product_Line": "Sports and Travel", "Revenue": 64691.60},
        {"Product_Line": "Health and Beauty", "Revenue": 63679.94},
        {"Product_Line": "Home and Lifestyle", "Revenue": 61927.08},
        {"Product_Line": "Electronic Accessories", "Revenue": 61729.25}
    ]
}

# Extract data for chart
product_lines = [item["Product_Line"] for item in data["product_lines"]]
revenues = [item["Revenue"] for item in data["product_lines"]]

# Abbreviate product line names to meet 15 character limit
abbreviated_lines = []
for line in product_lines:
    if len(line) <= 15:
        abbreviated_lines.append(line)
    else:
        if line == "Fashion Accessories":
            abbreviated_lines.append("Fashion Access.")
        elif line == "Food and Beverages":
            abbreviated_lines.append("Food & Beverage")
        elif line == "Sports and Travel":
            abbreviated_lines.append("Sports & Travel")
        elif line == "Health and Beauty":
            abbreviated_lines.append("Health & Beauty")
        elif line == "Home and Lifestyle":
            abbreviated_lines.append("Home & Lifestyle")
        elif line == "Electronic Accessories":
            abbreviated_lines.append("Electronic Acc.")

# Format revenue values with 'k' abbreviation
formatted_revenues = [f"${rev/1000:.1f}k" for rev in revenues]

# Brand colors
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C']

# Create horizontal bar chart
fig = go.Figure(go.Bar(
    x=revenues,
    y=abbreviated_lines,
    orientation='h',
    marker=dict(color=colors[:len(revenues)]),
    text=formatted_revenues,
    textposition='outside',
    cliponaxis=False,
    hovertemplate='<b>%{y}</b><br>Revenue: $%{x:,.0f}<extra></extra>'
))

# Update layout
fig.update_layout(
    title='Product Line Revenue Performance',
    xaxis_title='Revenue ($k)',
    yaxis_title='Product Lines'
)

# Update axes
fig.update_xaxes(
    tickformat='.0f',
    ticksuffix='k',
    tickvals=[revenue for revenue in revenues],
    ticktext=[f'{rev/1000:.0f}k' for rev in revenues]
)

# Save the chart
fig.write_image('product_line_revenue_chart.png')