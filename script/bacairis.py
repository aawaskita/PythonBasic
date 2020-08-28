a=open('iris.data','r')
jenis={}
total=0
for baris in a.readlines():
    try:
        element=baris.split(',')
        kelas=element[4].split('\n')
        if kelas[0] not in jenis:
            jenis[kelas[0]]=1
        else:
            jenis[kelas[0]]+=1
        print(kelas[0]+' ke-'+str(jenis[kelas[0]])+':')
        print('Sepal length: '+element[0]+ 'cm')
        print('Sepal width: '+element[1]+ 'cm')
        print('Petal length: '+element[2]+ 'cm')
        print('Petal width: '+element[3]+ 'cm')
        total+=1
    except:
        print('End of file')
a.close()
print('Statistics')
for i in jenis.keys():
    print(i+': '+str(jenis[i])+' items ('+'{:4.2f}'.format(jenis[i]/total)+'%)')
