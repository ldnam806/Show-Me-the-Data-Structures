import os

def find_files(suffix, path):
    if not os.path.exists(path):
        return []

    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(suffix):
                result.append(os.path.join(root, file))
    return result

# Test Case 1: Basic test case
print("Test Case 1:")
print(find_files('.txt', './testdir'))

# Test Case 2: Edge case with null or empty values
print("\nTest Case 2:")
print(find_files('', ''))  # Empty path and suffix
print(find_files('.txt', ''))  # Empty path

# Test Case 3: Large values
print("\nTest Case 3:")
print(find_files('.txt', '/'))  # Search the entire file system (be cautious with this)