from dash.dependencies import Input, Output
import datetime
import json
from .yfinance.utils import valid_tickers
import plotly.graph_objects as go

def register_callbacks(app):
    @app.callback(Output('updating_datetime', 'children'),
                  [Input('interval-component', 'n_intervals')])
    def update_metrics(n):
        return datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')

    @app.callback(Output("ticker_output", "children"),
                    [Input("ticker_input", "value")])
    def output_text(value):
        return "Searching for info on " + value

#### Check validity of Ticker
    @app.callback(
        [Output("ticker_input", "valid"), Output("ticker_input", "invalid")],
        [Input("ticker_input", "value")],
    )
    def check_validity(text):
        if text:
            is_gmail = text in valid_tickers
            return is_gmail, not is_gmail
        return False, False

#### Storing the return as an intermediate value for usage later
    @app.callback(
    Output("intermediate-value", "children"),
    [Input("get_info", "n_clicks"),
    Input("ticker_input", "value")]
    )
    def on_button_click(n, ticker_input):
        from .yfinance.analysis import getinfo
        return(getinfo(ticker_input))

#### Updating all items on the page on button click (intermediate_value is updated)
    @app.callback(
    Output("jumbo-image", "src"),
    [Input("intermediate-value", "children")]
    )
    def update_jumbo_image(input):
        myfile = json.loads(input)
        return(myfile['logo_url'])

    @app.callback(
    Output("jumbo1", "children"),
    [Input("intermediate-value", "children")]
    )
    def update_jumbo1(input):
        myfile = json.loads(input)
        return(myfile['longName'])

    @app.callback(
    Output("jumbo2", "children"),
    [Input("intermediate-value", "children")]
    )
    def update_jumbo2(input):
        myfile = json.loads(input)
        return(myfile['sector'])

    @app.callback(
    Output("jumbo3", "children"),
    [Input("intermediate-value", "children")]
    )
    def update_jumbo3(input):
        myfile = json.loads(input)
        return(myfile['longBusinessSummary'])

    @app.callback(
    Output("stock_infotable", "data"),
    [Input("intermediate-value", "children")]
    )
    def update_infotable(input):
        myfile = json.loads(input)

        from .yfinance.createdf import createdf
        mydf = createdf(myfile)
        return(mydf.to_dict('records'))

    @app.callback(
    Output("analyst_recommendations_pie", "figure"),
    [Input("intermediate-value", "children")]
    )
    def update_analystpie(input):
        myfile = json.loads(input)
        fig = go.Figure(json.loads(myfile['piejson']))

        return fig

    @app.callback(
    Output("ytd_performance_line", "figure"),
    [Input("intermediate-value", "children")]
    )
    def update_analystpie(input):
        myfile = json.loads(input)
        fig = go.Figure(json.loads(myfile['ytdjson']))

        return fig
