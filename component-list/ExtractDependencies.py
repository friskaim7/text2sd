import json

INPUT_FILENAME = "./component-list/out/JDepend/output.txt"
OUTPUT_FILENAME = "./component-list/out/JDepend/repo-dependencies.json"
ROOT_PACKAGE_NAME = "com.welab."
PACKAGE_LINE_STARTER = "- Package: "
DEPENDS_UPON = "Depends Upon:"
USED_BY = "Used By:"

def get_repo_name(package_name) -> str:
    splitted_package_name = package_name.split('.')
    return '.'.join(splitted_package_name[:3]).strip()

def get_package_name(package_line):
    splitted_package_line = package_line.split(' ')
    return splitted_package_line[-1].strip()

def get_dependency_list(file):
    dep_list = set()
    # Skipping the Dependency Type
    line = file.readline()

    # Every Dependency Type ends with an empty line
    while line not in ['\n', '\r\n']:
        if ROOT_PACKAGE_NAME in line:
            dep_list.add(get_repo_name(line.strip()))
        line = file.readline()
    return dep_list

def dep_list_to_dict(du, ub):
    return {
        "du" : du,
        "ub" : ub
    }

if __name__ == "__main__":
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        # Define outputs
        repo_dependencies = {}
        package_name = None
        repo_name = None
        depend_upon_list = set()
        used_by_list = set()

        # the first line is always empty
        line = file.readline()

        # Iterate as long as EOF has not been reached
        while line:
            # Change Package and Repo name when enter new package
            # Non Welab packages are ignored
            if (line.startswith(PACKAGE_LINE_STARTER)) and (ROOT_PACKAGE_NAME in line):
                package_name = get_package_name(line)
                repo_name = get_repo_name(package_name)
                repo_dependencies[repo_name] = {
                                                "du" : set(),
                                                "ub" : set()
                                            }
            # Get the next line
            line = file.readline()

            # Iterate next line as long as there is "com.welab" after Dependency Type line
            if DEPENDS_UPON in line:
                depend_upon_list = get_dependency_list(file)
            elif USED_BY in line:
                used_by_list = get_dependency_list(file)

            if (package_name is not None) and (repo_name is not None):
                repo_dependencies[repo_name]["du"].update(depend_upon_list)
                repo_dependencies[repo_name]["ub"].update(used_by_list)

    # Convert sets to lists
    for repo_name, dep_info in repo_dependencies.items():
        dep_info["du"] = list(dep_info["du"])
        dep_info["ub"] = list(dep_info["ub"])

    # Save the dictionary to the JSON file
    with open(OUTPUT_FILENAME, 'w',  encoding='utf-8') as json_file:
        json.dump(repo_dependencies, json_file, indent=4)
