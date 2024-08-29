1. 0827总结一些面试题，包括各种排序算法
2. 0825是pdd的笔试


---
# pythonic风格
 1. 简洁和易懂<br>
**清晰胜于晦涩，可读性优先** <br>
``` python 
# Non-Pythonic
if a > b:
    result = True
else:
    result = False
# Pythonic
result = a > b
```
2. 利用内置函数和数据结构<br>
**充分利用Python内置函数以及数据结构，不要重复造轮子，避免不必要的手动实现**<br>
``` python
# Non-Pythonic
squares = []
for i in range(10):
    squares.append(i * i)

# Pythonic
squares = [i * i for i in range(10)]
```
3. 控制流<br>
**列表推导式，生成器表达式** <br>
``` python
# Non-Pythonic
result = []
for item in iterable:
    if condition(item):
        result.append(item)

# Pythonic
result = [item for item in iterable if condition(item)]
```
4. 异常处理而不是条件判断<br>
**EAFP:宁愿道歉，也不请示**<br>
```python
# Non-Pythonic
if 'key' in my_dict:
    value = my_dict['key']
else:
    value = None

# Pythonic
try:
    value = my_dict['key']
except KeyError:
    value = None
```
5. 模块化和可复用性
函数和类的划分合理，遵循 DRY（Don't Repeat Yourself） 原则：避免重复代码
```python
# Non-Pythonic
def process_data(data):
    # 处理数据的一大段代码

# Pythonic
def clean_data(data):
    # 清洗数据的代码

def analyze_data(data):
    # 分析数据的代码

def process_data(data):
    clean_data(data)
    analyze_data(data)

```
6. 使用标准库
```python
# Non-Pythonic
import os

files = os.listdir('.')
files = [f for f in files if f.endswith('.py')]

# Pythonic
import glob

files = glob.glob('*.py')

```