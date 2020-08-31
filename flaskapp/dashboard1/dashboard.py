"""Instantiate a Dash app."""
import numpy as np
import pandas as pd
import dash

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    # import os
    # assets_path = os.getcwd() +'/myflaskapp/plotlydash/app_assets'

    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard1/',
        ### if we want to define our own assets_path
        # assets_folder = assets_path,

        ### if you want to use external stylesheets.
        # external_stylesheets=[
        #     '/static/dist/css/styles.css',
        #     'https://fonts.googleapis.com/css?family=Lato'
        #     ]
    )

    # Create Layout
    from .layouts import dash1layout
    dash_app.layout = dash1layout

    # Initialize callbacks
    from .callbacks import register_callbacks
    register_callbacks(dash_app)

    return dash_app.server
