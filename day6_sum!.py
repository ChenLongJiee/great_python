s = 1
sum = 0
for i in range(1,6):#计算1到5的阶乘
    s *= i #i的阶乘
    sum += s #计算阶乘和
print("1!+2!+3!+4!+5!的和是：%d"% sum)