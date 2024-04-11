import collections

class Node:
    def __init__(self, char=None, frequency=0):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def combine(self, other):
        combined_frequency = self.frequency + other.frequency
        combined_node = Node(frequency=combined_frequency)
        combined_node.left = self if self.frequency <= other.frequency else other
        combined_node.right = other if self.frequency <= other.frequency else self
        return combined_node

class PriorityQueue:
    def __init__(self, string):
        counter = collections.Counter(string)
        self.queue = [Node(char=char, frequency=freq) for char, freq in counter.items()]
        self.queue.sort(key=lambda x: x.frequency)

    def combine_nodes(self):
        node1 = self.queue.pop(0)
        node2 = self.queue.pop(0)
        combined_node = node1.combine(node2)
        self.queue.append(combined_node)
        self.queue.sort(key=lambda x: x.frequency)

class HuffmanTree:
    def __init__(self, queue):
        while len(queue.queue) > 1:
            queue.combine_nodes()
        self.root = queue.queue[0]

    def convert_to_binary(self):
        self._assign_binary_code(self.root, '')

    def _assign_binary_code(self, node, code):
        if node is None:
            return
        node.code = code
        self._assign_binary_code(node.left, code + '0')
        self._assign_binary_code(node.right, code + '1')

class HuffmanEncoder:
    def __init__(self, tree):
        self.encoding_table = {}
        self._create_encoding_table(tree.root, '')

    def _create_encoding_table(self, node, code):
        if node is None:
            return
        if node.char is not None:
            self.encoding_table[node.char] = code
        self._create_encoding_table(node.left, code + '0')
        self._create_encoding_table(node.right, code + '1')

    def encode(self, text):
        return ''.join(self.encoding_table[char] for char in text)

    def decode(self, encoded_text):
        reverse_table = {code: char for char, code in self.encoding_table.items()}
        decoded_text = ''
        current_code = ''
        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_table:
                decoded_text += reverse_table[current_code]
                current_code = ''
        return decoded_text

def huffman_encoding(data):
    if not data:
        print("Please provide a non-empty string.")
        return None, None
    queue = PriorityQueue(data)
    tree = HuffmanTree(queue)
    tree.convert_to_binary()
    encoder = HuffmanEncoder(tree)
    encoded_data = encoder.encode(data)
    return encoded_data, encoder

def huffman_decoding(data, encoder):
    if encoder is None:
        print("Encoder not provided.")
        return None
    return encoder.decode(data)

# Test Case 1: Empty string
print("Test Case 1 (Empty string):")
data = ""
print("Input: {}".format(data))
encoded_data, encoder = huffman_encoding(data)
print("Encoded data: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, encoder)
print("Decoded data: {}".format(decoded_data))
print()

# Test Case 2: None value
print("Test Case 2 (None value):")
data = None
print("Input: {}".format(data))
encoded_data, encoder = huffman_encoding(data)
print("Encoded data: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, encoder)
print("Decoded data: {}".format(decoded_data))
print()

# Test Case 3: Long sentence
print("Test Case 3 (Long sentence):")
data = "New one in, old one out."
print("Input: {}".format(data))
encoded_data, encoder = huffman_encoding(data)
print("Encoded data: {}".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, encoder)
print("Decoded data: {}".format(decoded_data))
