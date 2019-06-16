# 折纸上月球
high = 0.088
month = 363300000000000
# high = high**2
x = 1
while high <= month:
    high += high
    x += 1
print("折纸 %d 次后可以登上月球！"% x)