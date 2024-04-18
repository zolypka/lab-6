class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

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
    linked_list.sort()
    print("Sorted linked list:")
    linked_list.display()


if __name__ == "__main__":
    main()