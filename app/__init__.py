import dash
import dash_bootstrap_components as dbc
from app.app import layout
from app.app import register_callbacks
from config import basevars

# Meta tags for viewport responsiveness
meta_viewport = {'name': 'viewport',
                     'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}
stylesheet = [dbc.themes.LUX]

def create_app():
    app = dash.Dash(__name__,
                         title="My Title",
                         external_stylesheets=stylesheet,
                         suppress_callback_exceptions=True,
                         url_base_pathname='/dashboard/',
                         meta_tags=[meta_viewport])
    app.layout = layout
    register_callbacks(app)
    return app
