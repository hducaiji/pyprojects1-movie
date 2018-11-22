#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 统计每个月有多少上映的电影数量，找出淡季和旺季
import pandas as pd
from pyecharts import Pie

def draw_Funnel(dist):
    dates = []
    nums = []
    for item, value in dist.items():
        dates.append(item)
        nums.append(value)
    pie = Pie("淡季和旺季", title_pos='center')
    pie.add(
        "当月上映电影数量",
        dates,
        nums,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
        is_legend_show=False
    )
    pie.render(path="season.html")
    print("Complete!")

if __name__ == '__main__':
    df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv', encoding='utf-8')  # or gbk
    # print(df.duplicated("name")
    df = df.drop_duplicates("name") #去掉重名的行
    monthlyon_df = df['list_date']

    now_year = 2018
    result = {}
    for date in monthlyon_df:
        month = int(date.split('-')[1])
        year = int(date.split('-')[0])
        if year==now_year:
            if month not in result:
                result[month] = 1
            else:
                result[month] += 1

    draw_Funnel(result)


