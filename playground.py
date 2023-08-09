import pygit2

# Open a repository
REPO_ROOT_PATH = "E:\Work\Maucash\Repos\drive-download-20230808T022718Z-001\\"
repo_name = 'welab-application'
repo = pygit2.Repository(REPO_ROOT_PATH + repo_name)

# Iterate through commit history
for commit in repo.walk(repo.head.target):
    print("Commit ID:", commit.id)
    print("Author:", commit.author.name)
    print("Date:", commit.commit_time)
    print("Message:", commit.message)
    print("-" * 40)
