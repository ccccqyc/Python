def num(K = 1, m = 1):
    i = 0
    numbers = []
    
    if K < m:
        print "sorry, I can't print it, it overrun."
    
    else :
        while i < K:
            print "At the i is %d" % i
            numbers.append(i)
        
            i = i + m
            print "numbers now: ", numbers
            print "At the bottom i is %d" % i 
        
        
        print "The numbers: "

        for nums in numbers:
            print nums 
