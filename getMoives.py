#!/usr/bin/env python3
import tushare as ts
import os
import datetime

ts.set_token('9e14c4447f059759bd6be7e03109d6acdcd03e983076b7448013fb49')
pro = ts.pro_api()

filename = '/Users/fseeeye/Desktop/movies.csv'
def getMovies():
    for month in range(1,datetime.datetime.now().month):
        # 规格化处理年月日为YYYYMM01
        month = str(month)
        fulldate = str(datetime.datetime.now().year)
        if len(month) == 1:
            month = "0" + month
        fulldate += month + "01"

        df = pro.bo_monthly(date=fulldate)
        print(os.path.exists(filename))
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=False)
        else:
            df.to_csv(filename)

if __name__ == '__main__':
    getMovies()
