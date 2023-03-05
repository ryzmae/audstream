import datetime

from colorama import Fore, Style

def time(text) -> str:
    cTime = datetime.datetime.now()

    return f"{Fore.MAGENTA} {Style.BRIGHT} [{cTime.year}-{cTime.day}-{cTime.month} {cTime.hour}:{cTime.minute}:{cTime.second}]{Fore.RESET} {Style.RESET_ALL} {text}"