def guess():
    i = 0
    j = 100
    m = 50
    counter = 1
    print("Please guess a number")
    while True:
        condition = input("Is your guess " + str(m) + "?(0 means it's too low, 1 means it's your guess and 2 means "
                                                      "it's too high) ")
        if condition == 1:
            break
        counter += 1
        if condition == 0:
            i = m + 1
        elif condition == 2:
            j = m - 1
        m = (i + j) // 2

    print("It took", counter, "times to guess your number")


guess()