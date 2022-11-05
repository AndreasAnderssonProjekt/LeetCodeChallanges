def levelOrder(root):
    return traverseLevelOrder((root,[],0)


def traverseLevelOrder(root, order,level):
    if not root:
        return

    if len(order) == 0:
        order.append([root.val])

    elif level >= len(order):
        order.append([root.val])

    else:
        order[level].append(root.val)

    traverseLevelOrder((root.left, level + 1)
    traverseLevelOrder((root.right, level + 1)

    return order
