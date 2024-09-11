import math
from itertools import zip_longest


def fun1():
    n = int(input())
    s, v = zip(*[input().split() for _ in range(n)])
    v = list(map(int, v))
    s = list(s)
    ans = -1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] in s[i] or s[i] in s[j]:
                temp = v[i] + v[j]
                ans = temp if temp > ans else ans
    return ans


def fun2():
    s = input().split()
    ans = 0
    for item in s:
        if item[0].isupper():
            ans += 1
    return ans


def fun3():
    '''字符串判断email phone_number ip'''

    def check_eamil(s):
        if "@" in s:
            username, domain = s.split("@")
            if ".com" not in domain:
                return False
            else:
                domain = domain.split(".")[0]
            print(f"{username} {domain}")
            for i in username:
                if not i.isdigit() and not i.isalpha() and i != "_" :
                    return False
            for j in domain:
                if not j.isdigit() and not j.isalpha():return False
            return True

        else:
            return False

    def check_phone(s):
        if s[0] == "+":
            country, arear, number = s[1:].split("-")
            try:
                temp = int(country)
                temp = int(arear)
            except:
                return False
            for i in number:
                if i != "#" and not i.isdigit():
                    return False
            else:
                return True
        else:
            return False

    def check_ip(s):
        ip = s.split(".")
        if len(ip) < 4:
            return False
        for i in ip:
            if not i.isdigit() or not 0 <= int(i) <= 255: return False
        return True

    n = int(input())
    for i in range(n):
        s = input()
        if check_ip(s):
            print("ip")
        elif check_eamil(s):
            print("email")
        elif check_phone(s):
            print("phone")
        else:
            print("invalid")

def re_strs_judge():
    '''正则表达式'''
    import re
    pattern_email = "^[a-zA-Z0-9_]+@+[a-zA-Z0-9_]+\\.com$"
    pattern_ip = r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-99])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-99]))"
    pattern_phone = "^\\+\\d+-\\d+-[\\d+#]+$"

    s = input()
    if re.match(pattern_phone, s):
        print("ip")
    else:
        print("invalid")

def fun4():
    '''最大公约数'''
    def check_prime(num):
        if num==1:return False
        for i in range(2, num):
            if num%i==0:
                return False
        return True

    def gcd(a,b):
        while b:
            a, b = b, a%b
        return a

    n = int(input())
    for m in range(n, 3, -1):
        ans = gcd(n, m)
        if check_prime(ans):
            return ans
def fun5():
    '''极差=最大值-最小值
    列表的极差最小-元素都接近平均值
    '''
    n = int(input())
    a = list(map(int, input().split()))
    average = sum(a)//len(a)
    ans = 0
    need = 0
    for i in range(n):
        need+=a[i]-average
        ans = max(ans, abs(need))
    return ans

def fun6():
    n = int(input())
    correct = input()
    password = [input() for _ in range(n)]
    password_sorted = sorted(password, key=lambda x:len(x))
    ans = []
    len_correct = len(correct)
    len_password_sorted = len(password_sorted)
    if len_correct==len(password_sorted[0]):ans.append(1)
    else:
        for i in range(len_password_sorted):
            if len_correct==len(password_sorted[i]):
                ans.append(i+1)
                break
    temp = []
    for i in range(len_password_sorted):
        if len(password_sorted[i])<len_correct:
            if password_sorted[i] not in temp:
                temp.append(password_sorted[i])
        elif len(password_sorted[i])==len_correct:
            if password_sorted[i]!=correct and password_sorted [i] not in temp:
                temp.append(password_sorted[i])
    print(temp)
    ans.append(len(temp)+1)
    print(ans)
    return " ".join(str(i) for i in ans)
            
def fun7():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = math.inf
    def counts(nums):
        min_num = -1
        for i in range(max(nums)+1):
            if i not in nums:
                min_num = i
                break

        if min_num==-1:min_num = max(nums)+1
        return min_num

    for i in range(n):
        temp = i*x+counts(a[i:])*k
        ans = min(ans, temp)
    print(ans)




if __name__ == '__main__':
    print(fun7())



