def maxArea(height):
    opt = 0
    l1 = 0
    l2 = len(height) - 1
    while l1 < l2:
        area = min(height[l1], height[l2]) * (l2-l1)
        if area > opt:
            opt = area

        if height[l1] < height[l2]:
            l1 += 1
        else:
            l2 -= 1

    return opt
