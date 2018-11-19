#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
import numpy as np

ts.set_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
pro = ts.pro_api()

if __name__ == '__main__':
    #Part1数据选择
    # df = pro.bo_monthly(date='20181001')
    # print(df)
    # print(df['name'])
    # print(df[1:3])

    # print(df.loc[0:2,'avg_price':'p_pc'])
    # print(df.loc[0,'name'])
    # print(df.loc[[1,7],['name','rank']])

    # print(df.at[1,'name'])

    # print(df.iloc[1])
    # print(df.iloc[1:3,1:3])
    # print(df.iat[1,1])
    # print(df.head(3))

    #Part2计数统计
    # df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv',encoding='utf-8') #or gbk
    # print(df)
    # rank_df  = df[df['rank']<6]
    # rank_count = rank_df['rank'].value_counts()
    # rank_sum = rank_df['month_amount'].sum()
    # print(rank_df)
    # print(rank_count[2])
    # print(rank_sum)

    #Part3 数据分组处理
    # name_group = df.groupby('name')
    # print(name_group.sum())
    # print(name_group.groups)
    # print(name_group.get_group('侏罗纪世界2'))
    # print(name_group.get_group('侏罗纪世界2').loc[:, 'month_amount'])
    # name_group = df.groupby(['list_date','name'])
    # print(name_group.first())
    # print(name_group.last())

    # print(name_group['month_amount'].agg([np.sum,np.mean,np.std]))
    # print(name_group['month_amount'].agg({'总和':np.sum, '平均':np.mean, '标准差':np.std}))
    # print(name_group.size())
    # print(name_group.describe())

    #Part4 查看数据
    # print(df.dtypes)
    # print(df.head())
    # print(df.tail())
    # print(df.index)
    # print(df.columns)
    # print(df.values)
    # print(df.T)
    # print(df.sort_index())
    # print(df.sort_values(by='rank'))

    #Part5 筛选数据
    # print(df['name'][(df['rank']<2)&(df['rank']>0)|(df['wom_index']>7)])
    # wom_list = [7.86,8.13,6.1]
    # print(df['wom_index'].isin(wom_list))
    # print(df['name'][df['wom_index'].isin(wom_list)==True])


    #Part6：增删
    # df['who'] = pd.Series(np.random.randn(110),index=df.index)
    # df.insert(len(df.columns),'who',np.random.randn(110))

    # del df['who']

    # print(df.drop([1]))
    # print(df.drop(['who','rank'],axis=1))

    #Part7缺失值处理
    # df = pd.DataFrame(np.random.randn(4,3), index=list("abcd"), columns=['one','two','three'])
    # df.iloc[1,:-1] = np.nan
    # df.iloc[1:-1,2] = np.nan

    # print(df.fillna(0))
    # print(df.fillna(method='pad'))
    # print(df.fillna(method='bfill',limit=1))
    # print(df.fillna(df.mean()['one':'two']))
    # print(df.fillna)

    # print(df.interpolate())

    # print(df.dropna())
    # print(df.dropna(axis=1))

    # df = pd.DataFrame({'a':[1,2,3,4],'b':[2,6,7,8]})
    # print(df)
    # print(df.replace(2,20))
    # print(df['a'].replace([1,3],[99,100]))





