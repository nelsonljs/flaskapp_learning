import pandas as pd

usefulkeys = ['longBusinessSummary','sector','fullTimeEmployees','website','industry','longName','symbol','logo_url'
             ]

usefulMetrics = ['previousClose','twoHundredDayAverage','fiftyDayAverage','regularMarketDayHigh','averageVolume10days','volume',
                 'beta','trailingPE','marketCap','priceToSalesTrailing12Months','profitMargins','enterpriseToEbitda','52WeekChange','forwardEps',
                 'trailingEps','priceToBook','shortPercentOfFloat','shortRatio'
                ]

def createdf(stockinfo):
    #Get Info DF
    metric = []
    value = []

    for item in usefulMetrics:
        try:
            value.append(stockinfo[item])
            metric.append(item)
        except KeyError:
            print(item + ' not in stockinfo.')
            continue

    infodf = pd.DataFrame({'Metric':metric, 'Value':value})

    return infodf
    ###########
