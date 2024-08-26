class Car:
    total_cars = 0  # 类变量，用于跟踪创建的汽车总数

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1  # 每次创建新汽车时，增加总汽车数

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars  # 类方法用于获取总汽车数


# 创建汽车实例
car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("BMW")

# 使用类方法获取汽车总数
print("Total cars using class method:", Car.get_total_cars())  # 输出: 3
print(Car.total_cars)

# 直接使用类名访问和修改类变量
Car.total_cars = 10  # 修改汽车总数为 10

# 使用类方法获取汽车总数
print("Total cars using class method:", Car.get_total_cars())  # 输出: 10
print(Car.total_cars)
