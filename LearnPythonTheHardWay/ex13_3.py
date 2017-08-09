from sys import argv
script, user_name = argv
prompt = '..........'
print "My name is %s, and you know I am the % script."%(user_name,script)
print "do you like me?"
like = raw_input(prompt)
print "How old are you?"
age = raw_input(prompt)
print """
Ok, you said you %s me very much. you are %s years old.
"""%(like, age)
