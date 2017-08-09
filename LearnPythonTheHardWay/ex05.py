name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print 'Let\'s talk about %s.' %name
print "He's %.2f centimeters tall." %(2.45 * height)
print "He's %.2f kiols heavy." % (0.4535924 * weight)
print "Actually that's not too heavy." 
print "He's got %s eyes ang %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
