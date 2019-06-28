randNum = int(input("请输入一个整数："))
if randNum%5 == 0 and randNum%6 ==0:
    print("%d能被5和6整除"%randNum)
elif randNum%5 == 0 and randNum%6 == 1:
    print("%d只能被5整除" % randNum)
elif randNum%5 == 1 and randNum%6 == 0:
    print("%d只能被6整除" % randNum)
else:
    print("%d不能被5和6整除" % randNum)