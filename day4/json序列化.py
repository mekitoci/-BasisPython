import json
import pickle
def sayhi(name):
    print("hello,",name)
    return 'love you'

info = {
    'name' : 'Kathy',
    'age' : 18,
    'func' :sayhi
}

f = open("test.text","wb")

#f.write(pickle.dumps(info))
pickle.dump(info,f)

f.close()