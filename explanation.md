#1 LRU Cache
Class Definition:

Node: This class represents a node in a doubly linked list. Each node contains a key-value pair and pointers to the previous and next nodes.
LRUCache: This class implements the LRU cache using a combination of a hashmap and a doubly linked list. It includes methods for __init__, get, and put.
Initialization (__init__):

In the __init__ method, the LRUCache class is initialized with a given capacity. It sets up a hashmap (self.cache) to store key-value pairs and a doubly linked list (self.head and self.tail) to maintain the order of items based on their usage.
Get Method (get):

The get method retrieves the value associated with a given key from the cache.
If the key exists in the cache, it moves the corresponding node to the front of the doubly linked list to indicate that it's the most recently used item.
If the key does not exist, it returns -1.
Put Method (put):

The put method inserts a new key-value pair into the cache.
If the key already exists in the cache, it updates the value and moves the corresponding node to the front of the doubly linked list.
If the key does not exist and the cache is full, it removes the least recently used item from the end of the doubly linked list and the corresponding entry from the hashmap before adding the new item.
If the cache is not full, it simply adds the new item to the front of the doubly linked list and the hashmap.
Test Cases:

Test Case 1: Basic Test Case:

This test case verifies the basic functionality of the LRUCache class.
It adds key-value pairs to the cache, retrieves values using the get method, and checks if the cache behaves correctly when it reaches its capacity.
The output of each get operation is printed on the console.
Test Case 2: Edge Case with Null or Empty Values:

This test case checks if the LRUCache class handles null or empty values correctly.
It inserts null or empty key-value pairs into the cache and verifies that the get method returns -1 for non-existent keys.
Test Case 3: Large Values:

This test case checks the LRUCache class's performance with a large capacity.
It creates a cache with a capacity of 10^6 and inserts key-value pairs from 0 to 10^6 - 1.
It retrieves values for specific keys and verifies that the get method behaves as expected.
Output:

The output of each test case is printed on the console, showing the results of the get operations and whether all test cases passed.

#2 File Recursion
Function Description:

The find_files function recursively searches for all files beneath a given path with a specified file name suffix.
It takes two parameters: suffix (the suffix of the file name to be found) and path (the path of the file system to search).
The function returns a list of paths to files with the specified suffix.
Function Algorithm:

The function starts by checking if the specified path exists. If not, it returns an empty list.
It traverses the directory structure starting from the given path using the os.walk function.
For each file encountered, it checks if the file name ends with the specified suffix. If it does, the file's path is added to the result list.
Test Cases:

Test Case 1: Basic test case:

Verifies the basic functionality of the find_files function by searching for files with a specific suffix in a test directory.
Test Case 2: Edge case with null or empty values:

Handles edge cases where the path and/or suffix are null or empty strings, ensuring the function handles them gracefully.
Test Case 3: Large values:

Tests the function's performance with a large path (such as the entire file system), evaluating its efficiency in handling large-scale scenarios.
Output:

The output of each test case is printed on the console, displaying the list of paths to files with the specified suffix or an empty list for edge cases.
The output allows verification of the function's correctness, handling of edge cases, and performance in large-scale scenarios.
Overall, the find_files function provides a flexible and efficient way to search for files with a specified suffix in a directory structure, making it useful for various file management tasks.

#3 Huffman Coding
Huffman Encoding Code:

The code implements the Huffman encoding algorithm, which generates variable-length codes for characters based on their frequencies in the input data.
It consists of classes for Node, PriorityQueue, HuffmanTree, and HuffmanEncoder, each responsible for different aspects of the encoding process.
The huffman_encoding and huffman_decoding functions orchestrate the encoding and decoding processes, respectively.
Test Case 1 (Empty string):

This test case verifies the behavior of the encoding and decoding functions when an empty string is provided as input.
It prints the input data, the encoded data, and the decoded data to demonstrate the behavior of the Huffman encoding and decoding.
Test Case 2 (None value):

