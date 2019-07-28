import hashlib

s2 = hashlib.sha1()
s2.update(b"helloIt's me")
print(s2.hexdigest())