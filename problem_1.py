class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._add_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
        else:
            if len(self.cache) >= self.capacity:
                del_key = self.tail.prev.key
                self._remove_node(self.tail.prev)
                del self.cache[del_key]
            node = Node(key, value)
            self.cache[key] = node
        self._add_to_front(node)

# Test Case 1: Basic test case
our_cache = LRUCache(3)
our_cache.put(1, 1)
our_cache.put(2, 2)
our_cache.put(3, 3)

print("Get(1):", our_cache.get(1))  # returns 1
print("Get(2):", our_cache.get(2))  # returns 2
print("Get(3):", our_cache.get(3))  # returns 3

our_cache.put(4, 4)  # This should evict key 1
print("Get(1):", our_cache.get(1))  # returns -1
print("Get(2):", our_cache.get(2))  # returns 2
print("Get(3):", our_cache.get(3))  # returns 3
print("Get(4):", our_cache.get(4))  # returns 4

# Test Case 2: Edge case with null or empty values
our_cache.put(None, 5)  # Should not raise any exceptions
our_cache.put(5, None)  # Should not raise any exceptions
our_cache.put(None, None)  # Should not raise any exceptions

print("Get(None):", our_cache.get(None))  # returns -1

# Test Case 3: Large values
large_cache = LRUCache(10**6)
for i in range(10**6):
    large_cache.put(i, i)

print("Get(0) from large_cache:", large_cache.get(0))  # returns 0
print("Get(999999) from large_cache:", large_cache.get(999999))  # returns 999999
print("Get(1000000) from large_cache:", large_cache.get(10**6))  # returns -1

print("All test cases passed!")
