from colorama import Fore
import colorama
import datetime


class log:
    def __init__(self):
        pass

    def err(msg: str, errCode: int, color = Fore.RED):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (ERR - {code})  >>>  {msg}".format(code=errCode, msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def info(msg: str, color = Fore.CYAN):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (INFO)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def success(msg: str, color = Fore.GREEN):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (SUCCESS)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def crit(msg: str, errCode: int, color = Fore.MAGENTA):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (CRIT ERR - {code})  >>>  {msg}".format(code=errCode, msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def sys_msg(msg: str, color = Fore.LIGHTBLUE_EX):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (SYSTEM MSG)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def shutdown(msg: str, errCode: int, color = Fore.MAGENTA):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (SYSTEM ERR - {code})  >>>  {msg}\n--> WARNING: Process exiting due to a system error.".format(code=errCode, msg=msg, color=color, timestamp=time))
        print(Fore.RESET)
        return exit(404)

    def warn(msg: str, color = Fore.YELLOW):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (WARNING)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))
        print(Fore.RESET)

    def log(msg: str, color = Fore.WHITE):
        time = datetime.datetime.now()
        print("{color}[-> {timestamp} <-] (LOG) >>>  {msg}".format(msg=msg, color=color, timestamp=time))
        print(Fore.RESET)