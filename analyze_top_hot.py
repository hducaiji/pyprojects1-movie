#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 人气最高的电影Top (场均人次)
import pandas as pd
from pyecharts import Bar

def draw_Bar(df):
    names = []
    pcs = []
    for name in df['name'].values.tolist():
        names.append(name)
    for pc in df['p_pc'].values.tolist():
        pcs.append(pc)
    bar = Bar("人气最高的电影Top10")
    bar.add("场均人次", names, pcs, is_more_utils=True, xaxis_rotate=20, is_label_show=True) #axis_rotate标签角度 labelshow显示柱形数字
    bar.render(path="p_pc.html")
    print("Complete!")

if __name__ == '__main__':
    df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv', encoding='utf-8')  # or gbk
    amount_group = df.groupby(by='name',as_index=False)['p_pc'].sum()
    amount_group = amount_group.sort_values(by='p_pc',ascending=False)
    movie_top10 = amount_group.head(10)

    draw_Bar(movie_top10)
