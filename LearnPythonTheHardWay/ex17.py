from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how ?
indata = open(from_file).read()
#or, (in_file,indata) = (open(from_file), in_file.read())
print "The input file is %d bytes long" % len(indata)

print "Dose the output file exit? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
