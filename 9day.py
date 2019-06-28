for num in range(200, 300):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            break
    else:
        print('%d 是大于200的最小质数' % num)
        break