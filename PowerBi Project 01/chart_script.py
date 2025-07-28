import plotly.graph_objects as go

# Data for branch performance - sorted in descending order by revenue
branches = ['B', 'C', 'A']
revenues = [142281.48, 123299.25, 119941.29]

# Create horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=branches,
    x=revenues,
    orientation='h',
    marker_color=['#1FB8CD', '#DB4545', '#2E8B57'],
    text=[f'${rev/1000:.1f}k' for rev in revenues],
    textposition='auto',
    cliponaxis=False
))

fig.update_layout(
    title='Branch Revenue Performance',
    xaxis_title='Revenue ($)',
    yaxis_title='Branch'
)

fig.update_xaxes(
    tickformat='$,.0f'
)

# Save the chart
fig.write_image('branch_performance_chart.png')