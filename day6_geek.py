h = int(input("请输入篮球初始高度（米）："))
m = h #第一次落地经过的距离
sum = h
for i in range(0,10):#弹跳10次
    if i == 0:#第一次落地经过的距离
        sum = m
    else:
        m = m / 2 #落地反弹的高度
        sum = sum + 2 * m #总共经过的距离
print("到球第10次落地一共经过 %.9f 米"% sum)
print("第10次弹跳高度是%.9f米"% m)
