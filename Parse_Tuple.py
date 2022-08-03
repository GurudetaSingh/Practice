# Use tuple to create tree
# 2 is root node, (1, 3, None) is left subtree, ((None, 3, 4), 5, (6, 7, 8)) is right subtree
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    # Recursion ends when encountering None as input
    elif data is None:
        node = None
    else:
        node = TreeNode(data)      
    return node
