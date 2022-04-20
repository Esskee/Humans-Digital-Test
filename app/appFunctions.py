import dash
import pandas as pd
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

class Corefunc():
    def __init__(self):
        # sidebar style taken from Adam of charmingData

        self.SIDEBAR_STYLE = {
            "position": "fixed",
            "top": 0,
            "left": 0,
            "bottom": 0,
            "width": "18rem",
            "padding": "2rem 1rem",
            "background-color": "#f8f9fa",
        }
        # padding for the page content
        self.CONTENT_STYLE = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }


class Layout_Templates(Corefunc):
    def Sidebar(self):
        return html.Div(
            [
                html.H2("Sidebar", className="display-4"),
                html.Hr(),
                html.P(
                    "Telegram Social Campaign", className="lead"
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("Page 1", href="/page-1", active="exact"),
                        dbc.NavLink("Page 2", href="/page-2", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            style=self.SIDEBAR_STYLE,
        )

    def Body(self):
        return html.Div(id="page-content", children=[], style=self.CONTENT_STYLE)

    def Social_Line(self, df):
        data = px.line(summary, x='Time', y="Users", color='Type',
                                     template='plotly_white', hover_name='User',
                                     color_discrete_sequence=px.colors.qualitative.Pastel2)
        data.update_layout(showlegend=True, legend=dict(orientation="h",
                                                                      yanchor="top",
                                                                      y=0.99,
                                                                      xanchor="left",
                                                                      x=0.01))
        return dcc.Graph(id='Socialgraph',
                        figure=data,
                        responsive='auto',
                        config={'displayModeBar': False, 'autosize': False})
