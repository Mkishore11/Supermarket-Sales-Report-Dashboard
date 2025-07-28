import plotly.graph_objects as go
import pandas as pd

# Create dataframe from the provided data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Revenue": [37576.81, 25842.76, 31640.24, 26444.36, 31545.66, 33837.89, 27134.22, 36094.59, 33450.31, 36938.04, 37404.94, 27612.20]
}

df = pd.DataFrame(data)

# Convert revenue to thousands for display
df['Revenue_k'] = df['Revenue'] / 1000

# Create line chart with markers
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Month'],
    y=df['Revenue_k'],
    mode='lines+markers',
    name='Revenue',
    line=dict(color='#1FB8CD', width=3),
    marker=dict(color='#1FB8CD', size=8),
    hovertemplate='%{x}<br>$%{y:.1f}k<extra></extra>',
    cliponaxis=False
))

# Update layout
fig.update_layout(
    title='2024 Monthly Sales Trend',
    xaxis_title='Month',
    yaxis_title='Revenue ($k)',
    showlegend=False
)

# Save the chart
fig.write_image("monthly_sales_trend.png")