class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def build_tree_from_file(file):
    root = None
    current_node = None
    stack = []
    for line in file:
        line = line.rstrip('\n')
        indent_level = line.count('\t')

        node_data = line.lstrip('\t')
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
    if node is not None:
        print("  " * indent + node.data)
        for child in node.children:
            print_tree(child, indent + 1)

# Example usage
# file_path = "./text2sd/sample/[Input] Sample.txt"
# tree_root = build_tree_from_file(file_path)
# print_tree(tree_root)
