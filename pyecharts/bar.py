from pyecharts.charts import Bar
from os.path import exists
import os
# 正常调用
# bar = Bar()
# bar.add_xaxis(['苹果', '香蕉', '栗子', '萝卜'])
# bar.add_yaxis("商家1", [10, 20, 30, 40])
# bar.add_yaxis("商家2", [20, 30, 40, 45])
# 链式调用x
# bar = (Bar().add_xaxis(['苹果', '香蕉', '栗子', '萝卜'])
#        .add_yaxis("商家1", [10, 20, 30, 40])
#        .add_yaxis("商家2", [20, 30, 40, 45])
#        .set_global_opts(title_opts='蔬菜'))
# if exists('bar.html'):
#     os.remove('bar.html')
# bar.render('bar.html')
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.sans-serif'] = 'SimHei'
# p1 = plt.figure(figsize=(10, 6))
# ax1 = p1.add_subplot(2, 1, 1)
#
# title = ['苹果', '香蕉', '栗子', '萝卜']
# value = [[10, 20, 30, 40], [20, 30, 40, 45]]
# range = np.arange(len(value[0]))
# plt.bar(range, value[0], 0.5)
# plt.bar(range+0.5, value[1], 0.5)
# plt.xticks(range+0.25, title, rotation=270)
# # ax1.autofmt_xdate()
# plt.show()
import pandas as pd
data = pd.read_csv('豆瓣书评.csv')
data = data.dropna(subset=['name'],axis=0)
data['pingjia'] = data['pingjia'].fillna('pingjia')
data['year'] = [i[0:4] for i in data['time']]
year = []
print(data.groupby(by='year').size())
for i in data.groupby(by='year').size():
    year.append(i)
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = 'SimHei'
plt1 = plt.figure(figsize=(10,6))
ax1 = plt1.add_subplot(2, 1, 1)
# print(np.arange(2012, 2023, 1))
plt.plot(np.arange(2012, 2023, 1), year)
pingjia = []
num = []
for i, j in data[["year","pingjia"]].groupby(by='year'):
    pingjia.append(i)
    num.append(j['pingjia'].count())
ax2 = plt1.add_subplot(2,1,2)
plt.pie(num, labels=pingjia,autopct='%1.1f%%')
plt.show()