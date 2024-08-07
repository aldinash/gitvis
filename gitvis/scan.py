import os
from typing import List
from gitvis import SUCCESS, DIR_ERROR

CURRENT_DIR = os.getcwd()

IGNORE_FOLDERS = [
    "node_modules",
    "vendor",
    ".svn",
    ".hg",
    ".bzr",
    "_vendor",
    "godeps",
    "bin",
    "obj",
    "tmp",
    "build",
    ".vscode",
    "dist",
    "__pycache__",
    ".cache",
    "coverage",
    "target",
    "out",
    ".idea",
    ".gradle",
    ".terraform",
    "env",
    ".ds_store",
    ".next",
    ".nuxt",
    ".expo",
    ".circleci",
    ".github",
    ".gitlab",
    ".vagrant",
    ".serverless",
]


def scan_git_folders(dir: str) -> List[str]:
    try:
        git_folders = []

        for dirpath, dirnames, _ in os.walk(dir):
            dirnames[:] = [d for d in dirnames if d.lower() not in IGNORE_FOLDERS]
            if ".git" in dirnames:
                git_folders.append(os.path.join(dirpath, ".git"))
                dirnames.remove(".git")
        return git_folders, SUCCESS
    except:
        return [], DIR_ERROR
