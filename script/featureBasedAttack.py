a=open('unsw15attack.csv','r')
basic=open('basicFeature.csv','w')
content=open('contentFeature.csv','w')
time=open('timeFeature.csv','w')
general=open('generalFeature.csv','w')
connection=open('connectionFeature.csv','w')
F=5
B=18
C=26
T=35
G=40
Conn=47
for baris in a.readlines():
    element=baris.split(',')
    jenis=element[len(element)-1]
    for j in range(F):
        basic.write(element[j]+',')
        content.write(element[j]+',')
        time.write(element[j]+',')
        general.write(element[j]+',')
        connection.write(element[j]+',')

    for j in range(F,B):
        basic.write(element[j]+',')
    basic.write(jenis)

    for j in range(B,C):
        content.write(element[j]+',')
    content.write(jenis)

    for j in range(C,T):
        time.write(element[j]+',')
    time.write(jenis)

    for j in range(T,G):
        general.write(element[j]+',')
    general.write(jenis)

    for j in range(G,Conn):
        connection.write(element[j]+',')
    connection.write(jenis)

a.close()
basic.close()
content.close()
time.close()
general.close()
connection.close()
