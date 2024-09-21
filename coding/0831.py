def compute_next(pattern):
    n = len(pattern)
    next = [0] * n
    length_pre_suffix = 0
    for i in range(1, n):
        while length_pre_suffix > 0 and pattern[i] != pattern[length_pre_suffix]:
            length_pre_suffix -= 1
        if pattern[i] == pattern[length_pre_suffix]:
            length_pre_suffix += 1
        next[i] = length_pre_suffix
    return next


def kmp(strs, pattern):
    next = compute_next(pattern)
    j = 0
    ans = []
    for i in range(len(strs)):
        while j > 0 and strs[i] != pattern[j]:
            j = next[j - 1]
        if strs[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            ans.append(i - j + 1)
            j = next[j - 1]
    return ans


def longest_parlindrome(strs):
    def expand_from_center(s, left, right):
        print(f"left: {left}, right: {right}")
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        print(f"right-left: {right - left - 1}")
        return right - left - 1

    if len(strs) <= 0:
        return 0
    start, max_len = 0, 1
    for i in range(len(strs)):
        len_add = expand_from_center(strs, i, i)
        len_even = expand_from_center(strs, i, i + 1)
        current_max = max(len_add, len_even)
        if current_max > max_len:
            max_len = current_max
            start = i - (max_len - 1) // 2
    return strs[start:start + max_len]


def length_of_longest_substring(strs):
    temp = []
    ans = 0
    for i in range(len(strs)):
        if strs[i] not in temp:
            temp.append(strs[i])
            print(f"temp: {temp}")
        else:
            index = temp.index(strs[i])
            temp = temp[index + 1:] + [s[i]]
            # temp.append(strs[i])

        if len(temp) > ans:
            ans = len(temp)
            res = ''.join(temp)
        print(ans)
    return res


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    if head or head.next is None: return False
    slow, fast = head, head.next
    while slow != fast:
        if fast is None and fast.next is None:
            return False

        slow = slow.next
        fast = fast.next.next
    return True
    # method2
    # temp = []
    # if head is None or head.next is None:
    #     return False
    # cur = head
    # while cur.next:
    #     if cur not in temp:
    #         temp.append(cur)
    #         cur = cur.next
    #     else:
    #         return True
    # return False


def permute(nums):
    def backtrack(path, used, ):
        if len(path) == len(nums):
            res.append(path[:])
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True

            print(f"i {i} path: {path}")
            backtrack(path, used)
            path.pop()
            print(f"回溯 i{i} path: {path}")

            used[i] = False
            # print(f"i {i} path: {path}")
            # print(f"i {i} used: {used}")

    res = []
    backtrack([], [False] * len(nums))
    return res

def reverse(nums):
    '''整数反转'''
    pass

def max_sub_array(nums):
    dp = [0]*len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    ans = max(dp)
    print(ans)
    print(dp)
    return ans

def single_number(nums):
    '''只出现一次的数字'''
    # 异或，相同的数字会相互抵消，0和数字异或为本身
    res = 0
    for num in nums:
        res^=num
    return res





if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_sub_array(nums)
    a = "-25"
    print(int(a))

