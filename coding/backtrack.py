def fun1():
    '''
    https://mp.weixin.qq.com/s/-JHuxZML2XRAmqUiAuMiQA
    '''
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
        b.append(list(map(int, input().split())))

    def backtracking(level, current_sum):
        nonlocal max_res
        if level == n:
            extra_bonus = 0
            for i in range(m):
                if chosen[i] >= 3:
                    extra_bonus += c[i]
            max_res = max(max_res, current_sum + extra_bonus)
            return

        for i in range(3):
            reward_value = a[level][i]
            resource = b[level][i] - 1
            chosen[resource] += 1
            backtracking(level + 1, current_sum + reward_value)
            chosen[resource] -= 1

    chosen = [0] * m
    max_res = 0
    backtracking(0, 0)

    print(max_res)


if __name__ == '__main__':
    fun1()




