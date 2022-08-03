# Inorder - left, current, right
# preorder - current, left, right
# postorder = left, right, current

def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + 
            [node.key] + 
            traverse_in_order(node.right))
        

def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key] +
            traverse_pre_order(node.left) +
            traverse_pre_order(node.right))


def traverse_post_order(node):
    if node is None:
        return []
    return (traverse_post_order(node.left) +
            traverse_post_order(node.right) + 
            [node.key])
