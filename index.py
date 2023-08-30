import dash
from dash.dependencies import Input, Output
from dash import dcc, html
# import dash_auth


app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    html.Div(
        # style={width: "100%"},
        dcc.Input(id="user", type="text", placeholder="Enter Username", className="inputbox1",
                  ),

    ),
    html.Div(
        dcc.Input(id="passw", type="text", placeholder="Enter Password", className="inputbox2",
                  ),
    ),

    html.Div(
        html.Button('Verify', id='verify', n_clicks=0, )),
    html.Div(id='output1')
])


@app.callback(
    Output('output1', 'children'),
    [Input('verify', 'n_clicks')],
    [Input('user', 'value'),
     Input('passw', 'value')])

def update_output(n_clicks, uname, passw):
    li = {'princewill': 'princewill'}
    if uname == '' or uname == None or passw == '' or passw == None:
        return html.Div(children='', )
    if uname not in li:
        return html.Div(children='Incorrect Username', )
    if li[uname] == passw:
        return html.Div(dcc.Link('Access Granted!', href='/next_page', ), )
    else:
        return html.Div(children='Incorrect Password', )


next_page = html.Div([
    html.Div(dcc.Link('Log out', href='/')),
    html.H1(children="This is the Next Page, the main Page", className="ap", )])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/next_page':
        return next_page
    else:
        return index_page


if __name__ == '__main__':
    app.run_server()
