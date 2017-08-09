def pf(x, y, z):
    return x * y * z
    
print "1****"
print pf(1, 2, 3)

print "2****"
x = 1
print pf(x, 2, 3)

print '3****'
x, y, z = 1, 2, 3
print pf(x, y, z)

print '4****'
x = pf(x, 2, 3)
print pf(x, 2, 3)
