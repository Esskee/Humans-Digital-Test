
import requests
import dash
import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app.appFunctions import Layout_Templates

content = Layout_Templates()
layout = html.Div([
                dcc.Location(id="URL"),
                content.Sidebar(),
                content.Body()
    ]
)

#callbacks
def register_callbacks(app):
    @app.callback(
        Output('result', 'children'),
        Input('btn1', 'n_clicks'),
        State('input1','value')
    )
    def calculate(n, val):
        pass

    @app.callback(
        Output('page-content', 'children'),
        Input('URL', 'pathname'),
    )
    def page_content1(pathname):

        if pathname == '/':
            return dbc.Card([
                    dbc.CardHeader([
                        dbc.Row([
                            dbc.Col(
                                html.H2('placeholder')
                        )], justify='center'),
                        dbc.Row([
                            dbc.Col(
                                html.P('by James Buck', className = 'text-muted')
                        )], justify='center'),
                    ]),
                    dbc.CardBody(
                     dbc.Row([
                        dbc.Col(
                                dbc.InputGroup([
                                    dbc.InputGroupText('placeholder'),
                                    dbc.Input(id="input1", placeholder="enter amount", value=100),
                                    dbc.Button('placeholder',id='btn1')
                                ])
                        )], justify='center'),
                    ),
                    dbc.CardFooter(
                        dbc.Row([
                            dbc.Col(
                                html.H6('answer', id='result', style={'text-align':'center'})
                        )], justify='center'),
                    )
                    ])
