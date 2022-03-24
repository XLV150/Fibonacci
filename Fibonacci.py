def fibonacci(x):
    """
    Returns fibbonacci(x)

    :param x:
    :return:
    """
    if 0 <= x <= 1:
        return x

    x_minus1, x_minus2 = 1, 0

    result = None
    for f in range(x - 1):
        result = x_minus2 + x_minus1
        x_minus2 = x_minus1
        x_minus1 = result

    return result


y = int(input("Enter the number for which fibonacci will return up to: "))

for i in range(y):
    print(fibonacci(i))