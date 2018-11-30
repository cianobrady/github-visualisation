from github import Github
import getpass
import json

user = input("Enter your username: ")

password = getpass.getpass(prompt = "Enter your password: ", stream=None)
g = Github(user, password)

username = input("Enter github username: ")
for repo in g.get_user(username).get_repos():
    print(repo.name)

repository = input("Enter repo: ")
data = []
for repo in g.get_user(username).get_repos():
    if(repository==repo.name):
        z = repo.get_stats_contributors()
        total_commits = 0
        total_additions = 0
        total_deletions = 0
        for x in z:
            for week in x.weeks:
                total_commits += week.c
                total_additions += week.a
                total_deletions += week.d
        net_lines = total_additions-total_deletions
        for x in z:
            login = x.author.login
            total = 0
            additions = 0
            deletions = 0
            for week in x.weeks:
                total += week.c
                additions += week.a
                deletions += week.d
            data.append({'user': login,'percentages': [{'value': total*100/total_commits,'type': 'commits'},{'value': (additions-deletions)*100/net_lines,'type': 'loc'}]})


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
