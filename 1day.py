profit = int(input("请输入当月利润(万元)："))
bonus1 = 10 * 0.1
bonus2 = bonus1 + 10 * 0.075#10万到20万
bonus3 = bonus2 + 20 * 0.05#20万到40万
bonus4 = bonus3 + 20 * 0.03#40万到60万
bonus5 = bonus4 + 40 * 0.015#60万到100万

if profit <= 10:
    print("应发奖金%0.2f万元"% bonus1)
elif profit < 20:
    print("应发奖金%0.2f万元"% bonus2)
elif profit <= 40:
    print("应发奖金%0.2f万元"% bonus3)
elif profit <= 60:
    print("应发奖金%0.2f万元"% bonus4)
elif profit <= 100:
    print("应发奖金%0.2f万元"% bonus5)
else:
    bonus = bonus5 + (profit - 100) * 0.01
    print("应发奖金%0.2f万元"% bonus)


