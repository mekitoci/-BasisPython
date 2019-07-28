import hashlib

m = hashlib.md5()
m.update(b"hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m.update(b"It's been a long time since we spoken..")
print(m.hexdigest())

m2 = hashlib.md5()
m2.update(b"helloIt's meIt's been a long time since we spoken..")

print(m2.hexdigest())
