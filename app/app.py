
import requests
import dash
import pandas as pd
from datetime import date
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from app.appFunctions import Layout_Templates, Data_Frame_funcs

content = Layout_Templates()
layout = html.Div([
                dcc.Location(id="URL"),
                content.Sidebar(),
                content.Body()
    ]
)

#callbacks


def register_callbacks(app):
    lay = Layout_Templates()
    data = Data_Frame_funcs()

    @app.callback(
        Output('page-content', 'children'),
        Input('URL', 'pathname'),
    )
    def page_content1(pathname):
        df = data.cat_traces()
        return dbc.Card([
                dbc.CardHeader([
                    dbc.Row([
                        dbc.Col(
                            html.H2('Telegram Social Data')
                            )], justify='center'),
                ]),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col(
                            dbc.InputGroup([
                                dbc.InputGroupText('Date Range'),
                                dcc.DatePickerRange(
                                    start_date=date(2020, 1, 21),
                                    end_date=date(2022, 6, 21),
                                    display_format='MMMM Y, DD',
                                    start_date_placeholder_text='MMMM Y, DD',
                                    id='date_picker'
                                ),
                            ])
                            )], justify='center'),
                    dcc.Loading(dbc.Row([lay.Social_Line(df)], id='graph_div', justify='center'))
                ]),
                dbc.CardFooter(
                    dbc.Row([
                        dbc.Col(
                            html.H6('by James Buck', id='result', style={'text-align': 'center'})
                            )], justify='center'),
                )
                ])

    @app.callback(
        Output('graph_div', 'children'),
        Input('date_picker', 'start_date'),
        Input('date_picker', 'end_date'),
        State('URL', 'pathname')
    )
    def graph_date(start, end, pathname):
        content = []
        if pathname == '/':
            df = data.Line_date_df(start, end)
            content = lay.Social_Line(df)
        elif pathname == '/page1':
            df = data.table_date_df(start, end)
            content = lay.Social_table(df)
        elif pathname == '/page2':
            df = data.table_date_df(start, end)
            content = lay.Word_cloud(df)
        return content
