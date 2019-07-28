#import json
import pickle
f = open("test.text","rb")

def sayhi(name):
    print("hello,",name)
    print("hello2,",name)
    return 'love you'

#database = pickle.loads(f.read())
data = pickle.load(f)
f.close()

print(data["func"]("Kathy"))
