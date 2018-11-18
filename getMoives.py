#!/usr/bin/env python3
import tushare as ts
import os
import datetime

ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
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
        # 全年电影数据输出到csv文件
        df = pro.bo_monthly(date=fulldate)
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=False)
        else:
            df.to_csv(filename)

if __name__ == '__main__':
    getMovies()
