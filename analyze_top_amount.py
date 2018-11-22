#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 票房最高的电影Top10
import pandas as pd
from pyecharts import Bar

def draw_Bar(df):
    names = []
    month_amounts = []
    for name in df['name'].values.tolist():
        names.append(name)
    for month_amount in df['month_amount'].values.tolist():
        month_amounts.append(month_amount)
    bar = Bar("票房最高的电影Top10")
    bar.add("票房", names, month_amounts, is_more_utils=True, xaxis_rotate=20, is_label_show=True) #axis_rotate标签角度 labelshow显示柱形数字
    bar.render(path="amounts.html")
    print("Complete!")

if __name__ == '__main__':
    df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv', encoding='utf-8')  # or gbk
    amount_group = df.groupby(by='name',as_index=False)['month_amount'].sum()
    amount_group = amount_group.sort_values(by='month_amount',ascending=False)
    movie_top10 = amount_group.head(10)

    draw_Bar(movie_top10)
