import pygit2
import pprint
import datetime

# Specify repository paths
REPO_ROOT_PATH = "E:\Work\Maucash\Repos\drive-download-20230808T022718Z-001\\"
repo_names = ['welab-application']

# Define output data structure
res = dict()

# Define timeframe
today = datetime.datetime.now()
six_months_ago = today - datetime.timedelta(days=30 * 6)

for repo_name in repo_names:
    repo = pygit2.Repository(REPO_ROOT_PATH + repo_name)

    for commit in repo.walk(repo.head.target):
        # pprint.pprint(dir(commit))
        commit_time = datetime.datetime.fromtimestamp(commit.commit_time)
        
        if commit_time >= six_months_ago:
            print(f"Repository '{repo_name}' has been changed in the last 6 months.")
            
            # Get the list of changed files for this commit
            changed_files = []

            parent_commit = None
            if commit.parents:
                parent_commit = commit.parents[0]
                diff = repo.diff(parent_commit, commit)
                for patch in diff:
                    changed_files.append(patch.delta.new_file.path)

            print("Changed files:")
            for file in changed_files:
                print(file)
            print("-" * 40)
            
            break