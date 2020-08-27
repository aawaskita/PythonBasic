n=input('n=')
n=int(n)
if n<0:
   print('Argumen salah')
else:
    f=1
    if n<2:
        f=1
    else:
        for i in range(1,n+1):
            f=f*i
    print(f)
