class MelodyException (Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise MelodyException('Cool!')
except MelodyException as e:
    print(e)
