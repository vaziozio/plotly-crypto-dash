import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import requests, base64
from io import BytesIO

app = dash.Dash()

def encode_image(image_url):
    buffered = BytesIO(requests.get(image_url).content)
    image_base64 = base64.b64encode(buffered.getvalue())
    return b'data:image/png;base64,' + image_base64

app.layout = html.Div([
    dcc.Dropdown(id='dropdown', 
                 options=[
                    {'label': 'Response 200', 'value': 'ok'},
                    {'label': 'Response 300', 'value': 'multiple'},
                    {'label': 'Response 400', 'value': 'bad'}
                 ],
                    value='ok',
                    placeholder='Select a Response'
                 ),
            html.Div(id="output-container")
])

@app.callback(
    Output("output-container", "children"),
    [Input('dropdown', 'value')])
def update_output(value):

    selected_image = encode_image('https://httpstatusdogs.com/img/100.jpg')

    if value == 'ok':
        selected_image = encode_image('https://httpstatusdogs.com/img/200.jpg')
    elif value == 'multiple':
        selected_image = encode_image('https://httpstatusdogs.com/img/300.jpg')
    elif value == 'bad':
        selected_image = encode_image('https://httpstatusdogs.com/img/400.jpg')
    return html.Div(html.Img(src=selected_image.decode(), style={'width': '500px'}))

if __name__=='__main__':
    app.run_server(debug=True)