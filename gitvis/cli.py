import click

from . import stats, print, scan, utils


@click.command()
@click.option("-d", "--directory", default=".", type=str, help="Target path to scan")
@click.option(
    "--email",
    default=utils.get_global_email("."),
    help="Email you want to show commits for",
)
def run(directory, email):
    git_folders = scan.scan_git_folders(directory)
    commits = stats.process_repos(git_folders, email)
    print.print_table(commits)
