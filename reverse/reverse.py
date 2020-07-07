class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev=None):
        if node is None:  # handles empty linked list
            return node

        if node.next_node is None:  # handles linked list with one node
            return node

        # label the end node as the new head node
        new_head = self.reverse_list(node.next_node)

        # set the new head node's next_node to be the previous, head node (which is now the end node)
        node.next_node.next_node = node

        # set the old head node's next_node to None, which makes it the end node
        node.next_node = None

        return new_head



        # current = self.head
        # while current is not None:
        #     next = current.next_node
        #     current.next_node = prev
        #     prev = current
        #     current = next
        # self.head = prev

