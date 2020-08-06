import pandas as pd
import yfinance as yf
import json

aapl = yf.Ticker('aapl')

# print(aapl.info)

stock_list = ['AAPL', 'AMD', 'TSLA']
stock_data = {} # Empty Dictionary

# for stock in stock_list:
#     info = yf.Ticker(stock).info
#     price = info.get('')
#     tEPS = info.get('trailingEps')
#     fEPS = info.get('forwardEps')
#     print(stock, 'Trailing EPS: ' + str(tEPS), 'Forward EPS: ' + str(fEPS))

for stock in stock_list:
    stock_object = yf.Ticker(stock)

    #convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(stock_object.info, orient="index")
    temp.reset_index(inplace=True)
    temp.columns = ["Attribute", "Result"]

    # add (ticker, dataframe) to main dictionary
    stock_data[stock] = temp

# print(stock_data)

combined_data = pd.concat(stock_data)
combined_data = combined_data.reset_index()
del combined_data["level_1"]  # clean up unnecessary column
combined_data.columns = ["Ticker", "Attribute", "Result"]  # update column names

# print(combined_data)

tEPS = combined_data[combined_data["Attribute"] == 'trailingEps'].reset_index()
del tEPS["index"]  # clean up unnecessary column

print(tEPS)

json = tEPS.to_json('stocks.json')
csv = tEPS.to_csv('stocks.csv')
