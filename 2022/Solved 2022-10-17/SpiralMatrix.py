def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])
    order = []
    if m == 1:
        for i in range(n):
            order.append(matrix[0][i])
        return order

    if n == 1:
        for i in range(m):
            order.append(matrix[i][0])
        return order

    order.append(matrix[0][0])
    n_right = n - 1
    n_left = 0
    m_down = m - 1
    m_up = 1

    right = True
    down = False
    left = False
    up = False

    i = 0
    j = 0
    while len(order) < m * n:
        while right:
            j += 1
            order.append(matrix[i][j])
            if len(order) == m * n:
                return order
            if j == n_right:
                n_right -= 1
                down = True
                right = False



        while down:
            i += 1
            order.append(matrix[i][j])
            if len(order) == m * n:
                return order
            if i == m_down:
                m_down -= 1
                left = True
                down = False

        while left:
          j -= 1
          order.append(matrix[i][j])
          if len(order) == m * n:
              return order
          if j == n_left:
              n_left += 1
              up = True
              left = False


        while up:
            i -= 1
            order.append(matrix[i][j])
            if len(order) == m * n:
                return order
            if i == m_up:
                m_up += 1
                right = True
                up = False

    return order
