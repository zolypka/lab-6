class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __lt__(self, other):
        return self.data < other.data


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


def main():
    linked_list = LinkedList()
    data = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    for item in data:
        linked_list.add_node(item)
    print("Unsorted linked list:")
    linked_list.display()

    sorted_list = sorted([node.data for node in linked_list])
    sorted_linked_list = LinkedList()
    for item in sorted_list:
        sorted_linked_list.add_node(item)

    print("Sorted linked list:")
    sorted_linked_list.display()


if __name__ == "main":
    main()