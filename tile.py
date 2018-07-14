# -*- coding: UTF-8 -*-
import numpy;

a = [ 0, 0 ];
print "a\r\n", a;
b = numpy.tile( a, 5 ); #在列方向上重复[0,0]5次，默认行1次
print "b\r\n", b;
c = numpy.tile( a, ( 3, 2) ); #在列方向上重复[0,0]2次，行3次
print "c\r\n", c;
