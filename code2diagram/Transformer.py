import json
from pprint import pprint

input_filepath = "code2diagram/resource/input.json"
output_filepath = "code2diagram/out/class_diagram.puml"

def determine_access_mod(access_mod):
    access_modifiers = {
        "public": "+",
        "protected": "#",
        "default": "~",
        "private": "-"
    }
    return access_modifiers[access_mod]

def determine_static_mod(var_static_mod):
    static_string = ""
    if var_static_mod:
        static_string = "{static}"
    return static_string

def class_var_to_write(class_var):
    c_var_access_mod = determine_access_mod(class_var["class_var_access_mod"])
    static_string = determine_static_mod(class_var["class_static_mod"])
    c_var_type = class_var["class_var_type"]
    c_var_name = class_var["class_var_name"]    
                        
    return f"{class_name} : {c_var_access_mod} {static_string} {c_var_type} {c_var_name}\n"

with open(input_filepath) as input_file:
    data = json.load(input_file)
    with open(output_filepath, 'a') as output_file:
        output_file.write("@startuml Class Diagram\n")

        # iterate each file data
        for package_data in data:
            package_name = package_data.get("package_name", "")
            classes = package_data.get("classes", [])

            # iterate each class
            for class_info in classes:
                # Write class name to the text file
                class_name = class_info.get("class_name", "")
                output_file.write(f"class {class_name}\n")

                # Write class fields/variables
                class_vars = class_info.get("class_vars", [])
                for class_var in class_vars:
                    output_file.write(class_var_to_write(class_var))
                
                # Write class methods
                methods = class_info.get("methods", [])

        output_file.write("@enduml\n")

print(f"Class names from '{input_filepath}' have been saved to {output_filepath}.")
