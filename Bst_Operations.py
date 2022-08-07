# Inserting into BST
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
        
    return node
  
  # Finding node in BST
def find(node, key):
    if node is None:
        return Node
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
      
# Updating a value in BST
def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
        
# List all nodes
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)
