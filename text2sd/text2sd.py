""" This file containing the functions needed to convert .txt file into .puml """

from nonbinary_tree import build_tree_from_file

INPUT_FILENAME = "./text2sd/sample/[Input] Sample.txt"
OUTPUT_FILENAME = "./text2sd/output/sample.puml"
CLASS = "cls"
METHOD = "method"
RETURN = "ret"

def count_ltab(line):
    """Return the number of leading tab in a string"""
    return line.lstrip().count('\t')

def has_colon(line):
    """Comfirm if the given line has any number of colon in any position"""
    return ':' in line

def has_return(line):
    """Comfirm if the given line has any number of ">>" in any position"""
    return ">>" in line

def property_identifier(line):
    """	Return class, method, and return """
    line_prop = {CLASS: "", METHOD: "", RETURN: ""}
    if line is None:
        return line_prop
    class_rest = line.split('.')
    method_return_raw = class_rest[1].split(" >> ")
    line_prop[CLASS] = class_rest[0].strip()
    line_prop[METHOD] = method_return_raw[0].strip()
    line_prop[RETURN] = method_return_raw[1][:-1].strip() if method_return_raw[1].endswith(":") else method_return_raw[1].strip()
    return line_prop

def formatting_passer(parent, child):
    """ A helper function for parentless nodes"""
    if parent is None:
        return None, child.data
    return parent.data, child.data

def get_output_props(caller_node, called_node):
    """Get line properties for both caller and called method """
    caller_line, called_line = formatting_passer(caller_node,called_node)
    caller_prop = property_identifier(caller_line)
    called_prop = property_identifier(called_line)
    return caller_prop, called_prop

def get_formatted_caller(caller_node, called_node):
    """ Format inputed caller and called lines into PlantUML sequence diagram call syntax"""
    caller_prop, called_prop = get_output_props(caller_node, called_node)
    return f"{caller_prop[CLASS]} -> {called_prop[CLASS]}: {called_prop[METHOD]}"

def get_formatted_return(caller_node, called_node):
    """ Format inputed caller and called lines into PlantUML sequence diagram return syntax"""
    caller_prop, called_prop = get_output_props(caller_node, called_node)
    return f"{caller_prop[CLASS]} <-- {called_prop[CLASS]}: {called_prop[RETURN]}"

def save_to_puml(puml_file, node, parent=None):
    """" Save inputed tree into a puml file with PlantUML sequence diagram syntax"""
    if node is not None:
        puml_file.write(get_formatted_caller(parent, node) + '\n')
        for child in node.children:
            save_to_puml(puml_file, child, node)
        puml_file.write(get_formatted_return(parent, node) + '\n')


def main():
    """ Run the program """
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as input_file:
        tree_root = build_tree_from_file(input_file)
        with open(OUTPUT_FILENAME, "w", encoding='utf-8') as puml_file:
            save_to_puml(puml_file, tree_root)

if __name__ == "__main__":
    main()
