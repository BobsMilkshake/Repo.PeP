import pandas as pd
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv('Accelerometer.csv')
df.index = pd.to_datetime(df['time'], unit = 'ns')

max_data = df['x'].max(axis=0)

fig = go.Figure()

for axis in ['x', 'y', 'z']:
    fig.add_trace(go.Scatter(x = df.index, y = df[axis], name = axis))

fig.show()