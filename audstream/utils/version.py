

import aiohttp
import asyncio
import threading
from colorama import Fore, Style
from .time import time

class version:
    @classmethod
    async def _get_version(cls, current_version: str) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/Ceeq9717/audstream/master/audstream/__init__.py") as resp:
                text = await resp.text()
                github_version = text.split("__version__ = ")[1].split("\n")[0].replace('"', "")

        current_version = current_version.replace(".", "")
        github_version = github_version.replace(".", "")

        if int(current_version) >= int(github_version):
            return print(time(f"{Fore.GREEN} {Style.BRIGHT} [AUDSTREAMER] You are using the latest version of audstream!{Fore.RESET} {Style.RESET_ALL}"))
        else:
            return print(time(f"{Fore.RED} {Style.BRIGHT} [WARNING] You are using an outdated version of audstream!{Fore.RESET} {Style.RESET_ALL}"))

    @classmethod
    def __check_version(cls, current_version: str) -> None:
        asyncio.run(cls._get_version(current_version))

    @classmethod
    def _check(cls, current_version: str) -> None:
        thread = threading.Thread(target=cls.__check_version, args=(current_version,))

        thread.start()