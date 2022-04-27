import dash
import psycopg2
import pandas as pd
from datetime import date
from sqlalchemy import create_engine
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from config import basevars
import pandas.io.sql as psql
import plotly.express as px
from dash import dash_table
import nltk
from wordcloud import WordCloud

print('Loading in Data from Database')
conn = psycopg2.connect(dbname=basevars.database, user=basevars.user, password=basevars.password,
                        host=basevars.host, port=5432, options='-c search_path=telegram_crawler_demo_access')
#df = pd.read_sql_query("SELECT message_timestamp, message_replies FROM message", con=conn)
df = pd.read_sql_query("SELECT * FROM channel JOIN message ON channel.record_id = message.channel_record_id", con=conn)
df = df[['message_timestamp', 'category', 'messages', 'author', 'message_text']]
for col in df.columns:
    print(col)


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


class Data_Frame_funcs(Corefunc):
    def cat_traces(self):
        dfa = df.sort_values(by='message_timestamp')
        #dfa = df.set_index("message_timestamp")
        #dfa = df
        #dfa = df.groupby('category', 'message_timestamp')['messages'].count()
        return dfa

    def Line_date_df(self, start, end):
        dfa = df[df['message_timestamp'] >= start]
        dfa = dfa[dfa['message_timestamp'] <= end]
        return dfa

    def table_date_df(self, start=date(2020, 1, 21), end=date(2022, 6, 21)):

        dfa = df[df['message_timestamp'] >= start]
        dfa = dfa[dfa['message_timestamp'] <= end]
        return dfa


class Layout_Templates(Corefunc):
    def Sidebar(self):
        return html.Div(
            [
                html.H2("Human Digital", className="display-5"),
                html.Hr(),
                html.P(
                    "Display Options", className="lead"
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("Line", href="/", active="exact"),
                        dbc.NavLink("Table", href="/page1", active="exact"),
                        dbc.NavLink("Cloud", href="/page2", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            style=self.SIDEBAR_STYLE,
        )

    def Body(self):
        return html.Div(id="page-content", children=[], style=self.CONTENT_STYLE)

    def Social_Line(self, df=df):
        data = px.line(df, x='message_timestamp', y='messages', color='category',  # hover_name='author',
                       template='plotly_white',
                       color_discrete_sequence=px.colors.qualitative.Pastel2)
        data.update_layout(showlegend=True, legend=dict(orientation="h",
                                                        yanchor="top",
                                                        y=0.99,
                                                        xanchor="left",
                                                        x=0.01))
        return dcc.Graph(id='Socialgraph',
                         figure=data,
                         responsive='auto',
                         #config={'displayModeBar': False, 'autosize': False}
                         )

    def Word_cloud(self, df):
        # stopwords = nltk.corpus.stopwords.words('english')
        # stopwords = set(stopwords)

        words = []
        for word in df['message_text']:
            words.append(word)
        allwords = " ".join(x for x in words)

        # generate wordcloud from all tweets
        my_wordcloud = WordCloud(
            #stopwords=stopwords,
            background_color='white',
            height=275
        ).generate(allwords)

        # visualize wordcloud inside plotly figure
        fig = px.imshow(my_wordcloud, template='ggplot2')
        fig.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False)

        return dcc.Graph(id='SocialWords',
                         figure=fig,
                         responsive='auto',
                         config={'displayModeBar': False}
                         )

    def Social_table(self, df=df):
        #return dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
        return dash_table.DataTable(
                    columns=[{"name": i, "id": i} for i in df.columns],
                    selected_columns=[],
                    selected_rows=[],
                    page_current=0,
                    page_size=10,
                    data=df.to_dict('records'),
                    style_table={'overflowX': 'auto'},
                    style_cell={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'minWidth': '20px', 'width': '80px', 'maxWidth': '180px'},
                    style_data_conditional=[
                        {'if': {'row_index': 'odd'},
                         'backgroundColor': 'rgb(248, 248, 248)'}],
                    style_header={'backgroundColor': '#ffffff', 'fontWeight': 'bold', 'color': 'black'})
