big=0
small=0
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
    if thing<small: #finds smallest value
        small=thing
    print(small,thing)
print('after',big)
print('after',small)
print('after',fork)
print('after', count,some,some/count)
