# plt, numpy, scatter example
import numpy as np;
import matplotlib.pyplot as plt;
x = [ 1, 2, 3, 04, 05 ];
print "x=: \r\n", x;
y = [ 1, 4, 9, 16, 25 ];
print "y=: \r\n", y;
fig = plt.figure( );
ax = fig.add_subplot( 1, 1, 1 );
ax.axis( [ -1, 6, -1, 30 ] );
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
plt.title( 'basic scatter plot ' );
plt.xlabel( 'variables x' );
plt.ylabel( 'variables y' );
plt.legend( );
plt.show( );
