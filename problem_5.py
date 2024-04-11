import hashlib
import datetime
import random
import string

class Block:
    def __init__(self, data, previous_block=None):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_block.hash if previous_block else 0
        self.hash = self.calc_hash()
        self.previous_block = previous_block

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) +
                    str(self.data) +
                    str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_previous_hash(self):
        return self.previous_hash

    def get_hash(self):
        return self.hash

    def __str__(self):
        return (f"\nBlock Attributes:"
                f"\n   timestamp: {self.timestamp}"
                f"\n   data: {self.data}"
                f"\n   previous hash: {self.previous_hash}"
                f"\n   hash: {self.hash}")

class Chain:
    def __init__(self):
        self.tail = self.create_genesis_block()

    def create_genesis_block(self):
        return Block("1) the singularity")

    def append(self, data):
        if data is None or data == "":
            return False
        new_block = Block(data, self.tail)
        self.tail = new_block
        return True

def main():
    chain = Chain()
    
    # Test Cases
    chain.append(random.randint(1, 9999))
    chain.append(random.randint(1, 9999))
    chain.append(random.randint(1, 9999))
    chain.append(random.randint(1, 9999))
    chain.append("")  # Empty data
    
    # Append a block with a large random string
    data = ''.join(random.choices(string.ascii_letters, k=10000))
    chain.append(data)
    
    # Append a block with a very large string
    data = ''.join(random.choices(string.ascii_letters, k=10000))
    chain.append(data)
    
    print("\n-----Block Chain (linked list test)-----")
    print("Going backwards through the blockchain")
    
    node = chain.tail
    while node:
        print(node)
        node = node.previous_block

if __name__ == "__main__":
    main()
