import json
from pprint import pprint

input_file_name = "code2diagram/resource/input.json"

with open(input_file_name) as json_file:
    data = json.load(json_file)
    # pprint(data)
    # for filedata in data:
    #     filedata[]

    for package_data in data:
        file_relative_path = package_data.get("file_relative_path", "")
        
        for package_name, classes in package_data.items():
            print("package_name: " + package_name)
            print("classes: " + classes)
            if package_name != "file_relative_path":
                for class_info in classes:
                    for class_name, class_data in class_info.items():
                        print("File Relative Path:", file_relative_path)
                        print("Package Name:", package_name)
                        print("Class Name:", class_name)
                        
                        # class_variables = class_data.get("class_variables", [])
                        # methods = class_data.get("methods", [])
                        
                        # for variable in class_variables:
                        #     variable_name = variable.get("class_variable_name", "")
                        #     variable_modifier = variable.get("class_variable_modifier", "")
                        #     print("Class Variable:", variable_modifier, variable_name)
                        
                        # for method in methods:
                        #     for method_name, method_info in method.items():
                        #         method_variables = method_info.get("method_variables", [])
                        #         calling_methods = method_info.get("calling", [])
                        #         print("Method:", method_name)
                                
                        #         for m_variable in method_variables:
                        #             m_variable_name = m_variable.get("method_variable_name", "")
                        #             m_variable_modifier = m_variable.get("method_variable_modifier", "")
                        #             print("Method Variable:", m_variable_modifier, m_variable_name)
                                
                        #         print("Calling Methods:", calling_methods)
                        
                        # print()