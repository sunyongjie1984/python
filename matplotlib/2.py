# -*- coding: UTF-8 -*-
# plt, numpy, scatter example

import numpy as np;
import matplotlib.pyplot as plt;
x = [ 1, 2, 3, 04, 05 ];
print "x=: \r\n", x;
y = [ 1, 4, 9, 16, 25 ];
print "y=: \r\n", y;
fig = plt.figure( );
ax = fig.add_subplot( 1, 1, 1 );
#ax.axis( [ -1, 6, -1, 30 ] );
sValue = 10 * x;
print "sValue=: \r\n", sValue;

x = np.array( [ 1, 2, 3, 4, 5 ] );
print "x=: \r\n", x;
y = x ** 2;
print "y=: \r\n", y;
sValue = 20 * x;
print "sValue=: \r\n", sValue;
#plt.scatter( x, y, s=sValue, c = 'red', marker = 'x', alpha=0.5, label='c1' );
ax.scatter( x, y, s = sValue, c = 'red', marker = 's', alpha = 0.5, label = 'c1' );
for a, b in zip( x, y ):
    plt.annotate(
            '(%s, %s)' %( a, b ),
            xy = ( a, b ),
            xytext = ( 0, -10 ),
            textcoords = 'offset points',
            ha = 'center',
            va = 'top' );
# 添加注释
# 第一个参数是注释的内容
# xy设置箭头尖的坐标
# xytext设置注释内容显示的起始位置
# arrowprops 用来设置箭头
# facecolor 设置箭头的颜色
# headlength 箭头的头的长度
# headwidth 箭头的宽度
# width 箭身的宽度
plt.annotate('this is a annotate', xy=(2, 4), xytext=(4, 9),arrowprops=dict(facecolor='yellow', shrink=0.05))
# 可以通过设置xy和xytext中坐标的值来设置箭身是否倾斜

plt.title( 'basic scatter plot ' );
plt.xlabel( 'variables x' );
plt.ylabel( 'variables y' );
plt.legend( );
plt.show( );
