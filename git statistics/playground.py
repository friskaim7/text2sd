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
        "commit_list": {}
    }

    # Iterate through commit history
    for commit in repo.walk(repo.head.target):
        commit_time = dt.datetime.fromtimestamp(commit.commit_time)
        formatted_commit_time = commit_time.strftime('%d-%b-%Y')
        if commit_time < six_months_ago:
            print("this commit was more than 6 month ago")
            break
        
        changed_files = []
        parent_commit = None
        if commit.parents:
            parent_commit = commit.parents[0]
            diff = repo.diff(parent_commit, commit)
            for patch in diff:
                print("-" * 40)
                print(commit_time)
                changed_files.append(patch.delta.new_file.path)

        res[repo_name]["commit_list"][str(commit.short_id)] = {
            "commit_author" : commit.author.name,
            "commit_time": formatted_commit_time,
            "commit_msg": commit.message,
            "changed_files": changed_files,
        }

