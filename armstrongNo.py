for i in range(1000):
    k=i
    sum = 0
    temp = i

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if i == sum:
            print(i, "is an Armstrong number")
        # else:
        # # print(i, "is not an Armstrong number")
