from node import Node
 
def comp_1(node_1, node_2):
    return node_1.remcap-node_2.remcap
    pass

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def get_height(self, node):
        return node.height if node else 0
    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self.update_height(y)
        self.update_height(x)

        return x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self.update_height(x)
        self.update_height(y)

        return y
    def insert(self, root, key, value=None):
        if not root:
            return Node(key, value)

        # Use the comparator function to determine the position of the new node
        if self.comparator(key, root.key) < 0:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)

        self.update_height(root)
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and self.comparator(key, root.left.key) < 0:
            return self.rotate_right(root)

        if balance < -1 and self.comparator(key, root.right.key) > 0:
            return self.rotate_left(root)

        if balance > 1 and self.comparator(key, root.left.key) > 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.comparator(key, root.right.key) < 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    def delete(self, root, key):
        if not root:
            #print(f"Node with key {key} not found.")
            return root
        
        # Traverse the tree to find the node to delete
        if self.comparator(key, root.key) < 0:
            #print(f"Going left: Searching for key {key} in left subtree of {root.key}")
            root.left = self.delete(root.left, key)
        elif self.comparator(key, root.key) > 0:
            #print(f"Going right: Searching for key {key} in right subtree of {root.key}")
            root.right = self.delete(root.right, key)
        else:
            #print(f"Deleting node with key {key}")
            # Node with only one child or no child
            if not root.left:
                #print(f"Node with key {key} has no left child.")
                return root.right
            elif not root.right:
                #print(f"Node with key {key} has no right child.")
                return root.left
            
            # Node with two children, get inorder successor (smallest in right subtree)
            temp = self.get_min_value_node(root.right)
            #print(f"Inorder successor of {key} is {temp.key}")

            # Replace root's key and value with successor's key and value
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)
        
        # Update height of current node
        self.update_height(root)
        #print(f"Updated height of node {root.key} to {root.height}")

        # Get balance factor of this node
        balance = self.get_balance(root)
        #print(f"Balance at node {root.key} is {balance}")

        # Balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            #print(f"Right rotation on node {root.key}")
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            #print(f"Left rotation on left child of {root.key} followed by right rotation")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            #print(f"Left rotation on node {root.key}")
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            #print(f"Right rotation on right child of {root.key} followed by left rotation")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)
    def get_max_value_node(self, node):
        if node is None or node.right is None:
            return node
        return self.get_max_value_node(node.right)
    def search(self, root, key):
        if root is None or self.comparator(key, root.key) == 0:
            return root
        if self.comparator(key, root.key) < 0:
            return self.search(root.left, key)
        return self.search(root.right, key)
    def find_successor(self, root, key):
        successor = None
        current = root

        while current:
            if current.key >= key:
                successor = current  # Candidate for successor
                current = current.left  # Look for smaller candidate in the left subtree
            else:
                current = current.right  # Look for greater key in the right subtree

        if successor:
            return successor.key
        else:
            return None  # No successor found (if the given key is the largest)
        
    def find_successor_node(self, root, key):
        successor = None
        current = root

        while current:
            if current.key >= key:
                successor = current  # Candidate for successor
                current = current.left  # Look for smaller candidate in the left subtree
            else:
                current = current.right  # Look for greater key in the right subtree

        if successor:
            return successor
        else:
            return None 
        
    def insert_node(self, key, value=None):
        self.root = self.insert(self.root, key, value)
    def delete_node(self, key):
        self.root = self.delete(self.root, key)
    def search_node(self, key):
        return self.search(self.root, key)
    # Function to perform in-order traversal of AVL tree
    def inorder_traversal(self, root):
        result = []
    
        def inorder(node):
            if node is not None:
                inorder(node.left)  # Visit left subtree
                result.append(node.key)  # Visit node itself
                inorder(node.right)  # Visit right subtree
        
        inorder(root)
        return result
        







if __name__ == "__main__":
    tree = AVLTree(lambda x,y: x-y)
    l = [x for x in range(10)]
    from random import shuffle
    shuffle(l)
    for i in l:
        tree.insert_node(i, i)
    print(tree.inorder_traversal(tree.root))
    shuffle(l)
    for i in l:
        print(f"removing {i}")
        tree.delete_node(i)
        print(tree.inorder_traversal(tree.root))
    