'''
面试题
'''
import random


class QueueUsingStacks:
    '''栈实现队列'''
    def __init__(self):
        self.stack_out = []
        self.stack_in = []
    
    def push(self, x):
        self.stack_in.append(x)
    
    def pop(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            return None
    def print_q(self):
        res = []
        if self.stack_out:
            res += self.stack_out
        if self.stack_in:
            res+=self.stack_in
        print(res)
    def is_empty(self):
        if not self.stack_out and not self.stack_in:
            return True
        return False
    def __len__(self):
        return len(self.stack_in)+len(self.stack_out)

class SortMethod:
    '''
    排序算法
    * 快速排序通过选择一个基准元素进行分区，递归地排序子数组，通常在内存中进行原地排序，
    * 而归并排序通过将数组分割成较小部分，递归地排序这些部分后再合并，保证稳定性，但需要额外的空间
    * python 内置的sort sorted是使用插入排序和归并排序的混合排序
    '''
    def quickSort_space(self, arr):
        '''快速排序-牺牲空间复杂度'''
        if len(arr)<=1: return arr
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quickSort_space(left) + middle + self.quickSort_space(right)
    
    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] < pivot:
                i+=1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
                
    
    def quick_sort(self, arr, low, high):
        '''
        - 快速排序-原地排序
        -  不稳定
        - 时间复杂度 O(n^2) O(nlogn)O(nlogn)
        - 空间复杂度 O(logn)
        - 分而治之，效率高
        '''
        if low < high:
            # 随机化基准点-不然很容易超时，大型的数据还是使用归并排序把
            pivot_index = random.randint(low, high)
            nums[high], nums[pivot_index] = nums[pivot_index], nums[high]

            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi-1)
            self.quick_sort(arr, pi, high)
        return arr  
    
    def merge_sort(self, arr):
        '''
        - 归并排序
        - 稳定
        - 时间复杂度O(nlogn) O(nlogn)O(nlogn)
        - 空间复杂度 O(n)
        - 大规模数据且要求稳定
        - 分而治之
        '''
        if len(arr)<=1: return arr
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        print("left: ", left)
        print("right: ", right)
        self.merge_sort(left)
        self.merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        print(arr)
        return arr

    def bubble_sort(self, arr):
        '''
        - 冒泡排序
        - 稳定
        - 时间复杂度O(n^2)
        - 空间复杂度O(1)
        - 教学或简单演示
        - 每轮将最大或最小冒泡到序列的一端
        '''
        if len(arr)<=1:return arr
        for i in range(len(arr)):
            flag = 1
            for j in range(len(arr)-1-i):
                if arr[j]>arr[j+1]:
                    flag = 0
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            print(arr)
            if flag:
                return arr
        return arr

    def insert_sort(self, arr):
        '''
        - 插入排序
        - 稳定
        - 时间复杂度O(n^2)
        - 空间复杂度O(1)
        - 小规模数据或部分有序的数据
        - 在几乎有序的数据上效率高
        '''
        if len(arr)<=1:return arr
        # i前面的是已经排好序了
        for i in range(1, len(arr)):
            key = arr[i]
            j = i -1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key
            print(arr)
        return arr

    def select_sort(self, arr):
        '''
        - 选择排序
        - 不稳定
        - 时间复杂度O(n^2)
        - 空间复杂度O(1)
        - 小规模数据且相对稳定性不高的场景
        - 每轮选择最小（或最大）元素放到已排序部分末尾
        '''
        if len(arr)<=1:return arr
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            print(arr[min_index])
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)
        return arr

class SearchMethod:
    def binary_search(self, arr, target):
        '''
        - 二分查找
        - 时间复杂度O(logn) O(logn)O(logn)
        - 空间复杂度O(1)
        - 适用于有序数据
        - 每次排除一半的数据
        '''
        left, right = 0, len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target:

                return mid
            elif arr[mid] < target:
                left = mid+1
            elif arr[mid] > target:
                right = mid-1
        return -1

class LinkNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def create(self, values):
        if not values:
            return None
        head = LinkNode(values[0])
        current = head
        for value in values[1:]:
            current.next = LinkNode(value)
            current = current.next
        return head

    def get_intersection_node_two_pointers(self, headA, headB):
        '''两个链表的相交点'''
        # 双指针法
        p1 = headA
        p2 = headB
        while p1 != p2:
            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next
            if p1:print(p1.val)
            else:print("p1 is None")
            if p2:print(p2.val)
            else:print("p2 is None")
        return p1
    
    def get_intersection_node_length(self, headA, headB):
        '''长度差'''
        def get_length(head):
            length = 0
            while head:
                length+=1
                head = head.next
            return length
        
        lenA, lenB = get_length(headA), get_length(headB)
        diff = abs(lenA-lenB)
        if lenA>lenB:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(diff):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def reverse(self, head):
        '''反转链表'''
        prev = None
        current = head
        while current:
            temp = current.next    
            current.next = prev
            prev = current
            current = temp
        return prev

    def insert_at_head(self, head, val):
        '''双向链表头节点插入一个节点'''
        new_node = LinkNode(val=val)
        if head is None:
            head = new_node
        else:
            new_node.next = head
            head.prev = new_node
            head = new_node
        return head


    def print_link(self, head):
        while head:
            print(head.val, end="->")
            head = head.next

