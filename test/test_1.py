# demo_str = "demo".encode("gbk")
# demo = demo_str.decode('gbk').encode('utf-8')
# print(demo)

class Solution():
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def removeElement(self, nums, val):

        # for i in nums:
        #     if i == val:
        #         nums.remove(i)   # 这样写会导致错乱，因为nums中的i本身就在迭代
        # print(nums)

        # c = 0
        # for i in range(len(nums) - 1):
        #     # 这样写会导致删除不完全，因为后面覆盖上来的元素也有可能是val
        #     if nums[i] == val:
        #         c += 1
        #         for j in range(i, len(nums) - 2):
        #             nums[j] = nums[j + 1]
        # print(c)
        # print(nums[:len(nums) - c -1])

        # 暴力
        # size = len(nums)
        # i=0
        # while(i<size):
        #     if nums[i]==val:
        #         for j in range(i, size-1):
        #             nums[j] = nums[j+1]
        #         size-=1
        #         i-=1
        #     i+=1
        # return size

        # 快慢指针；快指针寻找新元素，跳过目标元素，慢指针更新保存
        slow = 0
        for fast in range(len(nums)):
            if val!=nums[fast]:
                nums[slow] = nums[fast]
                slow+=1
        print(slow)
        print(nums[:slow])
        return slow

    def searchRange(self, nums, target):
        s = "".join(map(str, nums))
        print(s)
        print(s.find(str(target)))
        print(s.rfind(str(target)))

    def get_sum(self, n):
        num = 0
        while(n):
            temp = n % 10
            num += temp**2
            n //= 10
        return num

    def isHappy(self, n: int) -> bool:
        ans = []
        ans.append(n)
        while (True):
            num = self.get_sum(n)
            if num == 1:
                return True
            elif num in ans:
                return False
            else:
                ans.append(num)
                n = num



if __name__ == '__main__':
    s = Solution()
    # s.removeElement([0,1,2,2,3,0,4,2], 2)
    # s.searchRange([5,7,7,8,8,10], 8)
    print(s.isHappy(2))

