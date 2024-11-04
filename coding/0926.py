import random


def generate_parenthesis(n):
    def backtrack(s, left, right):
        # 如果当前生成的括号组合长度达到 2*n，说明已经生成了一个有效的组合
        if len(s) == 2 * n:
            result.append(s)
            return

        # 如果左括号的数量小于 n，可以添加一个左括号
        # 确保左括号不超过n，然后右括号不超过left，所以可以保证两者不超过n
        if left < n:
            backtrack(s + '(', left + 1, right)

        # 如果右括号的数量小于左括号的数量，可以添加一个右括号
        if right < left:
            backtrack(s + ')', left, right + 1)

    result = []
    backtrack('', 0, 0)
    return result



def partition(nums, low, high):
    '''主要是将数组的分区，小于pivot的放在左边，大于pivot放在右边'''
    i = low-1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j]<pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

def quick_sort(nums,low, high):
    '''随机选择一个基准元素，然后递归分区'''
    if low<high:
        r = random.randint(low, high)
        nums[high], nums[r] = nums[r], nums[high]
        index = partition(nums, low, high)
        quick_sort(nums, low, index-1)
        quick_sort(nums, index, high)
    return nums

def merge_sort(nums):
    '''将数组分成两半，直到每个子数组只包含一个元素
    对每个子数组进行递归排序
    将两个有序的数组合并为一个有序数组
    '''
    if len(nums)<=1:return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    ans = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    ans.extend(left[i:])
    ans.extend(right[j:])
    return ans

'''
快速排序：
最坏情况：
当每次选择的枢轴都是当前数组的最大或最小值时，数组会被分为一个空数组和一个包含所有其他元素的数组。
这种情况下，递归树的高度为 n，且每层的比较次数为 n。
时间复杂度为 O(n^2)。
平均情况：
在随机情况下，每次选择的枢轴大约能将数组均匀地分成两半。
递归树的高度为 log n，每层的比较次数为 n。
时间复杂度为 O(n log n)。

归并排序：
分解：
在每次递归中，数组被分成两个相等的部分，直到每个部分只包含一个元素（基于 O(log n) 的深度）。
合并：
合并两个已排序数组的时间复杂度为 O(n)。
因此，归并排序的总时间复杂度为：
时间复杂度：
最坏情况：O(n log n)
平均情况：O(n log n)
最好情况：O(n log n)
'''
def check_palindrome(s):
    left, right = 0, len(s)-1
    while left<=right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def longest_palinddrome(s):
    res = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if check_palindrome(s[i:j]):
                if j-i+1>len(res):
                    res = s[i:j]
    return res



if __name__ == '__main__':
    print(longest_palinddrome("ana"))