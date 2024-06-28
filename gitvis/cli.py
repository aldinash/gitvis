import click
from datetime import datetime

from . import print_m, stats, scan, utils
from gitvis import DIR_ERROR, EMAIL_ERROR, DATE_ERROR, ERRORS


@click.command()
@click.option("-d", default=".", type=str, help="Target path to scan")
@click.option(
    "--email",
    default=None,
    type=str,
    help="Email you want to show commits for",
)
@click.option(
    "--since",
    default=None,
    type=str,
    help="Date you want to see commits from (format: MM-DD-YYYY)",
)
def run(d, email, since):
    if email == None:
        email, error = utils.get_global_email(".")
        if error == EMAIL_ERROR:
            click.echo(ERRORS[EMAIL_ERROR])
            return
    if since == None:
        since = since = datetime.now().date()
    else:
        try:
            since = datetime.strptime(since, "%m-%d-%Y").date()
        except:
            click.echo(ERRORS[DATE_ERROR])
            return
    git_folders, error = scan.scan_git_folders(d)
    if error == DIR_ERROR:
        click.echo(ERRORS[DIR_ERROR])
        return
    commits = stats.process_repos(git_folders, email)
    click.echo(f"Email: {email}")
    click.echo(f"Directory {d}")
    print_m.print_table(commits, since)
