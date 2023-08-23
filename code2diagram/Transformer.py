import json
from pprint import pprint

input_filepath = "code2diagram/resource/input.json"
output_filepath = "code2diagram/out/class_diagram.txt"

with open(input_filepath) as json_file:
    data = json.load(json_file)
    for package_data in data:
        package_name = package_data.get("package_name", "")
        classes = package_data.get("classes", [])
        
        for class_info in classes:
            class_name = class_info.get("class_name", "")
            
            # Write class name to the text file for each package
            with open(output_filepath, 'a') as txt_file:
                txt_file.write(class_name + '\n')
        
        print(f"Class names from '{input_filepath}' have been saved to {output_filepath}.")
