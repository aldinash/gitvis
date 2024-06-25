import git
from datetime import datetime, timedelta
from typing import List


def __fill_commits(path: str, email: str, commits):
    repo = git.Repo(path)
    six_month_ago = datetime.now().date() - timedelta(days=180)
    for commit in repo.iter_commits():
        if commit.author.email != email:
            continue
        commit_date = commit.committed_date
        if commit_date < six_month_ago:
            continue
        days_ago = (now - commit_date).days
        if days_ago not in commits:
            commits[days_ago] = 1
        else:
            commit[days_ago] += 1


def process_repos(repos: List[str], email: str):
    map = {}
    for repo in repos:
        __fill_commits(repo, email, map)

    return map
