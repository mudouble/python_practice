def valid_ip_address(strs):
    '''验证IP地址'''
    def is_ipv4(s):
        try:
            for i in s:
                if not 0<=int(i)<=255:
                    return False
                if len(i)>1 and i[0]=="0":
                    return False
        except Exception as e:
            print(e)
            return False
        return True

    def is_ipv6(s):
        for i in s:
            if not 1<=len(i)<=4:
                return False
            for j in i:
                if not ("0"<=j<="9" or "a"<=j<="f" or "A"<=j<="F"):
                    return False
        return True
    s = ""
    if "." in strs:s = strs.split(".")
    if ":" in strs:s = strs.split(":")
    if len(s)==4 and is_ipv4(s):
        return "IPv4"
    elif len(s)==8 and is_ipv6(s):
        return "IPv6"
    else:
        return "Neither"

def number_to_chinese(num):
    '''阿拉伯数字转中文'''
    chinese_digits = ["零","一", "二","三","四","五","六","七","八","九"]
    chinese_units = ["","十", "百","千","万","亿"] 
    if num==0:return chinese_digits[0]
    num = str(num)
    length = len(num)
    ans = ""
    for i in range(length):
        digit = int(num[i])
        unit = chinese_units[length-i-1]
        if digit!=0:
            ans+=chinese_digits[digit]+unit
        else:
            if ans.endswith("零") and ans!="":
                ans+=chinese_digits[digit]

    if ans.endswith("零") and ans!="":
        ans = ans[:-1]
    ans = ans.replace("一十", "十") if ans.startswith("一十") else ans
    return ans
            

'''米哈游笔试'''
def exchange_max(nums):
    dp = [0]*len(nums)
    for i in range(len(nums)-1):
        dp[i] = nums[i]*nums[i+1]
    print(f"dp {dp}")
    dp_exchange = [0]*len(nums)
    for i in range(1, len(nums)-1):
        dp_exchange[i] = nums[i-1]*nums[i+1]
    print(f"dp_exchange {dp_exchange}")
    max_1 = max(dp)
    max_2 = max(dp_exchange)
    return max(max_1, max_2)

def buy_good():
    n, m, k = map(int, input().split())
    dicts = {}
    for i in range(1, n+1):
        dicts[i] = list(map(int, input().split()))
    for i in range(1, k+1):
        a, b = map(int, input().split())
        dicts[a].append(b)
    print(dicts)
    res = 0
    for i in range(1, n+1):
        ans = dicts[i][1]
        w = dicts[i][0]
        for j in range(i+1, n+1):
            if j not in dicts[i][2:] and m>=(w+dicts[j][0]):
                ans+=dicts[j][1]
                w+=dicts[j][0]
        res = ans if ans>res else res
    print(res)
    return res






            

    
if __name__ == '__main__':
    print(loop())