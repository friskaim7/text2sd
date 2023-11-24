""" This file containing the functions needed to convert .txt file into .puml and .png """

import os
import subprocess as sp
import sys
from lib.custom.nonbinary_tree import build_tree_from_file

PLANTUML_PATH = "lib/plantuml-1.2023.10.jar"
IMAGE_OUTPUT_PATH = "../img"
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
    # if return part is not empty, then take the return property
    if len(method_return_raw) > 1:
        ret_raw = method_return_raw[1]
        line_prop[RETURN] = ret_raw[:-1].strip() if ret_raw.endswith(":") else ret_raw.strip()
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

def save_to_puml(puml_output_file, node, parent=None):
    """" Save inputed tree into a puml file with PlantUML sequence diagram syntax"""
    if node is not None:
        puml_output_file.write(get_formatted_caller(parent, node) + '\n')
        for child in node.children:
            save_to_puml(puml_output_file, child, node)
        puml_output_file.write(get_formatted_return(parent, node) + '\n')

def convert_puml_to_image(input_puml_path, output_path):
    """ Convert generated puml file into an image"""
    try:
        # Use Java to execute the PlantUML JAR file
        sp.run(["java", "-jar", PLANTUML_PATH, input_puml_path, "-o", output_path], check=True)
    except sp.CalledProcessError as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python text2sd.py input_file_directory\ni.e. "py text2sd.py input-sample/"\n')
        sys.exit(1)

    # Extract input file name from command-line arguments
    input_directory = sys.argv[1]

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            # Construct the full path for the file
            input_file_path = os.path.join(input_directory, filename)

            # Extract only the filename from the path (excluding extension)
            input_filename, _ = os.path.splitext(os.path.basename(input_file_path))
            output_file_path = f"./out/puml/[SD] {input_filename}.puml"
        else:
            print(f'"{filename}" is not a .txt file and cannot be processed.')

        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            tree_root = build_tree_from_file(input_file)

            with open(output_file_path, "w", encoding='utf-8') as puml_file:
                puml_file.write(f"@startuml {input_filename}\n")
                save_to_puml(puml_file, tree_root)
                puml_file.write("@enduml\n")

        print(f'PlantUML File saved to\t"{output_file_path}"')
        convert_puml_to_image(output_file_path, IMAGE_OUTPUT_PATH)
        print(f'Sequence Diagram saved to "./out/img/[SD] {input_filename}.png"')
 