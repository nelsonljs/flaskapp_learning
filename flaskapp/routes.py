"""Routes for parent Flask app."""
from flask import render_template
from flask import current_app as app

from flask import request, jsonify, render_template
from flask_cors import CORS, cross_origin
import json
import plotly
import dash

@app.route('/abc')
def home():
    """Landing page."""
    return render_template(
        'index.jinja2',
        title='Plotly Dash Flask Tutorial',
        description='Embed Plotly Dash into your Flask applications.',
        template='home-template',
        body="This is a homepage served with Flask."
    )


# from .api import api_routes
