big=0
small=None
fork=0
some=0
count=0
print('before',big)
for thing in [-25,-99,0,9,12,13,54,6,78,98]:
     count=count+1
    some=some+thing
    print(count,some,thing)
    fork=fork+1 #counts number of execution
    print(fork,thing)
    fork=fork+thing #adds in things
    print(fork,thing)
    fork=fork-thing #substracts from things
    print(fork,thing)
    if thing>big: #finds biggest value
        big=thing
    print(big,thing)
     if small is None:
        small=thing
    elif thing < small:#finds smallest value
        small=thing
    print(small,thing)
print('big',big)
print('small',small)
print('count',fork)
print('avg', count,some,some/count)
