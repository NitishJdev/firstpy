big=0
small=0
fork=0
print('before',big)
for thing in [-25,-99,0,9,12,13,54,6,78,98]:
    fork=fork+1 #calculates executed loops
    print(fork,thing)
    if thing>big: #finds biggest number from thing
        big=thing
    print(big,thing)
    if thing<small: #finds smallest number from thing
        small=thing
    print(small,thing)
print('after',big)
print('after',small)
print('after',fork)
