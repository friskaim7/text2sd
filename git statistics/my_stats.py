from collections import defaultdict
import pygit2
import pprint
import datetime as dt
import os
import json

# Open a repository
REPO_ROOT_PATH = "E:\Work\Maucash\Repos\drive-download-20230808T022718Z-001\\"
repo_names = [name for name in os.listdir(REPO_ROOT_PATH) if os.path.isdir(os.path.join(REPO_ROOT_PATH, name))]

# Define timeframe
today = dt.datetime.now()
six_months_ago = today - dt.timedelta(days=30 * 6)

# Define output variable
res = dict()

for repo_name in repo_names:
    repo = pygit2.Repository(REPO_ROOT_PATH + repo_name)

    # Initialize the nested dictionaries for the repository
    res[repo_name] = {
        "commit_list": {},
        "commit_counts": {}
    }
    commit_counts = defaultdict(int)

    # Iterate through commit history
    for commit in repo.walk(repo.head.target):
        commit_time = dt.datetime.fromtimestamp(commit.commit_time)
        formatted_commit_time = commit_time.strftime('%d-%b-%Y')
        if commit_time < six_months_ago:
            print("this commit was more than 6 month ago")
            break
        
        commit_month = commit_time.strftime('%Y-%m')
        commit_counts[commit_month] += 1

        changed_files = []
        parent_commit = None
        if commit.parents:
            parent_commit = commit.parents[0]
            diff = repo.diff(parent_commit, commit)
            for patch in diff:
                changed_files.append(patch.delta.new_file.path)

        res[repo_name]["commit_list"][str(commit.short_id)] = {
            "commit_author" : commit.author.name,
            "commit_time": formatted_commit_time,
            "commit_msg": commit.message,
            "changed_files": changed_files,
        }
    res[repo_name]["commit_counts"] = commit_counts

# Specify the path of the JSON file
json_file_path = 'output.json'        

# Save the dictionary to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(res, json_file, indent=4)  # indent for pretty formatting
