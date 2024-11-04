def func1():
    n = int(input())
    for i in range(n):
        s = input()
        flag = 0
        if len(s)<11 or len(s)>11:
            flag =1
        for j in range(len(s)):
            if j<3:
                if not s[j].isupper():
                    flag =1
            if j==3 or j==4:
                if not s[j].isdigit():
                    flag =1
            if j==5:
                if not s[j]=="M":
                    flag =1
            if j>5:
                if not s[j].isdigit():
                    flag =1
        if flag:
            print("invalid")
        else:
            print("valid")

def func2():
    s = input()
    index_r = s.index("R")
    index_g = s.index("G")
    index_b = s.index("B")
    def find_left(index, d):
        temp = index
        while index-1>=0:
            index -= 1
            if s[index] in d:
                return temp-index
            if s[index]=="#":
                return -1
        return -1

    def find_right(index, d):
        temp = index
        while index+1<len(s):
            index+=1
            if s[index] in d:

                return index-temp
            if s[index]=="#":
                return -1

        return -1

    ans = []
    r_left = find_left(index_r, ["G","B"])
    r_right = find_right(index_r, ["G","B"])
    if r_left==-1 and r_right==-1:
        ans.append(-1)
    elif r_left!=-1 and r_right==-1:
        ans.append(r_left)
    elif r_right!=-1 and r_left==-1:
        ans.append(r_right)
    elif r_left!=-1 and r_right!=-1:
        ans.append(min(r_left,r_right))

    b_left = find_left(index_b, ["G","R"])
    b_right = find_right(index_b, ["G","R"])
    if b_left==-1 and b_right==-1:
        ans.append(-1)
    elif b_left!=-1 and b_right==-1:
        ans.append(b_left)
    elif b_right!=-1 and b_left==-1:
        ans.append(b_right)
    elif b_left!=-1 and b_right!=-1:
        ans.append(min(b_right,b_left))

    g_left = find_left(index_g, ["R", "B"])
    g_right = find_right(index_g, ["R", "B"])
    if g_left == -1 and g_right == -1:
        ans.append(-1)
    elif g_left != -1 and g_right == -1:
        ans.append(g_left)
    elif g_right != -1 and g_left == -1:
        ans.append(g_right)
    elif g_left!=-1 and g_right != -1:
        ans.append(min(g_left,g_right))

    print(" ".join(str(i) for i in ans ))

def func3():
    T = int(input())
    for i in range(T):
        ans = 0
        a,b,c,x,y = map(int,input().split())
        if a<b and a<x:
            ans = min(a,b,c)
        if a>b and a>x:
            a_num = a//x
            b_num = a_num//y
            c+=b_num
            ans = min(a,b,c)
        print(ans)
                                                                                     

if __name__ == '__main__':
    func3()