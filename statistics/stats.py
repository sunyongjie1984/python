from math import sqrt
from numpy import average, std
from scipy.stats import t
from scipy.stats import skew
from scipy.stats.mstats import mquantiles
from scipy.stats import kurtosis


dataArray = [ ];
with open("a.txt") as file_object:
    for line in file_object:
        line = line.strip();
        dataArray.append( float( line ) );

print dataArray;
mean = average( dataArray )
print "mean:", mean

stddev = std(  dataArray, ddof=1 )
print "stddev: ", stddev

n = len( dataArray );
print "size of samples %d" % n;

df = n - 1;
print "degree of freedom %d" % df;

ci = t.interval(0.95, df    , loc=mean, scale=stddev/sqrt( n ))  # 95% confidence interval
print "confidence interval( student t distribution ): ( %e, %e ) " % ( ci[ 0 ], ci[ 1 ] );

tmpArray = [ ];
for i in range( 4 ):
    tmpArray.append( dataArray[ i ] );

print tmpArray;

tmp_kurtosis = kurtosis( tmpArray, 0, True, False )
print "tmp kurtosis: ", tmp_kurtosis

tmpArray = [ 1, 2, 3, 4 ];
print tmpArray;

tmp_kurtosis = kurtosis( tmpArray, 0, True, False )
print "tmp kurtosis: ", tmp_kurtosis
tmpArray = [ 2, 7, 4, 9, 3 ];
print tmpArray;

tmp_kurtosis = kurtosis( tmpArray, 0, True, False )
print "tmp kurtosis: ", tmp_kurtosis
tmp_kurtosis = kurtosis( tmpArray );
print "tmp kurtosis: ", tmp_kurtosis


val_kurtosis = kurtosis( dataArray, 0, True, False )
print "kurtosis: ", val_kurtosis

val_skew = skew( dataArray, 0, False )
print "skewness: ", val_skew

val_quartile = mquantiles( dataArray );
print "quartile 1 (Q1):", val_quartile[ 0 ];
print "quartile 3 (Q3):", val_quartile[ 2 ];

#dataArray = ( [ 1, 2, 3, 4, 5 ] );
#al_skew= skew( dataArray );
#rint "skewness: ", val_skew

