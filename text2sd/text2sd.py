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
    class_rest = line.split('.')
    method_return_raw = class_rest[1].split(" >> ")
    line_prop[CLASS] = class_rest[0].strip()
    line_prop[METHOD] = method_return_raw[0].strip()
    line_prop[RETURN] = method_return_raw[1][:-1].strip() if method_return_raw[1].endswith(":") else method_return_raw[1].strip()
    return line_prop


def formatted_caller(caller, called):
    caller_prop = property_identifier(caller)
    called_prop = property_identifier(called)
    return f"{caller_prop[CLASS]} -> {called_prop[CLASS]}: {called_prop[METHOD]}"

def formatted_return(caller, called):
    caller_prop = property_identifier(caller)
    called_prop = property_identifier(called)
    return f"{caller_prop[CLASS]} <-- {called_prop[CLASS]}: {called_prop[RETURN]}"

# def process(file, caller_line="", called_line=""):
#     print(formatted_caller(caller_line, called_line))
#     print(formatted_return(caller_line, called_line))

def print_tree(node, indent=0):
    if node is not None:
        print("  " * indent + node.data)
        for child in node.children:
            print_tree(child, indent + 1)


def main():
    """ Run the program """
    tree_root = build_tree_from_file(INPUT_FILENAME)
    print_tree(tree_root)


if __name__ == "__main__":
    main()