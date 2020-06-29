"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        # if value < self.value and self.left is None:
        #     self.left = BSTNode(value)
        # if value >= self.value and self.right is None:
        #     self.right = BSTNode(value)

        # if value is < less than self.value
        if value < self.value:
            # go left
            # check if left has value
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

            # go right
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value >= target
        # found = False
        if self.value >= target:
            # check the left subtree
            # if you cannot go left, return false
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            # check if right subtree contains target
            # if you cannot go right, return false
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
        # check that there are values on right
        # while there are values

        # current = self
        #
        # while current.right is not None:
        #     current = current.right
        # return current.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # if exists check left
        if self.left is not None:
            # call .for_each(fn)
            self.left.for_each(fn)
        # check right
        if self.right is not None:
            # call .for_each(fn)
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
            # if self has a 'left', self is BIGGER
        if self.left:
            self.left.in_order_print(self)

        print(self.value)

        # if self has a 'right', self is SMALLER
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        # add the first node to the queue
        q = []
        q.append(self)
        # while queue is not empty
        while len(q) > 0:
            # remove the first node from the queue
            current = q.pop(0)
            # print the removed node
            print(current.value)
            # add all children into the queue
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(self)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from teh top of the stack
            current = stack.pop(len(stack) - 1)
            # print that node
            print(current.value)
            # add all children to the stack
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            # keep in mind, the order you add the children, will matter

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