This test case examines how the encoding and decoding functions handle a None value as input.
Similar to the first test case, it prints the input data, encoded data, and decoded data to observe the behavior.
Test Case 3 (Long sentence):

This test case evaluates the performance of the encoding and decoding functions on a long sentence as input.
It provides a lengthy string as input, representing a typical use case scenario, and examines the encoded and decoded results.
Each test case follows a similar structure:

It sets up the input data.
It calls the huffman_encoding function to encode the data.
It prints the encoded data.
It calls the huffman_decoding function to decode the encoded data.
It prints the decoded data.
These test cases collectively ensure that the Huffman encoding code functions correctly under various input scenarios, including edge cases like empty strings and None values.

#4 Active Directory
Avoiding Redundant Operations:

In the Group class, we removed the getter methods (get_groups, get_users, and get_name) as they were simply returning the attributes directly accessible by the class instances.
By directly accessing the users and groups attributes, we eliminate the overhead of method calls, making the code more efficient and readable.
Simplify BFS Implementation:

We simplified the breadth-first search (BFS) implementation in the is_user_in_group function.
Instead of using recursion, we utilized a visited set to keep track of visited groups during BFS traversal.
The BFS traversal starts from the group parameter and iteratively explores its subgroups.
The queue is initialized with the root group (group) and is updated with each subgroup encountered during traversal.
By using a set to track visited groups, we ensure that each group is visited only once, preventing redundant traversal and improving efficiency.
If the user is found in any group, the function returns True; otherwise, it returns False after checking all groups.

#5 Blockchain
Block Class:

Represents a single block in the blockchain.
Attributes:
timestamp: Timestamp of when the block was created.
data: Data stored in the block.
previous_hash: Hash of the previous block in the chain.
hash: Hash of the current block.
Methods:
calc_hash(): Calculates the hash of the block based on its attributes.
get_previous_hash(): Returns the hash of the previous block.
get_hash(): Returns the hash of the current block.
__str__(): Returns a string representation of the block.
Chain Class:

Manages the blockchain by maintaining the linked list of blocks.
Attributes:
tail: Points to the last block in the chain.
Methods:
create_genesis_block(): Creates the genesis block (the first block in the chain).
append(data): Appends a new block to the chain with the given data.
Main Function:

Creates a blockchain (Chain object).
Appends several blocks with random data to the chain.
Prints the attributes of each block in reverse order, starting from the last block (tail).
Overall, this code demonstrates a basic implementation of a blockchain using linked list structure. Each block contains data and a hash of the previous block, ensuring the integrity and immutability of the blockchain. The Chain class manages the chain by adding new blocks and maintaining a reference to the last block. Finally, the main function tests the functionality by appending blocks and printing their attributes.

#6 Union and Intersection
LinkedList Class:

We defined a LinkedList class to represent a linked list data structure.
It contains an append method to add elements to the end of the linked list.
We added a to_list method to convert the linked list into a Python list of values.
find_unique_values Function:

This function takes a linked list as input and returns a set containing unique values from the linked list.
union Function:

The union function takes two linked lists as input.
It calls the find_unique_values function on each linked list to get the unique values.
Then, it combines the unique values from both linked lists using the update method of sets.
Finally, it returns a new linked list containing the union of the unique values.
intersection Function:

The intersection function also takes two linked lists as input.
It first extracts the unique values from the first linked list using find_unique_values.
Then, it iterates through the nodes of the second linked list and checks if each value exists in the set of unique values from the first linked list.
If a value is found in both linked lists, it adds it to the result set.
Finally, it returns a new linked list containing the intersection of the unique values.
run_test_case Function:

This function takes two linked lists as input and prints the union and intersection of their elements.
It converts both linked lists into Python lists using the to_list method.
For the union, it concatenates the lists.
For the intersection, it converts both lists into sets, finds the common elements using the intersection method, and converts the result back to a list.

