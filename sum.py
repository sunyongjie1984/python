# -*- coding: UTF-8 -*-
import numpy as np
n = [ 0, 1, 2 ];
m = [ 2, 1, 3 ];
k = [ n, m ];

mat0 = np.mat( k ); #list -> matrix
print "mat0\r\n", mat0;
print "mat0.shape\r\n", mat0.shape;

# 现在对于数据的处理更多的还是numpy。没有axis参数表示全部相加，
# axis＝0表示按列相加，axis＝1表示按照行的方向
a=np.sum( mat0, axis = 0 );
print "a=np.sum( mat0, axis = 0 )\r\n", a;
a=np.sum( mat0, axis = 1 );
print "a=np.sum( mat0, axis = 1 )\r\n", a;

a=mat0.sum( axis = 0 );
print "mat0.sum( axis = 0 )\r\n", a;
a=mat0.sum( axis = 1 );
print "mat0.sum( axis = 1 )\r\n", a;
