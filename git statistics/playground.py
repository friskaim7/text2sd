import pygit2
import datetime

# Open a repository
REPO_ROOT_PATH = "E:\Work\Maucash\Repos\drive-download-20230808T022718Z-001\\"
repo_names = ['welab-application']

# Define timeframe
today = datetime.datetime.now()
six_months_ago = today - datetime.timedelta(days=30 * 6)

for repo_name in repo_names:
    repo = pygit2.Repository(REPO_ROOT_PATH + repo_name)

    # Iterate through commit history
    for commit in repo.walk(repo.head.target):
        commit_time = datetime.datetime.fromtimestamp(commit.commit_time)
        formatted_time = commit_time.strftime('%d-%b-%Y')
        if commit_time < six_months_ago:
            print("this commit was more than 6 month ago")
            break
        print("Commit ID:", commit.id)
        print("Author:", commit.author.name)
        print("Date:", formatted_time)
        print("Message:", commit.message)
        print("-" * 40)
