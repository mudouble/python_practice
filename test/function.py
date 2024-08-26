dicts = {'a':1, 'b':2,'c':3}
new_dicts = {v:k for k, v in dicts.items()}
print(new_dicts)

def single_ton(cls):
    instance={}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls]=cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@single_ton
class MyClass():
    def __init__(self):
        self.value = 0

instance1 = MyClass()
instance2 = MyClass()
print(instance2==instance1)

# 快速选择
def partition(low, high, nums):
    pivot = nums[high]
    index = low-1
    for i in range(low, high):
        if nums[i] < pivot:
            index += 1
            nums[index], nums[i] = nums[i], nums[index]
    nums[index+1], nums[high] = nums[high], nums[index+1]
    return index+1


def select_small(nums, k):
    low, high = 0, len(nums)-1
    while low<=high:
        index = partition(low, high, nums)
        if index==k:
            return nums[:k]
        elif index<k:
            low = index+1
        else:
            high = index-1
    return nums[:k]

def quick_sorted(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x <pivot]
    right = [x for x in nums if x >pivot]
    middle = [x for x in nums if x == pivot]

    return quick_sorted(left)+middle+quick_sorted(right)

def quick_sort(arr, low, high):
    if low<high:
        index = partition(low, high, arr)
        quick_sort(arr, low, index-1)
        quick_sort(arr, index+1, high)
    return arr

import heapq
def find_smallest_elements(arr, n):

    return heapq.nsmallest(n, arr)


def sorted_smallest(arr, n):
    arr.sort()
    return arr[:n]

# 示例用法
arr = [5, 3, 8, 1, 7, 9, 4, 2, 6]
n = 3
print(quick_sort(arr, 0, len(arr)-1))  # 输出前3小的元素


class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_head(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end="<->"if current.next else"\n")
            current = current.next

link = DoublyLinkedList()
link.insert_at_head(1)
link.insert_at_head(12)
link.display()

class LinkNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Linked:
    def __init__(self):
        self.head = None

    def insert(self, value):
        current = self.head
        if current is None:
            self.head = LinkNode(value)
        else:
            while current.next is not None:
                current = current.next
            new_node = LinkNode(value)
            current.next = new_node

    def converse(self):
        current = self.head
        pre = None
        while current:
            temp = current.next
            current.next = pre
            pre = current
            current = temp
        self.head = pre

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" " if current.next else "\n" )
            current = current.next

link1 = Linked()
link1.insert(2)
link1.insert(22)
link1.display()
link1.converse()
link1.display()






