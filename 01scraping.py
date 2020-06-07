import sys
import os
import datetime
import pandas_datareader.data as web
import time

# DIR
DIR_HOME = os.getcwd() + os.sep + ".."
DIR_CSV = DIR_HOME + os.sep + "csv"

# constants
TICKER_LIST = [] #取得するTicker ここだけ変更
SOURCE = "yahoo" 
START = "2010.05.31" #開始日
END = "2020.05.31" # 終了日


def download_stock_data(ticker, source, start, end):
    filename = os.path.expanduser(DIR_CSV + os.sep +ticker+'.csv')
    data = web.DataReader(ticker, source, start, end)
    data.to_csv(filename)
def main(argv):
    os.makedirs(DIR_CSV, exist_ok=True) #出力先のフォルダを作成
    for ticker in TICKER_LIST:
        download_stock_data(ticker, SOURCE, START, END)
        time.sleep(30) #30秒待機
if __name__ == '__main__':
    main(sys.argv) 
