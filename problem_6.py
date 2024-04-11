class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def find_unique_values(llist):
    values = set()
    current = llist.head
    while current:
        values.add(current.value)
        current = current.next
    return values

def union(llist_1, llist_2):
    values = find_unique_values(llist_1)
    values.update(find_unique_values(llist_2))

    result = LinkedList()
    for value in values:
        result.append(value)
    return result

def intersection(llist_1, llist_2):
    values_1 = find_unique_values(llist_1)

    result = LinkedList()
    current = llist_2.head
    while current:
        if current.value in values_1:
            result.append(current.value)
        current = current.next
    return result

# Test cases
def run_test_case(llist_1, llist_2):
    print("Union:", llist_1.to_list() + llist_2.to_list())
    intersection_values = set(llist_1.to_list()).intersection(llist_2.to_list())
    print("Intersection:", list(intersection_values))

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)
print("Test Case 1:")
run_test_case(linked_list_1, linked_list_2)

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print("Test Case 2:")
run_test_case(linked_list_3, linked_list_4)
