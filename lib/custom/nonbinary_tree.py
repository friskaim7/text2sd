""" This file containing the functions needed to build an n-ary tree from a file """
class TreeNode:
    """ Define class for n-ary tree nodes """
    def __init__(self, data):
        self.data = data
        self.children = []

def build_tree_from_file(file):
    """ Build an n-ary tree with lines from file as nodes """
    root = None
    current_node = None
    stack = []
    for line in file:
        # Ignore lines starting with ' or empty lines
        if line.startswith("'"):
            continue

        # 1 tab = 4 spaces
        indent_level = (len(line) - len(line.lstrip()))/4

        node_data = line.strip()
        new_node = TreeNode(node_data)

        if indent_level == 0:
            root = new_node
            stack = [root]
        else:
            while len(stack) > indent_level:
                stack.pop()

            current_node = stack[-1]
            current_node.children.append(new_node)
            stack.append(new_node)

    return root

def print_tree(node, indent=0):
    """ Print the generated n-ary tree """
    if node is not None:
        print("  " * indent + node.data)
        for child in node.children:
            print_tree(child, indent + 1)
