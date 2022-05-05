import time
import requests
import pandas as pd

urls = [
'https://blockchain.info/charts/market-price',
'https://blockchain.info/charts/total-bitcoins',
'https://blockchain.info/charts/market-cap',
'https://blockchain.info/charts/trade-volume',
'https://blockchain.info/charts/blocks-size',
'https://blockchain.info/charts/avg-block-size',
'https://blockchain.info/charts/n-orphaned-blocks',
'https://blockchain.info/charts/n-transactions-per-block',
'https://blockchain.info/charts/median-confirmation-time',
'https://blockchain.info/charts/hash-rate',
'https://blockchain.info/charts/difficulty',
'https://blockchain.info/charts/miners-revenue',
'https://blockchain.info/charts/transaction-fees',
'https://blockchain.info/charts/cost-per-transaction-percent',
'https://blockchain.info/charts/cost-per-transaction',
'https://blockchain.info/charts/n-unique-addresses',
'https://blockchain.info/charts/n-transactions',
'https://blockchain.info/charts/n-transactions-total',
'https://blockchain.info/charts/n-transactions-excluding-popular',
'https://blockchain.info/charts/n-transactions-excluding-chains-longer-than-100',
'https://blockchain.info/charts/output-volume',
'https://blockchain.info/charts/estimated-transaction-volume',
'https://blockchain.info/charts/estimated-transaction-volume-usd'
]

suffix_to_add = '?timespan=8years&format=csv'

def get_btc_data():
    counter = 0
    for url in urls:
        header = ['Date', "btc_" + url.split("/")[-1].replace("-","_")]
        print(header[-1])
        temp_df = pd.read_csv(url+suffix_to_add, header=None, names=header)
        if counter == 0:
            df = temp_df.copy()
        else:
            df = pd.merge(df, temp_df, on="Date", how="left")
        print(temp_df.shape, df.shape)
        counter += 1
        time.sleep(1)
    df.to_csv("../input_v9/bitcoin_dataset.csv", index=False)
    
get_btc_data()