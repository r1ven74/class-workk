
def check(z, v):
    if z == v:
        print(z)
        return
    print(z)
    if z < v:
        check(z+1, v)
    else:
        check(z-1, v)
check(1, int(input()))



def check(a, b):
    if a == b:
        print(a)
        return
    print(a)
    if a < b:
        check(a+1, b)
    else:
        check(a-1, b)
check(int(input()), int(input()))




num = int(input())
lst = 1
result = ""
def check(num, lst):
    global result
    if lst > num:
        result = "NO"
    else:
        if lst == num:
            result = "YES"
        else:
            lst *= 2
            check(num, lst)

check(num, lst)
print(result)


def fib(x):
    print(x)
    fib(x+x)
fib(1)






























