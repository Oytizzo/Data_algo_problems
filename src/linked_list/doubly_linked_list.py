class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return repr(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ','.join(nodes)

    def append(self, data):
        pass

    def prepend(self, data):
        pass

    def search(self, item):
        pass

    def remove_node(self, node):
        pass

    def remove(self, item):
        pass
