import heapq
import random

def partition(nums, low, high):
    i = low-1
    # 这里的随机会影响结果
    # index = random.randint(low, high)
    # pivot = nums[index]
    pivot = nums[high]
    for j in range(low, high):
        if nums[j]>pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

def find_kth_largest(nums ,k):
    # heap = []
    # for num in nums:
    #     heapq.heappush(heap, num)
    #     if len(heap) > k:
    #         heapq.heappop(heap)
    # return heapq.heappop(heap)
    if len(nums)==1:return nums[0]
    k = k-1
    low, high = 0, len(nums)-1
    while True:
        index = random.randint(low, high)
        print(f"index {index}")
        nums[high], nums[index] = nums[index], nums[high]
        pi = partition(nums, low, high)
        if pi==k:
            print(nums)
            return nums[pi]
        elif pi<k:
            low = pi-1
        else:
            high = pi+1