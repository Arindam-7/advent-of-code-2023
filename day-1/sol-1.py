def calculate(s):
    val1, val2 = 0, 0
    l = len(s)

    for i in range(l):
        if(s[i].isdigit()):
            val1 = int(s[i])
            break

    for j in range(l):
        i = l - j - 1 
        if(s[i].isdigit()):
            val2 = int(s[i])
            break 

    return (val1*10)+val2 

def sol(data):
    lines = list(data)
    ans = 0
    for i in lines:
        ans += calculate(i)
    return ans


data = open('input.txt', 'r').read().split('\n')
print(sol(data))

