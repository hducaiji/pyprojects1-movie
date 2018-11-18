# movies
密圈第一个实战项目：电影数据分析
## 要求
做一份电影数据分析，通过对2018全年的电影数据获取进行分析和探索：
1. 票房最高的电影Top10
2. 人气最高的电影Top
3. 性价比最好的电影(根据价格，时长和口碑指数)
4. 统计每个月有多少上映的电影数量，找出淡季和旺季
## 步骤一：获取数据
* 电影的数据通过tushare库获取，老库：https://tushare.pro 新库：http://tushare.org
* 然后通过`to_csv(filename)`方法，将获得的数据保存到本地。如果要追加，通过`.to_csv(filename, mode='a', header=False)`。具体可以参考：http://tushare.org/storing.html#csv
## 步骤二：清洗数据
## 步骤三：分析数据
## 步骤四：可视化数据
## 结论
