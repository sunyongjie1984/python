import matplotlib.pyplot as plt
x = [ 1, 2, 3, 04, 05 ];
y = [ 1, 4, 9, 16, 25 ];
fig = plt.figure( );
fig.add_subplot( 2, 2, 4 );
plt.scatter( x, y );
fig.add_subplot( 1, 2, 1 );
plt.scatter( x, y );
plt.show( );
