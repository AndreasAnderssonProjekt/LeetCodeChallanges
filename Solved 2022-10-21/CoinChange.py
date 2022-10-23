def coinChange(coins,amount):
    if amount == 0:
        return 0

    value1 = [0]
    value2 = []

    layer = 0

    visited = [False] * (amount + 1)
    visited[0] = True

    while value1:
        layer += 1

        for v in value1:
            for c in coins:
                if v + c == amount:
                    return layer
                elif v + c > amount:
                    continue
                elif not visited[v + c]:
                    value2.append(v + c)
                    visited[v+c] = True

        value1, value2 = value2, []

    return -1
