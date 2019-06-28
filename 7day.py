money = int(input("请输入汇款金额（元）："))
if money > 5000:
    cost = 50
elif money >= 100:
    cost = money * 0.01
else:
    cost = 1
print("邮局的会费为%.2f元"% cost)