import javalang
import json

def parse_java_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
        try:
            tree = javalang.parse.parse(code)
            return tree
        except javalang.parser.JavaSyntaxError as e:
            print("Syntax error:", e)
            return None

def object_to_dict(obj):
    if isinstance(obj, dict):
        # If the object is already a dictionary, return it as is.
        return obj
    elif isinstance(obj, list):
        # If the object is a list, recursively convert each element.
        return [object_to_dict(item) for item in obj]
    elif hasattr(obj, '__dict__'):
        # If the object has a __dict__ attribute, convert it to a dictionary.
        return {key: object_to_dict(value) for key, value in obj.__dict__.items()}
    else:
        # For other data types (e.g., strings, numbers), return them directly.
        return obj

def save_to_json(dictionary, filename='data.json'):
    # Convert sets to lists before serializing
    def convert_to_serializable(obj):
        if isinstance(obj, set):
            return list(obj)
        return obj

    json_string = json.dumps(dictionary, indent=4, default=convert_to_serializable)

    # json_string = json.dumps(dictionary)
    with open(filename, 'w') as json_file:
        json_file.write(json_string)

if __name__ == "__main__":
    # java_file_path = "E:\Work\Maucash\Repos\\21-repos\welab-credit-engine\welab-credit-engine-web\src\main\java\com\welab\credit\engine\Application.java"
    java_file_path = "E:\Work\Maucash\Repos\\21-repos\welab-loan-finance\welab-loan-finance-core\src\main\java\com\welab\loan\\finance\service\\business\FifUvfBusiService.java"
    parsed_tree = parse_java_file(java_file_path)
    if parsed_tree:
        print("Java file parsed successfully!")
        save_to_json(object_to_dict(parsed_tree), "data-checkLoan.json")
