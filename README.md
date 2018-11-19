密圈第一个实战项目：电影数据分析
# 要求
做一份电影数据分析，通过对2018全年的电影数据获取进行分析和探索：
1. 票房最高的电影Top10
2. 人气最高的电影Top
3. 性价比最好的电影(根据价格，时长和口碑指数)
4. 统计每个月有多少上映的电影数量，找出淡季和旺季
# 步骤一：获取数据
源码：getMoives.py
* 电影的数据通过tushare库获取，老库：https://tushare.pro 新库：http://tushare.org
* 然后通过`to_csv(filename)`方法，将获得的数据保存到本地。如果要追加，通过`.to_csv(filename, mode='a', header=False)`。具体可以参考：http://tushare.org/storing.html#csv
# 步骤二：清洗数据
# 步骤三：分析数据
# 步骤四：可视化数据
# 结论
# 附录1: dataframe
dataframe简单来说就是个数据框，x轴/列名为columns，y轴行标签为index，中间填充数据。根据Columns和Index两个参数定位数据。

## 创建df
[10 Minutes to pandas — pandas 0.23.4 documentation](https://pandas.pydata.org/pandas-docs/stable/10min.html)<br>
[pandas.DataFrame — pandas 0.23.4 documentation](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame)<br>
`DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)`
* Creating a Series by passing a list of *values*, letting pandas create a default integer index:
```python
s = pd.Series([1,3,5,np.nan,6,8])
```
* Creating a DataFrame by passing a *NumPy array*, with a datetime index and labeled columns:
```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
```
* Creating a DataFrame by passing a *dict* of objects that can be converted to series-like:
```python
df2 = pd.DataFrame({ 'A' : 1.,'B' : pd.Timestamp('20130102'),'C' :pd.Series(1,index=list(range(4)),dtype='float32'),'D' : np.array([3] * 4,dtype='int32'),'E' : pd.Categorical(["test","train","test","train"]),'F' : 'foo' })
```

## 增删
### 增加列
在最后增加一列
```python
df['who'] = pd.Series(np.random.randn(110),index=df.index)
```
在指定位置增加一列
```python
df.insert(0,'who',np.random.randn(110))
df.insert(len(df.columns),'who',np.random.randn(110)) #在最后一行插入一列
```
### 删除列
直接删除df的某列
```python
del df['who']
```
返回一张删了某行/某列的新表
```python
print(df.drop([1])) #删index=1的行
print(df.drop(['who','rank'],axis=1)) #删who和rank两个列
```

## 数据选择
```python
df['name']
df[0:2] #选择第一行和第二行
df['0':'1'] #使用行标签选择！需要照顾到行标签的数据类型
```
### loc
loc方法主要用于获取某一块的数据
```python
df.loc[0:2,'avg_price':'p_pc'] #获取某一块
df.loc[[1,7],['name','rank']] #获取指定列的指定行
df.loc[0,'name'] #获取某一行的某一列
```
### at
at方法主要用于获取某一个值 效率
`df.at[1,'name']`
### iloc
iloc方法主要用于通过int(数字的行列标)获取某一块数据
```python
print(df.iloc[1])
print(df.iloc[1:3,1:3])
print(df.iloc[[2,4,6],[1,3,4]])
```
### iat
iat方法主要用于通过int提取某一个数据 效率更高
`df.iat[1,1]`
### T
行列转换
`df.T`

## 计数统计
### 读取数据
```python
df = pd.read_csv('/Users/fseeeye/Desktop/movies.csv',encoding='utf-8') #or gbk
```
### 统计数量
```python
rank_df  = df[df['rank']<6]
rank_count = rank_df['rank'].value_counts()
```
### 统计总和
```python
amount_sum = df['month_amount'].sum()
```

## 数据分组处理
groupby方法实现分组
```python
name_group = df.groupby('name') #分组
name_group.sum() #对所有列求和
name_group.groups #获取分组的字典
name_group.get_group('侏罗纪世界2') #获得name=某个值的组
name_group.get_group('侏罗纪世界2').loc[:, 'month_amount']
name_group = df.groupby(['list_date','name']) #根据两列分组
name_group.first() #Compute first of group values
name_group.last() #Compute last of group values
```
aggregate方法实现数据分组计算
```python
name_group['month_amount'].agg([np.sum,np.mean,np.std]) #.aggregate=.agg 对month_amount列进行统计总和、平均数、标准差
name_group['month_amount'].agg({'总和':np.sum, '平均':np.mean, '标准差':np.std})
# 定制显示标题 FutureWarning: using a dict on a Series for aggregation is deprecated and will be removed in a future version
name_group.size() #查看各组的行数
name_group.describe() #对每个组进行描述性统计
```

## 查看数据
查看各行数据: `df.dtypes`
查看前几行数据，默认五行 `df.head(2)`
查看后几行数据，默认五行 `df.tail(2)`
查看df的索引们 `df.index`
查看df的列名们 `df.columns`
查看所有数据值，返回array `df.values`
通过某列对数据排列 `df.sort_values(by='name')`
通过索引对数据排列 `df.sort_index`

## 筛选数据
```python
#逻辑符号筛选数据，并输出其name
print(df['name'][(df['rank']<2)&(df['rank']>0)|(df['wom_index']>7)])
#列表筛选数据，isin函数会返回true/false
wom_list = [7.86,8.13,6.1]
print(df['wom_index'].isin(wom_list))
print(df['name'][df['wom_index'].isin(wom_list)==True]) #筛选出评分在列表中的name
```

## 缺失值处理
### 代替缺失值
```python
print(df.fillna(0))
print(df.fillna(method='pad')) #从上而下替代
print(df.fillna(method='bfill',limit=1)) #从下而上替代 最多替代1次
print(df.fillna(df.mean()['one':'two'])) #用统计值替代(平均/总和...)df某几列的nan
print(df.interpolate()) #上下两点估计中间的值
```
### 删除缺失值
删除含有缺失值的行/列
```
print(df.dropna()) #删行
print(df.dropna(axis=1)) #删列
```
### 数值替换
```
#把所有2换成20
print(df.replace(2,20))
#替换a列中的1和3 为 99和100
print(df['a'].replace([1,3],[99,100]))
```
