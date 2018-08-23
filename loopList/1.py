#
a = [ 'a1', 'a2', 'a3' ];
b = [ 'b1', 'b2' ];

print "Map:"
for x, y in map(None, a, b):
    print x, y

print "Zip:"
for x, y in zip(a, b):
    print x, y


print "List comprehension:"
for x, y in [(x,y) for x in a for y in b]:
    print x, y
