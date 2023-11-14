""" This file containing the function needed to convert .txt file into .puml """

import re
from nonbinary_tree import build_tree_from_file

INPUT_FILENAME = "./text2sd/sample/[Input] Sample.txt"
CLASS = "cls"
METHOD = "method"
RETURN = "ret"

def count_ltab(line):
    """Return the number of leading tab in a string"""
    return line.lstrip().count('\t')

def has_colon(line):
    return ':' in line

def has_return(line):
    return ">>" in line

def property_identifier2(line):
    pattern = r"\s*(?P<cls>\w+)\.(?P<method>[\w(), ]+)\s>>\s(?P<ret>[\w<>]+):?"
    matches = re.match(pattern, line)
    return matches.groupdict() if matches else None

def property_identifier(line):
    """	return class, method, and return """
    line_prop = {CLASS: "", METHOD: "", RETURN: ""}
    if line is None:
        return line_prop
    class_rest = line.split('.')
    method_return_raw = class_rest[1].split(" >> ")
    line_prop[CLASS] = class_rest[0].strip()
    line_prop[METHOD] = method_return_raw[0].strip()
    line_prop[RETURN] = method_return_raw[1][:-1].strip() if method_return_raw[1].endswith(":") else method_return_raw[1].strip()
    return line_prop


def formatted_caller(caller_node, called_node):
    caller_line, called_line = formatting_passer(caller_node,called_node)
    caller_prop = property_identifier(caller_line)
    called_prop = property_identifier(called_line)
    return f"{caller_prop[CLASS]} -> {called_prop[CLASS]}: {called_prop[METHOD]}"

def formatted_return(caller_node, called_node):
    caller_line, called_line = formatting_passer(caller_node,called_node)
    caller_prop = property_identifier(caller_line)
    called_prop = property_identifier(called_line)
    return f"{caller_prop[CLASS]} <-- {called_prop[CLASS]}: {called_prop[RETURN]}"

def print_tree(node, indent=0):
    if node is not None:
        print("  " * indent + node.data)
        for child in node.children:
            print_tree(child, indent + 1)

def formatting_passer(parent, child):
    if parent is None:
        return None, child.data
    else:
        return parent.data, child.data

def print_custom(node, parent=None):
    if node is not None:
        print(formatted_caller(parent, node))
        for child in node.children:
            print_custom(child, node)
        print(formatted_return(parent, node))

def save_to_puml(puml_file, node, parent=None):
    if node is not None:
        print(formatted_caller(parent, node))
        puml_file.write(formatted_caller(parent, node) + '\n')
        for child in node.children:
            save_to_puml(puml_file, child, node)
        print(formatted_return(parent, node))
        puml_file.write(formatted_return(parent, node) + '\n')
    

def main():
    """ Run the program """
    tree_root = build_tree_from_file(INPUT_FILENAME)
    print_tree(tree_root)
    print("\n==========\n")
    with open("./text2sd/output/sample.puml", "w") as puml_file:
        save_to_puml(puml_file, tree_root)


if __name__ == "__main__":
    main()