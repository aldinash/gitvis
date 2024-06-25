from git import Repo

def get_global_email(repo: str) -> str:
    repo = Repo(repo)
    git_config = repo.config_reader()
    return git_config.get_value("user", "email")