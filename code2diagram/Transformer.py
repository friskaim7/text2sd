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

def class_member_to_string(class_name, class_member):
    access_mod = determine_access_mod(class_member["access_mod"])
    static_string = determine_static_mod(class_member["static_mod"])
    name = class_member["name"]

    if "return_type" in class_member:
        return_type = class_member["return_type"]
        param_string = ""
        params = class_member["params"]
        print(params)
        for param in params:
            param_name = param["name"]
            param_type = param["type"]
            param_string += f"{param_name}: {param_type},"
        param_string = param_string.rstrip(",")  # Remove trailing commas
        return f"{class_name} : {access_mod} {static_string} {return_type} {name}({param_string})\n"
    else:
        var_type = class_member["type"]
        return f"{class_name} : {access_mod} {static_string} {var_type} {name}\n"

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
                class_name = class_info.get("name", "")
                output_file.write(f"class {class_name}\n")

                # Write class fields/variables
                class_vars = class_info.get("vars", [])
                for class_var in class_vars:
                    output_file.write(class_member_to_string(class_name, class_var))
                
                # Write class methods
                methods = class_info.get("methods", [])
                for method in methods:
                    output_file.write(class_member_to_string(class_name, method))

        output_file.write("@enduml\n")

print(f"Class names from '{input_filepath}' have been saved to {output_filepath}.")
