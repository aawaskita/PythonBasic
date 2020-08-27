def faktorial(n):
    f=1
    if n<2:
        return 1
    else:
        return n * faktorial(n-1)

if __name__=='__main__':
    while True:
        a=input('a=')
        a=int(a)
        if a>=0:
            break

    print(str(a)+'!='+str(faktorial(a)))
