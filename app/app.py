
import requests
import dash
import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

#most layouts copied from the basic examples from https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/ for the sake of speed

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.Container([
                dbc.Card([
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
    ], className="justify-content-center center-block text-center",
)

#make a callback
def register_callbacks(app):
    from config import basevars
    @app.callback(
        Output('result', 'children'),
        Input('btn1', 'n_clicks'),
        State('input1','value')
    )
    def calculate(n, val):
    pass
