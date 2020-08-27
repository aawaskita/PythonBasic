import random

while True:
    a=random.randint(0,10)
    b=random.randint(0,20)
    try:
        print(a/b)
    except:
        print('Penyebut sama dengan 0')
        break
