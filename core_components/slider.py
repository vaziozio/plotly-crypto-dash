import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Square root slider graph'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "black", "color": "white"}),
    dcc.Slider(
        id="slider-updatemode",
        marks={i: f'{i}' for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag'
    ),
    html.Div(id="updatemode-output-container", style={'margin-top': 20})
])

@app.callback(
    [Output('slider-graph', 'figure'), Output('updatemode-output-container', 'children')],
    [Input('slider-updatemode', 'value')]
)
def display_value(value):
    x = []
    for i in range(value+1):
        x.append(i)

    y=[]
    for i in range(value+1):
        y.append(i*i)

    graph= go.Scatter(
        x=x,
        y=y,
        name="Manipulate Graph"
    )
    layout = go.Layout(
        paper_bgcolor="#27293d",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white')
    )
    return {'data': [graph], 'layout': layout}, f'Value: {round(value, 1)} Square: {value*value}'


if __name__=='__main__':
    app.run_server(debug=True)