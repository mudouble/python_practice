def single_ton(cls):
    instance= {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls]=cls(*args, **kwargs)
        return instance[cls]
    return wrapper
    # 返回一个函数，可以被调用

def single_ton_1(cls):
    instance= {}
    if cls not in instance:
        instance[cls]=cls()
    return instance[cls]
    # 返回了一个类本身，后续去调用的时候就会出错

@single_ton
class MyClass:
    a = 0
    b = 0
    def __init__(self):
        self.value = 'Hello, World!'

def func(nums, n):
    res = []
    digits = [int(digit) for digit in str(n)]
    print(digits)
    for i in digits:
        if i in nums:
            res.append(i)
        else: res.append(max(nums))
    print(res)


nums = [2,4,9]
n = 23121
func(nums, n)

# instance1 = MyClass()
# instance2 = MyClass()
# MyClass.a = 100
# print(instance1.a)
# print(instance1 == instance2)
