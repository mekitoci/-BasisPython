靜態方法
    只是名義上歸類管理,實際上在靜態方法裡訪問不了類或實例中的任何屬性

類方法
    只能訪問類變量,不能訪問實例變量

屬性方法
    把一個方法變成一個靜態屬性

__new__ 是用來創建實例的

__init__ --> __call__

_new__ --> __init__

反射:
    hasattr(obj,name_str) , 判斷一個對象裡是否有對應的name_str字符串的方法

    getattr(obj,name_str) , 根據字符串去獲取obj對象裡的對應的方法的內存地址

    setattr(obj,'y' ,z ) is equivalent to x.y = v

    delattr

異常
    try:
        code
    except (Error_name,Error_name2) as e:
        print(e)

    except Exception : 抓住所有錯誤 -->不建議使用