category={}
pre='UNSW_2018_IoT_Botnet_Dataset_'
post='.csv'
for i in range(2,75):
    c=0
    filename=pre+str(i)+post
    print(filename)
    a=open(filename,'r')
    for baris in a.readlines():
        element=baris.split(',')
        x=len(element)
        c=c+1
        if x>=35:
            b=element[x-1].split('\n')
            if b[0] not in category:
                category[b[0]]=1
            else:
                category[b[0]]=category[b[0]]+1
        else:
            print(c)

    c=0
    a.close()
print(category)
