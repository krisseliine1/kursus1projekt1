from random import *
def minu_suffle(järjend):
    for i in range(len(järjend)):
        a = järjend[i]
        b = randint(0, len(järjend)-1)
        järjend[i] = järjend[b]
        järjend[b] = a
        
    return järjend
print(minu_shuffle([2,3,4,6,7])
    


