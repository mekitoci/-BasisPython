import time

class Flight(object):
    def __init__(self,name):
        self.flight_name = name


    def checking_status(self):
        print("\033[35;1m歡迎來到雋洋機場－班機狀況服務系統\033[0m")
        print("確認班機\033[41;1m%s\033[0m狀態" % self.flight_name)
        return 0

    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0 :
            print("\033[31;1m查詢中......請稍後\033[0m")
            time.sleep(3)
            print("班機已經取消(CANCEL)")
        elif status == 1 :
            print("\033[31;1m查詢中......請稍後\033[0m")
            time.sleep(3)
            print("班機已經抵達(ARRIVAL)")
        elif status == 2:
            print("\033[31;1m查詢中......請稍後\033[0m")
            time.sleep(3)
            print("班機已經離站(DEPARTURE)")
        else:
            print("查詢中......請稍後")
            time.sleep(1)
            print("無法確認班機情況,請稍後確認...")

    @flight_status.setter
    def flight_status(self,status):
        status_dic = {
            0 :"取消",
            1 :"到達",
            2 :"離站"
        }
        time.sleep(2)
        print("發生錯誤！！")
        time.sleep(1)
        print("發生錯誤！！")
        time.sleep(0.5)
        print("\033[31;1m更正班機情況：\033[0m",status_dic.get(status))

    @flight_status.deleter  #删除
    def flight_status(self):
        time.sleep(5)
        print("\033[32;1m班機資料已被刪除\033[0m")

f = Flight("跳跳虎航空(T1104)")
f.flight_status
f.flight_status = 2
del f.flight_status
