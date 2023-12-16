def multiply(num1,num2):
    comp1, comp2 = [], []

    for i in reversed(range(len(num1))):
        comp1.append(int(num1[i]) * (10**(len(num1) - 1 - i)))

    for i in reversed(range(len(num2))):
        comp2.append(int(num2[i]) * (10**(len(num2) - 1 - i)))

    prod = 0

    for n1 in comp1:
        for n2 in comp2:
            prod += n1 * n2

    return str(prod)
