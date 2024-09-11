'''
- 二分查找
- 在一个有序序列中查找某个目标值。
- 在一个满足单调性（单调递增或单调递减）的范围内查找最优解。
- 步骤
     - 确定边界-迭代查找-终止条件
'''


def min_length_to_plant_trees():
    # https://mp.weixin.qq.com/s/eB0ralhhAxk9hFsT9ExVVA
    n, k = map(int, input().split())
    a = list(map(int,  input().split()))
    a.sort()

    def check(lens):
        temp = []
        for i in range(len(a)):
            for j in range(0, lens):
                if a[i]+j not in temp:
                    temp.append(a[i]+j)
        if len(temp)>=k:
            return  True
        else:return False

    left, right = 0,  a[-1] - a[0]
    while left < right:
        mid = (left + right) // 2
        if check(mid):right = mid
        else: left = mid + 1

    return left

if __name__ == '__main__':
    print(min_length_to_plant_trees())