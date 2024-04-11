#1 LRU Cache
Initialization (__init__):
- Time Complexity: O(1)
- The initialization of the LRUCache class involves setting up the cache dictionary, head and tail sentinel nodes, and initializing other variables. Since these operations have a constant time complexity, the overall time complexity of initialization is O(1).

`get` Method:
- Time Complexity: O(1)
- When retrieving a value associated with a key from the cache, the get method performs the following operations:
     + Check if the key exists in the cache dictionary (O(1)).
     + If the key exists, remove the corresponding node from its current position in the linked list and move it to the front (O(1)).
- Since all operations involved in the get method (dictionary lookup and node manipulation) have constant time complexity, the overall time complexity is 0(1).

`put` Method: 
- Time Complexity: O(1)
- When putting a key-value pair into the cache, the put method performs the following operations:
    + Check if the key already exists in the cache dictionary (O(1)).
    + If the key exists, update the value and move the corresponding node to the front of the linked list (O(1)).
    + If the key doesn't exist and the cache is at capacity, evict the least recently used node from the cache (O(1)).
    + Add a new node to the front of the linked list and update the cache dictionary (O(1)).
- Since all these operations have constant time complexity, the overall time complexity of the put method is O(1).

#2 File Recursion
Initialization and Error Handling:
- Time Complexity: O(1)
- The function begins by checking if the provided path exists using os.path.exists(path). This operation has constant time complexity, as it involves a simple file system lookup.

File Search:
- Time Complexity: O(n)
- The function traverses the file system starting from the specified path using os.walk(path). This operation involves visiting each directory and file recursively.
- For each file encountered during the traversal, the function checks if the file's extension matches the provided suffix using file.endswith(suffix). This operation has constant time complexity.
- Since the function may potentially traverse all directories and files in the file system, the time complexity of the file search portion is linear with respect to the total number of files and directories in the file system, denoted as O(n).

#3 Huffman Coding
Node Class:
- Initialization: O(1)
- combine method: O(1)

PriorityQueue Class:
- Initialization: O(n log n), where n is the number of unique characters in the input string (sorting the priority queue).
- combine_nodes method: O(log n) on average, as it involves removing and adding elements from/to the priority queue.

HuffmanTree Class:
- Initialization: O(n log n), as it initializes a priority queue and builds the Huffman tree by combining nodes until a single root node remains.

HuffmanEncoder Class:
- Initialization: O(n), where n is the number of nodes in the Huffman tree. It traverses the tree to create an encoding table.
- encode method: O(m), where m is the length of the input text. It performs a constant-time lookup for each character in the encoding table.
- decode method: O(k * m), where k is the maximum length of any encoded character code, and m is the length of the encoded text. It iterates through the encoded text and performs a lookup in the reverse encoding table for each code.

Main Functions:
- `huffman_encoding`: O(n log n) to build the Huffman tree and O(m) to encode the input text, where n is the number of unique characters and m is the length of the input text.
- `huffman_decoding`: O(k * m) to decode the encoded text, where k is the maximum length of any encoded character code, and m is the length of the encoded text.

Overall, the time complexity of the Huffman encoding and decoding algorithms depends on the length of the input text (m) and the number of unique characters (n) in the text. The encoding process is more efficient than the decoding process due to the use of lookup tables. However, both operations are generally efficient and suitable for compressing textual data.

#4 Active Directory
Initialization of Group Object: O(1)
is_user_in_group Function:
- Initialization of variables: O(1)
- Loop through the group hierarchy: O(N), where N is the total number of groups and subgroups in the hierarchy.
- Checking if the user is in the current group: O(1) due to the use of a set for user storage.
- Adding visited groups to the set: O(1)
- Enqueuing subgroups: O(M), where M is the number of subgroups in the current group.

Therefore, the overall time complexity of the is_user_in_group function is O(N + M), where N is the total number of groups and M is the total number of subgroups.

The space complexity of this function is O(N), where N is the number of groups and subgroups, due to the usage of the visited set to keep track of visited groups. Additionally, the use of the deque for the queue contributes to the space complexity. However, since the users set and the groups list are specific to each group object, they don't significantly contribute to the space complexity of the function.

#5 Blockchain
Block Class:
- __init__: Initializes a block with data and the previous block (if any). It calculates the hash of the block based on its data, timestamp, and the hash of the previous block. Time complexity: O(1).
- calc_hash: Calculates the SHA-256 hash of the block. Time complexity: O(1).
- get_previous_hash and get_hash: Getter methods for previous hash and current hash. Time complexity: O(1).
- __str__: Returns a string representation of the block attributes. Time complexity: O(1).

Chain Class:
- __init__: Initializes the blockchain with a genesis block. Time complexity: O(1).
- create_genesis_block: Creates the genesis block with predefined data. Time complexity: O(1).
- append: Appends a new block to the blockchain. It creates a new block with the provided data and sets its previous block to the current tail. Time complexity: O(1).

Main Function:
- Appends multiple blocks with random data and one with a large random string. Time complexity for each append operation: O(1).

Therefore, the overall time complexity of creating the blockchain and appending blocks is O(N), where N is the number of blocks appended.

The space complexity of this implementation is O(N), where N is the number of blocks in the blockchain, as each block object occupies space in memory. Additionally, the space complexity is affected by the length of the large strings appended to the blocks.

#6 Union and Intersection
Node Class:
- __init__: Initializes a node with a value and a reference to the next node. Time complexity: O(1).

LinkedList Class:
- __init__: Initializes an empty linked list with a head node. Time complexity: O(1).
- `append`: Appends a new node with the given value to the end of the linked list. Time complexity: O(N), where N is the number of nodes in the linked list.
- `to_list`: Converts the linked list to a Python list. Time complexity: O(N), where N is the number of nodes in the linked list.

find_unique_values Function:
- Iterates through the linked list to find unique values using a set. Time complexity: O(N), where N is the number of nodes in the linked list.

union Function:
- Finds unique values in both linked lists and combines them into a new linked list. Time complexity: O(N1 + N2), where N1 and N2 are the number of nodes in the two linked lists.

intersection Function:
- Iterates through one linked list and checks if each value exists in the other linked list. Time complexity: O(N1 * N2), where N1 and N2 are the number of nodes in the two linked lists.

run_test_case Function:
- Prints the union and intersection of two linked lists as Python lists. Time complexity depends on the operations performed, but it does not add significant overhead to the overall time complexity.

Overall, the time complexity of the main operations (union and intersection) is dominated by the time complexity of finding unique values and iterating through the linked lists. Therefore, the overall time complexity is O(N1 + N2) for the union operation and O(N1 * N2) for the intersection operation, where N1 and N2 are the number of nodes in the two linked lists.

