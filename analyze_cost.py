#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 性价比最好的电影(根据价格，时长和口碑指数)
import pandas as pd
from pyecharts import Bar

def draw_Bar(df):
    names = []
    costs = []
    for name in df['name'].values.tolist():
        names.append(name)
    for cost in df['cost'].values.tolist():
        costs.append(cost)
    bar = Bar("性价比最好的电影Top10")
    bar.add("性价比", names, costs, is_more_utils=True, xaxis_rotate=20, is_label_show=True) #axis_rotate标签角度 labelshow显示柱形数字
    bar.render(path="cost.html")
    print("Complete!")

if __name__ == '__main__':
    df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv', encoding='utf-8')  # or gbk
    df1 = df.groupby('name', as_index=False)['list_day'].sum() # 对上映天数求和
    df2 = df.groupby('name', as_index=False)['wom_index', 'avg_price'].mean() # 对价格和口碑指数求平均（因为两月总是相等的）
    result_df = pd.merge(df1, df2, on='name') # 合并
    result_df.insert(4, 'cost', 0) #增加新列，计算性价比cost
    for index, row in result_df.iterrows():
        # 性价比 = ((口碑*3)*(上映天数*0.5))/(价格)
        cost = (((row["wom_index"]*3)*row["list_day"]*0.1)/row["avg_price"])
        score_result = float('%.2f' % (cost))
        result_df.iloc[index, 4] = score_result
    high_per_df = result_df.sort_values(by='cost', ascending=False).reset_index(drop=True).head(10)
    draw_Bar(high_per_df)
