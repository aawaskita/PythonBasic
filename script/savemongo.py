import pymongo

f=open('173.pdf.json','r')
artikel=json.load(f)

try:
    myclient=pymongo.MongoClient('mongodb://localhost:27017')
    try:
        mydb=myclient['articledb']
        try:
            mycollection=mydb['parsedb']
            try:
                x=mycollection.insert_one(artikel)
                print(x.inserted_id)   
            except:
                print('insert document failed')
        except:
            print('collection creation failed')
    except:
        print('database creation failed')
except:
    print('connection failed')


