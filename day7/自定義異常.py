class MelodyException (Exception):
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

try:
    raise MelodyException('沒有喜歡上你')
except MelodyException as e:
    print(e)
