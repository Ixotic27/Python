import math as mt
def prime(n):
    if n<=1:
        print("Not Prime!")
        return
    found=1
    r=int(mt.sqrt(n))
    for i in range(2,r,1):
       if n%i==0:
          found-=1
          break
    if(found): print("Prime no")
    else : print("Not a prime no")
    return