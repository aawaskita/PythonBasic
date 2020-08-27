from faktorial4 import faktorial as fk
while True:
    a=input('a=')
    a=int(a)
    if a>=0:
        break

print(str(a)+'!='+str(fk(a)))
