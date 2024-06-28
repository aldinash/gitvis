import click

from . import print_m, stats, scan, utils
from gitvis import DIR_ERROR, EMAIL_ERROR, ERRORS


@click.command()
@click.option("-d", default=".", type=str, help="Target path to scan")
@click.option(
    "--email",
    default=None,
    # default=utils.get_global_email("."),
    help="Email you want to show commits for",
)
def run(d, email):
    if email == None:
        email, error = utils.get_global_email(d)
        if error == EMAIL_ERROR:
            print(ERRORS[EMAIL_ERROR])
            return
    git_folders, error = scan.scan_git_folders(d)
    if error == DIR_ERROR:
        print(ERRORS[DIR_ERROR])
        return
    commits = stats.process_repos(git_folders, email)
    print_m.print_table(commits)
