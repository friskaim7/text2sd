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

def params_to_string(params):
    param_string = ""
    for param in params:
        param_name = param["name"]
        param_type = param["type"]
        param_string += f" {param_name}: {param_type},"
    return param_string.strip(" ,") # Trailing comma and whitespace removed

def split_called_method_name(calling_method):
    cm_list = calling_method.split()
    cm_list.remove("from")
    method_name = cm_list.pop(0)
    full_class_name = " ".join(cm_list)

    return method_name, full_class_name

def split_called_method_name_list(calling_method_list):
    # define output variables
    method_name_list = []
    full_class_name_list = []

    # Iterate each method 
    for calling_method in calling_method_list:
        method_name, full_class_name = split_called_method_name(calling_method)
        
        # Store split result to the approriate list
        method_name_list.append(method_name)
        full_class_name_list.append(full_class_name)

    return method_name_list, full_class_name_list

def class_member_to_string(class_name, class_member):
    access_mod = determine_access_mod(class_member["access_mod"])
    static_string = determine_static_mod(class_member["static_mod"])
    name = class_member["name"]

    # Identify whether class_member represents a field or a method.
    if "return_type" in class_member:
        return_type = class_member["return_type"]
        param_string = params_to_string(class_member["params"])
        return f"{class_name} : {access_mod} {static_string} {return_type} {name}({param_string})\n"
    else:
        var_type = class_member["type"]
        return f"{class_name} : {access_mod} {static_string} {var_type} {name}\n"

with open(input_filepath, 'r', encoding='cp437') as input_file:
    data = json.load(input_file)
    with open(output_filepath, 'a') as output_file:
        # output_file.write("@startuml Class Diagram\n")

        # iterate each file data
        for package_data in data:
            package_name = package_data.get("package_name", "")
            classes = package_data.get("classes", [])

            # iterate each class
            for class_info in classes:
                # Write class name to the text file
                class_name = class_info.get("name", "")
                # output_file.write(f"class {class_name}\n")
                print("==========")
                print(class_name)

                # Write class fields
                class_vars = class_info.get("vars", [])
                for class_var in class_vars:
                    # output_file.write(class_member_to_string(class_name, class_var))
                    break
                
                # Write class methods
                methods = class_info.get("methods", [])
                for method in methods:
                    # output_file.write(class_member_to_string(class_name, method))
                    print("-----")
                    called_method_name, full_class_name = split_called_method_name_list(method["calling"])
                    print(f"{called_method_name} - {full_class_name}")

                # TODO:
                # Write class relationships

        # output_file.write("@enduml\n")

print(f"Class names from '{input_filepath}' have been saved to {output_filepath}.")
