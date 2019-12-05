big=0
small=0
print('before',big)
for thing in [-25,-99,0,9,12,13,54,6,78,98]:
    if thing>big:
        big=thing
    print(big,thing)
    if thing<small:
        small=thing
    print(small,thing)
print('after',big)
print('after',small)
