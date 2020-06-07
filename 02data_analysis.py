import sys
import os
import math
from pylab import mpl,plt
import numpy as np
import glob
import pandas as pd
from argparse import ArgumentParser

# plot 
plt.style.use("seaborn")
mpl.rcParams["font.family"] = "serif"


# DIR
DIR_HOME = os.getcwd() + os.sep + ".."
DIR_CSV = DIR_HOME + os.sep + "csv"

# constants

def getoption():
    argparser = ArgumentParser()
    argparser.add_argument('-d', '--debug', type=bool, default=False, help='debug mode')
    return argparser.parse_args()


def load_data(dir, args):
    # if debug mode is true , then we load few data 
    if args.debug:
        file_names = glob.glob(dir + os.sep +"*.csv")[0:1]
    else:
        file_names = glob.glob(dir + os.sep + "*.csv")
    stock_data = []
    for file_name in file_names:
        ticker = file_name.split('/')[-1][:-4] #file_nameからtickerを抽出
        data = pd.read_csv(file_name, index_col=0, usecols=['Date','Adj Close']) #調整済み終値だけ抽出
        data = data.rename(columns={'Adj Close':ticker}) #列名をtickerに変更
        stock_data.append(data)
    stock_data = pd.concat(stock_data, axis=1, join='inner') #innerで共通のindexをもつものだけ抽出

    return stock_data
        
def print_statistics(data):
    print(data.info())
    (data/data.iloc[0]*100).plot(figsize=(10,6)) #最初の日からの変動率をプロット
    plt.show()
    plt.close()
    log_returns = np.log(data / data.shift(1))
    print(log_returns.head)
    log_returns.hist(bins=50, figsize=(10,8))
    plt.show()
    
def main(argv):
    args = getoption()
    if args.debug :
        for i in range(10):
            print("------DEBUG MODE-------")
    stock_data = load_data(DIR_CSV, args)
    print_statistics(stock_data)
if __name__ == '__main__':
    main(sys.argv) 
