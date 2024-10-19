class BinaryTree:
    def __init__(self):
        self.root = None

    # Recursive insert
    def insert_recursive(self, data):
        if self.root is None:
            print(f'\nNew tree!. Inserting {data} as the root node.')
            self.root = Node(data)
        else:
            self.insert_recursive_helper(self.root, data)
    
    # Recursive insert helper
    def insert_recursive_helper(self, curr, data):
        if data < curr.data:
            if curr.left is None:
                print(f'Inserted {data} on the left of {curr.data}')
                curr.left = Node(data)
            else:
                print(f'{data} is less than than {curr.data}, traversing left.')
                self.insert_recursive_helper(curr.left, data)
        elif data > curr.data:
            if curr.right is None:
                print(f'Inserted {data} on the right of {curr.data}')
                curr.right = Node(data)
            else:
                print(f'{data} is greater than than {curr.data}, traversing right.')
                self.insert_recursive_helper(curr.right, data)
        else:
            print(f'Value {data} already present in the tree. Skipping insert.')

    # Iterative insert
    def insert_iterative(self, data):
        new_node = Node(data)
        if self.root is None:
            print(f'\nNew tree!. Inserting {data} as the root node.')
            self.root = new_node
            return
        
        curr = self.root
        while True:
            print(f'Checking {data} against the current node value: {curr.data}')
            if new_node.data > curr.data:
                # If the right node is null, insert it to the right
                if curr.right is None:
                    print(f'Inserted {data} on the right of {curr.data}')
                    curr.right = new_node
                    return
                # Otherwise traverse right and continue the search
                print(f'{data} is greater than {curr.data}, traversing right.')
                curr = curr.right
            elif new_node.data < curr.data:
                # If the left node is null, insert it to the left
                if curr.left is None:
                    print(f'Inserted {data} on the left of {curr.data}')
                    curr.left = new_node
                    return
                # Otherwise traverse left and continue the search
                print(f'{data} is less than than {curr.data}, traversing left.')
                curr = curr.left
            else:
                print(f'Value {data} already present in the tree. Skipping insert.')
                return

    def search(self, data):
        print(f'\nBeginning search for {data}')
        if self.root is None:
            print(f'Tree is empty')
            return False
        else:
            return self._search(self.root, data)

    def _search(self, curr, data):
        if curr is None:
            print(f'{data} does not exist in this binary tree.')
            return False
        
        if data == curr.data:
            print(f'Found {data}')
            return True
        elif data < curr.data:
            print(f'{data} is less than than {curr.data}, searching left.')
            return self._search(curr.left, data)
        else:
            print(f'{data} is greater than than {curr.data}, searching right.')
            return self._search(curr.right, data)

    # Inorder

    def inorder(self):
        print('\nBeginning inorder traversal.')
        res = []
        if self.root is None:
            return
        self._inorder(self.root, res)
        return res

    def _inorder(self, curr, result):
        if curr is None:
            return
        self._inorder(curr.left, result)
        print(f'[{curr.data}]', end = ' ')
        result.append(curr.data)
        self._inorder(curr.right, result)

    # Preorder
    def preorder(self):
        print('\nBeginning preorder traversal.')
        res = []
        if self.root is None:
            return
        self._preorder(self.root, res)
        return res

    def _preorder(self, curr, result):
        if curr is None:
            return
        print(f'[{curr.data}]', end = ' ')
        result.append(curr.data)
        self._preorder(curr.left, result)
        self._preorder(curr.right, result)   

    # Postorder
    def postorder(self):
        print('\nBeginning postorder traversal.')
        res = []
        if self.root is None:
            return
        self._postorder(self.root, res)
        return res

    def _postorder(self, curr, result):
        if curr is None:
            return
        self._postorder(curr.left, result)
        self._postorder(curr.right, result)
        print(f'[{curr.data}]', end = ' ')
        result.append(curr.data)


    # TODO -  Delete



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None