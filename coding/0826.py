from typing import List


def lengthOfLongestSubstring(s: str):
    '''无重复字符的最长子串-面试题'''
    temp = []
    ans = 0
    for i in s:
        if i not in temp:
            temp.append(i)
        else:
            index = temp.index(i)
            temp = temp[index + 1:] + [i]
        ans = len(temp) if len(temp) > ans else ans
    print(ans)
    return ans

def longgest_substring(s, k):
    '''k个重复的最长子串'''
    if len(s)<k:
        return 0
    char_count = {}
    for item in s:
        char_count[item] = char_count.get(item, 0)+1
    for ch in char_count:
        if char_count[ch]<k:
            substrings = s.split(ch)
            return max(longgest_substring(substring, k) for substring in substrings)
    return len(s)


def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    '''子数组中不同整数的绝对差值小于等于k'''
    ''' # 超时
     ans = 0
     for i in range(len(nums)):
         flag = i+k
         while flag<=len(nums):
             temp = nums[i:flag]
             flag+=1
             if len(set(temp))==k:
                 print(temp)
                 ans+=1
             elif len(set(temp))>k:
                 break
     '''
    return atMostKDistinct(nums, k)-atMostKDistinct(nums, k-1)

def atMostKDistinct(nums, k):
    length = len(nums)
    freq = [0]*(length+1)
    left, right = 0, 0
    count, res = 0, 0
    while right<length:
        if freq[nums[right]]==0:
            count+=1
        freq[nums[right]]+=1
        right+=1
        while count>k:
            freq[nums[left]]-=1
            if freq[nums[left]]==0:count-=1
            left+=1
        res+=right-left
    return res
    


if __name__ == '__main__':
    s= "aaaab"
    print(longgest_substring(s, 4))
