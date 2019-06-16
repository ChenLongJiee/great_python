# n!=1*2*3*...*n
# n的阶乘
n = int(input("请输入一个非负整数n的值："))
count = 1
sum = 1
if n == 0:
    print("%d != 1"% n)
else:
    while count < n:
        sum = sum * (count + 1)
        count += 1
    print("%d  != " % count,sum)

