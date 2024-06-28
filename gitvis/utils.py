from git import Repo
from gitvis import SUCCESS, EMAIL_ERROR

def get_global_email(repo):
    try:
        repo = Repo(repo)
        git_config = repo.config_reader()
        return git_config.get_value("user", "email"), SUCCESS
    except:
        return None, EMAIL_ERROR