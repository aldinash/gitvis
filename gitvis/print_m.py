import datetime
import colorama
from colorama import Fore, Back, Style


colorama.init(autoreset=True)

six_empty_spaces = " " * 6


def __build_header(start, end):
    s = []
    current = start
    while current <= end:
        s.append(f"{current.strftime('%b'): <16}")
        current = __add_months(current, 1)
    return "".join(s)


def __get_day(i):
    days = {1: "Mon", 3: "Wed", 5: "Fri"}
    return days.get(i, "   ")


def print_table(commits):
    print()
    today = datetime.date.today()
    six_months_ago = __add_months(today, -6)

    start_date = six_months_ago - datetime.timedelta(days=six_months_ago.weekday() + 1)
    end_date = today + datetime.timedelta(days=(5 - today.weekday()))

    print(f"{six_empty_spaces}     {__build_header(start_date, end_date)}")
    max_val = max(commits.values(), default=0)

    s1 = start_date

    for i in range(7):
        line = f"{__get_day(i): <5}"
        sn2 = s1
        while sn2 <= end_date:
            d = __days_ago(sn2)
            line += __print_cell(commits.get(d, 0), max_val)
            sn2 += datetime.timedelta(days=7)
        s1 += datetime.timedelta(days=1)
        print(line)
    print()


def __print_cell(val, max_value):
    if val == 0:
        return f"{Fore.RESET}{Back.RESET}  - "
    if val <= max_value / 8:
        return f"{Fore.RESET}{Back.LIGHTCYAN_EX} {val:2d} "
    elif val <= max_value / 4:
        return f"{Fore.RESET}{Back.CYAN} {val:2d} "
    elif val < max_value / 2:
        return f"{Fore.RESET}{Back.BLUE} {val:2d} "
    else:
        return f"{Fore.RESET}{Back.LIGHTBLUE_EX} {val:2d} "


def __add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12)
    month = month % 12 + 1
    day = min(
        sourcedate.day,
        [
            31,
            29 if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0 else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,
        ][month - 1],
    )
    return datetime.date(year, month, day)


def __days_ago(d):
    today = datetime.date.today()
    return (today - d).days
