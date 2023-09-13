ROOT_PACKAGE_NAME = "com.welab."

def get_repo_name(package_name) -> str:
    splitted_package_name = package_name.split('.')
    return '.'.join(splitted_package_name[:3]).strip()

def get_package_name(package_line):
    splitted_package_line = package_line.split(' ')
    return splitted_package_line[-1].strip()

def get_dependency_list(file, dep_type="depend upon", stoper="Used By:"):
    print(dep_type)
    line = file.readline()
    while stoper not in line:
        if ROOT_PACKAGE_NAME in line:
            print(f'{dep_type} {line}')  # Print each dependency
        line = file.readline()

if __name__ == "__main__":
    input_filename = "./component-list/out/JDepend/output - Copy.txt"
    with open(input_filename, 'r', encoding='utf-8') as file:
        line = file.readline()

        # Iterate as long as EOF has not been reached
        while line:
            # Change Package and Repo name when enter new package
            # Non Welab packages are ignored
            if (line.startswith("- Package: ")) and (ROOT_PACKAGE_NAME in line):
                package_name = get_package_name(line)
                repo_name = get_repo_name(package_name)
                print()
                print(f"package_name: {package_name}")
                print(f"repo_name: {repo_name}")
            
            # Get next line
            line = file.readline()

            # Iterate next line as long as there is "com.welab" after "Depends Upon"
            if "Depends Upon:" in line:
                get_dependency_list(file, "Depends Upon:", "Used By:")
            # if "Used By:" in line:
            elif "Used By:" in line:
                get_dependency_list(file, "Used By:", "--------------------------------------------------")
