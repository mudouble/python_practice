def find_median_sorted_arrays(nums1, nums2):
    '''两个有序数组找中位数，时间复杂度log(m+n)'''
    nums = nums1 + nums2
    nums.sort()
    median = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[median - 1] + nums[median]) / 2.0
    else:
        return nums[median]


def check_palindrome(s):
    left, right = 0, len(s)-1
    while left<=right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def longest_palindrome(s):
    '''超时'''
    # ans = 0
    # res = ''
    # # if len(s)<=1:
    # #     print(s)
    # #     return s
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)+1):
    #         if check_palindrome(s[i:j]):
    #             print(f"i: {i}, j:{j}, s[i:j]: {s[i:j]}")
    #             if j-i>ans:
    #                 ans = j-i
    #                 res = s[i:j]
    #
    # print(res)
    # return res
    '''中心扩散法'''
    if len(s)<2:
        return s
    start, max_len = 0,1
    def expand_around_center(left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1, right-1
    
    for i in range(len(s)-1):
        l1, r1 = expand_around_center(i, i)
        l2, r2 = expand_around_center(i, i+1)
        if r1-l1+1>max_len:
            start, max_len = l1, r1-l1+1
        if r2-l2+1>max_len:
            start, max_len = l2, r2-l2+1
    return s[start:start+max_len]
    



if __name__ == '__main__':
    longest_palindrome("b")
    nums = [1]
    print(nums[0:1])
    for i in range(1, 1):
        print("执行吗")