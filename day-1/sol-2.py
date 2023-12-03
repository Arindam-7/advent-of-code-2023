hash = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4, 
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def strToNum(s):
    for i in hash:
        if s.startswith(i):
            return hash[i]
    return 0


def calculate(s):
    val1, val2 = 0, 0
    l = len(s)

    for i in range(l):
        if(s[i].isdigit()):
            val1 = int(s[i])
            break
        else:
            a = strToNum(s[i:])
            if(a != 0):
                val1 = a 
                break

    for j in range(l):
        i = l - j - 1 
        if(s[i].isdigit()):
            val2 = int(s[i])
            break 
        else:
            a = strToNum(s[i:])
            if(a != 0):
                val2 = a 
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


