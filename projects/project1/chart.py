from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='initial value', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    return f'You have entered {value}'

if __name__ == '__main__':
    app.run_server(debug=True)