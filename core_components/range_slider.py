import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Range Slider'),
    dcc.RangeSlider(
        id='range_slider',
        marks={i: f'{i}' for i in range(30)},
        min=0,
        max=30,
        value=[20, 25],
        step=1,
    ),
    html.Div(id='solution', style={'margin-top': 20})
])

@app.callback([Output('solution', 'children')],
              [Input('range_slider', 'value')])
def display_value(value):
    return [f'You have selected from range {value[0]} to {value[1]}']

app.run_server()