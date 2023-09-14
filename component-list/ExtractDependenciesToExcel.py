# import json
import pandas as pd

INPUT_FILENAME = "./component-list/out/JDepend/output.txt"
OUTPUT_FILENAME = "./component-list/out/JDepend/repo-dependencies.xlsx"
ROOT_PACKAGE_NAME = "com.welab."
PACKAGE_LINE_STARTER = "- Package: "
DEPENDS_UPON = "Depends Upon:"
USED_BY = "Used By:"

# Repo Mapping as of 14 Sep 2023 10.35
REPO_MAPPING = {
    "S01":	"com.welab.application",
    "S02":	"com.welab.approval",
    "S03":	"com.welab.collect",
    "S04":	"com.welab.collection",
    "S05":	"com.welab.common",
    "S06":	"com.welab.core",
    "S07":	"com.welab.credit",
    "S08":	"com.welab.customer",
    "S09":	"com.welab.document",
    "S10":	"com.welab.event",
    "S11":	"com.welab.fund",
    "S12":	"com.welab.integral",
    "S13":	"com.welab.komodo",
    "S14":	"com.welab.loan",
    "S15":	"com.welab.marketing",
    "S16":	"com.welab.merchant",
    "S17":	"com.welab.message",
    "S18":	"com.welab.moon",
    "S19":	"com.welab.pay",
    "S20":	"com.welab.report",
    "S21":	"com.welab.user",
    "S22":	"com.welab.dayu",
    "S23":	"com.welab.ddd",
    "S24":	"com.welab.enums",
    "S25":	"com.welab.sea",
    "S26":	"com.welab.security",
    "S27":	"com.welab.sun",
    "S28":	"com.welab.test",
    "S29":	"com.welab.trace",
    "S30":	"com.welab.x",
    "S31":	"com.welab.xdao"
}

def get_repo_name(package_name):
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

def get_code_for_repo(repo_name):
    # list out keys and values separately
    key_list = list(REPO_MAPPING.keys())
    val_list = list(REPO_MAPPING.values())

    return key_list[val_list.index(repo_name)]

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

    # Create a list of all unique repo names
    all_repos = sorted(set(dep for deps in repo_dependencies.values() for dep in list(deps['du'])))

    # Initialize an empty DataFrame with repo names as columns and index
    dependency_matrix = pd.DataFrame(index=REPO_MAPPING.keys(), columns=REPO_MAPPING.keys())

    # Fill in the dependency matrix based on your repo_dependencies dictionary
    for repo_name, deps in repo_dependencies.items():
        repo_code = get_code_for_repo(repo_name)
        for dep_repo in deps['du']:
            dep_code = get_code_for_repo(dep_repo)
            dependency_matrix.at[dep_code, repo_code] = True

    # Fill NaN values with False (repos that are not dependent)
    dependency_matrix = dependency_matrix.fillna(False)

    # Export the DataFrame to an Excel file
    dependency_matrix.to_excel(OUTPUT_FILENAME, engine='openpyxl')

    print(f'Dependency matrix saved to {OUTPUT_FILENAME}')
