import random
a=[]
for i in range(20):
    a.append(random.randint(0,10))

b=7
if b in a:
    print('Ada')
else:
    print('Tidak ada')

