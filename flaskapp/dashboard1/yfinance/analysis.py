import yfinance as yf
import json
import pandas as pd
import numpy as np
from flask import jsonify
import plotly
import plotly.express as px

stock_ticker = "AMZN"
terminology = {'Buy':['Strong Buy', 'Buy','Outperform','Overweight','Positive','Market Outperform'],
              'Neutral':['Neutral','Hold','Market Perform','Equal-Weight','Sector Perform','Peer Perform','In-Line','Perform','Sector Weight'],
              'Sell':['Strong Sell', 'Reduce','Sell','Underperform','Negative','Underweight']}
# Useful keys
def plotanalystpie(stock_ticker_recommendations):
    mydf = stock_ticker_recommendations.drop_duplicates(keep='last', subset = ["Firm"])
    mydf = mydf['2016':]
    conditions = [
        (mydf["To Grade"].isin(terminology['Buy'])),
        (mydf["To Grade"].isin(terminology['Neutral'])),
        (mydf["To Grade"].isin(terminology['Sell'])),

    ]
    choices = ["Buy", "Neutral", "Sell"]

    mydf['Ratings'] = np.select(conditions, choices)

    import plotly.express as px
    # This dataframe has 244 lines, but 4 distinct values for `day`
    fig = px.pie(mydf[mydf['Ratings']!='0'], names='Ratings', color='Ratings',
                 color_discrete_map={'Buy':'seagreen',
                                     'Neutral':'lemonchiffon',
                                     'Sell':'red'},
                title = "Analyst Recommendations (Total: {})".format(mydf[mydf['Ratings']!='0'].shape[0]), height = 300)
    return fig

def plotYTDperformance(stock_ticker):
    data = yf.download(
        tickers = "SPY ^IXIC " + stock_ticker,
        period = "ytd",
        interval = "1d",
    )
    stockdata = data['Close']
    # Get start of year values
    SOY_SPY = stockdata['SPY']['2020-01-02']
    SOY_IXIC = stockdata['^IXIC']['2020-01-02']
    SOY_stock = stockdata[stock_ticker]['2020-01-02']

    stockdata['percentSPY']=stockdata['SPY']/SOY_SPY-1
    stockdata['percentNASDAQ']=stockdata['^IXIC']/SOY_IXIC-1
    stockdata['percentstock']=stockdata[stock_ticker]/SOY_stock-1
    fig = px.line(stockdata, x= stockdata.index, y = ['percentSPY','percentNASDAQ','percentstock'],
                  title='{0} YTD performance vs indices'.format(stock_ticker), range_x=[stockdata.index[0],stockdata.index[-1]])

    fig.add_annotation(x=stockdata.index[-1], y=stockdata['percentSPY'][-1], text="SPY YTD Performance: {:.2%}".format(stockdata['percentSPY'][-1]))
    fig.add_annotation(x=stockdata.index[-1], y=stockdata['percentNASDAQ'][-1], text="NASDAQ YTD Performance: {:.2%}".format(stockdata['percentNASDAQ'][-1]))
    fig.add_annotation(x=stockdata.index[-1], y=stockdata['percentstock'][-1], text="{0} YTD Performance: {1:.2%}".format(stock_ticker, stockdata['percentstock'][-1]))
    fig.update_traces(hovertemplate='Date: %{x} <br>YTD Performance: %{y:.2%}')
    fig.update_xaxes(showspikes=True)
    fig.update_yaxes(showspikes=True, title = 'YTD Performance %')
    fig.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Rockwell"
        ), showlegend=False
    )

    return fig

def getinfo(stock_ticker):
    stock = yf.Ticker(stock_ticker)
    mydict = stock.info
    fig = plotanalystpie(stock.recommendations)
    ytdfig = plotYTDperformance(stock_ticker)
    pieJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    ytdJSON = json.dumps(ytdfig, cls=plotly.utils.PlotlyJSONEncoder)
    mydict['piejson'] = pieJSON
    mydict['ytdjson'] = ytdJSON

    try:
        return json.dumps(mydict)
    except ValueError:
        return json.dumps(mydict)
    ###########

my_json = json.loads(getinfo(stock_ticker))

from .createdf import createdf
infodf = createdf(my_json)
