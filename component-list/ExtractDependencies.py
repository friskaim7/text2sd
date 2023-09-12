def get_repo_name(package_name):
    splitted_package_name = package_name.split('.')
    return '.'.join(splitted_package_name[:3])

def get_package_name(package_line):
    splitted_package_line = package_line.split(' ')
    return splitted_package_line[-1]

if __name__ == "__main__":
    input_filename = "./component-list/out/JDepend/output - Copy.txt"
    with open(input_filename, 'r', encoding='utf-8') as file:
        line = file.readline()

        # Iterate as long as EOF has not been reached
        while line:
            # Change Package and Repo name when enter new package
            if (line.startswith("- Package: ")) and ("com.welab." in line):
                package_name = get_package_name(line)
                repo_name = get_repo_name(package_name)
                print(f'package_name: {package_name}')
                print(f'repo_name: {repo_name}')
            
            # Get next line
            line = file.readline()

            # Iterate next line as long as there is "com.welab" after "Depends Upon"
            if "Depends Upon:" in line:
                while line:
                    line = file.readline()
                    if "com.welab." in line:
                        print(f'depend upon line: {line}')
                        line = file.readline()
                        # depend_upon_list[f"{package_name}"]
                    elif "--------------------------------------------------" in line:
                        break
            if "Used By:" in line:
                while line:
                    line = file.readline()
                    if "com.welab." in line:
                        print(f'used by line: {line}')
                        line = file.readline()
                        # depend_upon_list[f"{package_name}"]
                    elif "--------------------------------------------------" in line:
                        break
