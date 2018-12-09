class Node:
    def __init__(self, number_of_children, number_of_metadata_entries):
        self.children = [None] * number_of_children
        self.metadata = [None] * number_of_metadata_entries

def create_node(tree):
    number_of_children = tree[0]
    number_of_metadata_entries = tree[1]
    node = Node(number_of_children, number_of_metadata_entries)
    tree = tree[2:]
    for i in range(number_of_children):
        tree, node.children[i] = create_node(tree)
    for i in range(number_of_metadata_entries):
        node.metadata[i] = tree[i]
    tree = tree[number_of_metadata_entries:]
    return tree, node

def count_metadata_1(node):
    metadata_sum = 0
    metadata_sum += sum(node.metadata)
    for i in range(len(node.children)):
        metadata_sum += count_metadata_1(node.children[i])
    return metadata_sum

def count_metadata_2(node):
    metadata_sum = 0
    number_of_children = len(node.children)
    if node.children:
        for entry in node.metadata:
            if entry <= number_of_children:
                metadata_sum += count_metadata_2(node.children[entry-1])
    else:
        metadata_sum += sum(node.metadata)
    return metadata_sum

f = open('input', 'r')
tree = f.readline()
tree = tree.split()
tree = list(map(int,tree))
tree, root = create_node(tree)

metadata_sum_1 = count_metadata_1(root)
print('Part One:')
print(f'Sum of metadata {metadata_sum_1}.')

metadata_sum_2 = count_metadata_2(root)
print('Part Two:')
print(f'Sum of metadata {metadata_sum_2}.')