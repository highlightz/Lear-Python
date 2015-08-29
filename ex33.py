def func_1( capacity ):
    i = 0
    numbers = []

    while i < capacity:
        print "At the top i is %d" % i
        numbers.append( i )

        i = i + 1

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

def func_2( capacity, step ):
    i = 0
    numbers = []

    while i < capacity:
        print "At the top i is %d" % i
        numbers.append( i )

        i = i + step

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

def func_3( capacity ):
    i = 0
    numbers = []

    for i in range( 0, capacity ):
        print "At the top i is %d" % i
        numbers.append( i )

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