def find_kth_min(listA, listB, k):
    '''两个排序数组找到第K小的值'''
    if len(listA) + len(listB) < k:
        return -1
    i, j = 0, 0
    while True:
        if i<len(listA):
            while j==len(listB) or listA[i]<=listB[j]:
                i+=1
                if i+j == k:return listA[i-1]
        if j<len(listB):
            while i==len(listA) or listA[i]>listB:
                j+=1
                if i+j == k:return listB[j-1]
                


def share_gold(n, gold):
    '''分金币-中位数的特性是使得数据分布两侧的距离总和最小'''
    average = sum(gold)//n
    print(f"average: {average}")
    diff_sum = [0]*n
    for i in range(1, n):
        diff_sum[i] = diff_sum[i-1]+gold[i-1]-average
    print(f"diff_sum: {diff_sum}")
    diff_sum.sort()
    median = diff_sum[n//2]
    print(f"medain: {median}")
    min_moves = sum(abs(diff-median)for diff in diff_sum)
    print(f"min_moves: {min_moves}")
    return min_moves


def can_split(nums, k, max_sum):
    current_sum = 0
    splits_required = 1
    for num in nums:
        # 当前子数组之和超过了max_sum
        if current_sum + num > max_sum:
            splits_required += 1
            current_sum = num
            if splits_required > k:
                return False
        else:
            current_sum += num
    return True


def split_array(nums,k):
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left+right)//2
        if can_split(nums, k, mid):
            right = mid
        else:
            left = mid+1
    return left

def longestCommonPrefix(strs):
    ans = ""
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i>=len(s) or strs[0][i] != s[i]:
                return ans
        ans += strs[0][i]
    return ans

def merge_two_sorted_array(arr1, m, arr2, n):
    '''合并两个有序数组'''
    # if m>0:
    #     arr1 = arr1[:n]+arr2
    # else: arr1 = arr2
    # arr1.sort()
    # print(arr1)
    i = len(arr1)-1
    while n>0:
        if m>0 and arr1[m-1]>arr2[n-1]:
            arr1[i] = arr1[m-1]
            i-=1
            m-=1
        else:
            arr1[i]=arr2[n-1]
            i-=1
            n-=1
        print(arr1)
    print(arr1)
    return arr1

def is_valid_bracket(str):
    stack = []
    for s in str:
        print(s)
        if s=='(' or s=='{' or s =='[':
            stack.append(s)
        else:
            if stack:
                if s==')' and stack.pop()!='(':
                    return False
                elif s=='}' and stack.pop()!='{':
                    return False
                elif s==']' and stack.pop()!='[':
                    return False
            else:
                return False
    if len(stack)>0:
        return False
    else:
        return True

def tranfer(nums):
    for i in range(len(nums)):
        if nums[i]%2!=0:
            j=i
            while j>0 and nums[j-1]%2==0:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
    # left, right = 0, len(nums)-1
    # while left<right:
    #     if nums[left]%2==0 and nums[right]%2!=0:
    #         nums[left], nums[right] = nums[right], nums[left]
    #     if nums[left]%2!=0:
    #         left+=1
    #     if nums[right]%2==0:
    #         right-=1
    print(nums)
    return nums

def merger(intervals):
    intervals.sort()
    print(intervals)
    res = []
    for inter in intervals:
        if res and res[-1][1]>=inter[0]:
            res[-1][1] = max(res[-1][1], inter[1])
        else:
            res.append(inter)
    print(res)
    return res

def duplicate_removal(nums):
    nums.sort()
    if len(nums)<=1:return nums
    slow, fast = 0,1
    while fast<len(nums):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            nums[slow+1] = nums[fast]
            slow+=1
    return nums[:slow+1]

def compute_next(pattern):
    next = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j>0 and pattern[i]!=pattern[j]:
            j = next[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        next[i] = j
    return next

def kmp(text, pattern):
    '''kmp字符串匹配问题-在一个文本字符串找到一个模式字符串的位置'''
    next = compute_next(pattern)
    j = 0
    for i in range(len(text)):
        while j>0 and text[i]!=pattern[j]:
            j = next[j-1]
        if text[i] == pattern[j]:
            j+=1
        if j == len(pattern):
            print(f"found pattern at index {i-j+1}")
            j = next[j-1]

def LCS(X, Y):
    '''最长公共子序列-在两个序列中找最长的公共子序列，出现的顺序是一致的'''
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f"dp: {dp}")
    # 回溯
    lcs = []
    i, j = m, n
    while i>0 and j>0:
        if X[i-1] ==Y[j-1]:
            lcs.append(X[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    print("".join(reversed(lcs)))
    return "".join(reversed(lcs))

if __name__ == '__main__':
    nums = [-1,0,0,3,5,9,9,12]
    method = SearchMethod()
    print(method.binary_search(nums, 9))
