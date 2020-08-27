def faktorial(n):
    f=1
    if n<2:
        f=1
    else:
        for i in range(1,n+1):
            f=f*i
    print(str(n)+'!='+str(f))

while True:
    a=input('a=')
    a=int(a)
    if a>=0:
        break

while True:
    b=input('b=')
    b=int(b)
    if b>=0:
        break

faktorial(a)
faktorial(b)
