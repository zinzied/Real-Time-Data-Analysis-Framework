import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from calculations import revenue_per_industry
from datetime import datetime

def create_dashboard():
    # Get the data
    revenue_data = revenue_per_industry()
    
    # Sort and get top 25
    top_25_revenue_data = revenue_data.sort_values(ascending=False).head(25)
    
    # Calculate key metrics
    total_revenue = revenue_data.sum()
    avg_revenue = revenue_data.mean()
    median_revenue = revenue_data.median()
    
    # Create an interactive bar chart using Plotly
    fig = go.Figure(data=[
        go.Bar(
            x=top_25_revenue_data.index,
            y=top_25_revenue_data.values,
            text=top_25_revenue_data.values,
            textposition='auto',
        )
    ])
    
    # Customize layout
    fig.update_layout(
        title={
            'text': f'Revenue Analysis Dashboard (Updated: {datetime.now().strftime("%Y-%m-%d %H:%M")})',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Industry",
        yaxis_title="Revenue ($)",
        template="plotly_white",
        annotations=[
            dict(
                text=f"Total Revenue: ${total_revenue:,.2f}<br>"
                     f"Average Revenue: ${avg_revenue:,.2f}<br>"
                     f"Median Revenue: ${median_revenue:,.2f}",
                showarrow=False,
                xref="paper",
                yref="paper",
                x=1.1,
                y=0.5
            )
        ]
    )
    
    # Add hover information
    fig.update_traces(
        hovertemplate="Industry: %{x}<br>Revenue: $%{y:,.2f}<extra></extra>"
    )
    
    # Rotate x-axis labels for better readability
    fig.update_xaxes(tickangle=45)
    
    # Add a trend line
    fig.add_trace(go.Scatter(
        x=top_25_revenue_data.index,
        y=top_25_revenue_data.values.mean() * np.ones_like(top_25_revenue_data.values),
        name='Average',
        line=dict(color='red', dash='dash')
    ))
    
    # Export to HTML for sharing
    fig.write_html("revenue_dashboard.html")
    
    # Show the plot
    fig.show()

if __name__ == "__main__":
    create_dashboard()
