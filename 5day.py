# 30000
# 6%
# 10

money = 30000
i = 0.06
sum = 30000
for year in range(0,10):
    money = money + money * i
    sum = sum + money
print("10年后年薪是%.2f元"% money)
print("10年后总收入是%0.2f元"% sum)