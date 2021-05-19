# -*- coding: UTF-8 -*-#中文编码
#coding=utf-8

import matplotlib.pyplot as plt#调用matplotlib的库
import numpy as np #
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)# x轴数据
y = np.sin(x)#y轴表示正弦波

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#第一行两列第一幅图
plt.title(r'$f(x)=sin(x)$') #给第一幅图片加标题
plt.plot(x, y)#绘制波形
#plt.show()

x1 = [t*0.375*np.pi for t in x]# x轴数据
y1 = np.sin(x1)#y轴表示正弦波
plt.subplot(1,2,2)#第一行两列第二幅图
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #给第二幅图片加标题
plt.plot(x, y1)#绘制第二个波形
plt.show()#输出波形