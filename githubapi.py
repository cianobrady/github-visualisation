from github import Github
import getpass


user = input("Enter your username: ")

password = getpass.getpass(prompt = "Enter your password: ", stream=None)
g = Github(user, password)

for repo in g.get_user().get_repos():
    print(repo.name)
