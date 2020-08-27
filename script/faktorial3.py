def faktorial(n):
    f=1
    if n<2:
        f=1
    else:
        for i in range(1,n+1):
            f=f*i
    return f
