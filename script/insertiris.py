import mysql.connector

mydb=mysql.connector.connect(host='localhost', user='arya', password='123456', database='iris')
mycursor=mydb.cursor()

a=open('iris.data','r')
jenis={}
total=0
for baris in a.readlines():
    try:
        element=baris.split(',')
        kelas=element[4].split('\n')
        slength=float(element[0])
        swidth=float(element[1])
        plength=float(element[2])
        pwidth=float(element[3])
        sql="insert into irisdata (sepallength, sepalwidth, petallength, petalwidth, kelas) values (%s, %s, %s, %s, %s)"
        val=(slength, swidth, plength, pwidth, kelas[0])
        mycursor.execute(sql,val)
        mydb.commit()
    except:
        print('End of file')
a.close()

