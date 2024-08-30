def fun():
    '''排列组合'''
    


def singleton(cls):
    '''装饰器'''
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

@singleton
class MyClass:
    def __init__(self, values):
        self.values = values

'''实习的时候django flask框架里有很多装饰器，比如装饰redis缓存的，还有redis加锁的'''


from collections import OrderedDict
# OrderedDict保留了键值对插入的顺序
class LRUCache:
    '''LRU算法-当缓存空间不足时，移除最近最少被访问的数据'''
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        # 将访问的键移动到末尾
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache)>=self.capacity:
                # 缓存已满，移除最近最少被访问的键
                # popitem(last=True) 从OrderedDict中移除并返回最后插入的键值对
                # popitem(last=False) 从OrderedDict中移除并返回最早插入的键值对（第一个键值对）
                self.cache.popitem(last=False)

            self.cache[key] = value


class TreeNode:
    '''二叉搜索树'''
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert_into_bst(self, root, value):
        if not root:
            return TreeNode(value)
        if value<root.value:
            root.left = self.insert_into_bst(root.left, value)
        else:
            root.right = self.insert_into_bst(root.right, value)
        return root

    def search(self, root, value):
        if not root or root.value==value:
            return root
        if value<root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def preorder_traversal(self, root):
        if root:
            print(root.value)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.value)


class Vector:
    '''魔法函数'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

def regex_ox(strs):
    import re
    hex_regex = re.compile(r'\b0x[0-9a-fA-F]+\b')
    matches = hex_regex.findall(strs)
    print(matches)

if __name__ == '__main__':
    strs= "Here are some hex numbers: 0x1A3, 0xB4F, 0x5C7, and some non-hex numbers: 0xG12, 0x123Z."
    regex_ox(strs)

