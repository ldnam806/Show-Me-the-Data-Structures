from collections import deque

class Group:
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.users = set()

def is_user_in_group(user, group):
    
    visited = set()
    queue = deque([group])

    while queue:
        current_group = queue.popleft()
        if user in current_group.users:
            return True
        visited.add(current_group)
        queue.extend(subgroup for subgroup in current_group.groups if subgroup not in visited)

    return False

# Creating group hierarchy
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child.users.add("sub_child_user")

child.groups.append(sub_child)
parent.groups.append(child)

# Test Case 1: User is in a subgroup
print(is_user_in_group("sub_child_user", parent))  # True

# Test Case 2: User is not in the group
print(is_user_in_group("non_existent_user", parent))  # False

# Test Case 3: User is in the root group
print(is_user_in_group("sub_child_user", sub_child))  # True
