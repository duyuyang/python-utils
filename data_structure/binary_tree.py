# Implement a binary tree
# root
# node
# leaf

from collections import deque # used in bfs()


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

        # insertion
        # If the current node doesn't have a left_child, we create a new node and set it to the current node's left_child
        # If it does have the left_child, we create a new node, put it in the current left_child's place. Allocate this left_child node to the new node's left_child.
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    # Print the value of the tree

    # Tree traversal
    # Depth-First Search (DFS)
    # It starts at the root and explores as far as possible along each branch before backtracking
    #

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)

    # Breadth-First Search (BFS)
    # It starts at the tree root and explores the neighbour nodes first, before moving to the next level


    def bfs(self):
        queue = []
        # queue.extend(self)
        queue.append(self)

        while queue: # if not empty
            current_node = queue.pop()
            print(current_node.value)

            if current_node.left_child:
                queue.append(current_node.left_child)

            if current_node.right_child:
                queue.append(current_node.right_child)


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)


if __name__ == "__main__":
    root = BinaryTree("root")
    root.insert_left("cat")
    root.insert_right("dog")
    cat = root.left_child
    dog = root.right_child
    cat.insert_left("cat1")
    cat.insert_right("cat2")
    dog.insert_left("dog1")
    dog.insert_right("dog2")

    # root.pre_order()
    root.bfs()
