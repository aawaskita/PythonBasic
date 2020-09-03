import json

def exploreDict(a,b):
    print('json level '+str(b)+':')
    for i in a:
        if not type(a[i]) is dict:
            if type(a[i]) is str:
                print('key='+i+', '+'value='+a[i])
            else:
                print('key='+i+', '+'value=')
                print(a[i])
        else:
            b+=1
            exploreDict(a[i],b)
    return b

f=open('173.pdf.json','r')
artikel=json.load(f)
print('total json level='+str(exploreDict(artikel,1)))
