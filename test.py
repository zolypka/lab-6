from main import LinkedList

def test_add_node():
    linked_list = LinkedList()
    linked_list.add_node(5)
    assert linked_list.head.data == 5

def test_display():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    assert linked_list.display() == [1, 2, 3]

def test_iter():
    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    elements = [node.data for node in linked_list]
    assert elements == [1, 2, 3]