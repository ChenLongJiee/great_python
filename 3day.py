r = []
a = []
b = []
count1 = input("请随机输入第一位位数：")
count2 = input("请随机输入第二位位数：")
count3 = input("请随机输入第三位位数：")
r.append(count1)
r.append(count2)
r.append(count3)

r.sort()
print(r)
r.sort(reverse = True)
print(r)