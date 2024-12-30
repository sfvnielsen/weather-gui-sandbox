"""
    Minimal main that spawns a webservice locally and shows 
    some dummy data

    Created using Microsoft copilot

    author: sfn
"""

import dash
from dash import html
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
import pandas as pd

# Generate random time series data
np.random.seed(0)
dates = pd.date_range('2023-01-01', periods=100)
data = np.random.randn(100).cumsum()

# Create a plot with Matplotlib
fig, ax = plt.subplots()
ax.plot(dates, data)
ax.set_title('Random Time Series')

# Save the plot to a bytes buffer
buf = io.BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
image_base64 = base64.b64encode(buf.read()).decode('utf-8')

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Random Time Series Plot'),
    html.Img(src=f'data:image/png;base64,{image_base64}')
])

if __name__ == '__main__':
    app.run_server(debug=True)
