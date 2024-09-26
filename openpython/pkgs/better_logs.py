from colorama import Fore
import colorama
import datetime

def err(msg: str, errCode: int, color = Fore.RED):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (ERR - {code})  >>>  {msg}".format(code=errCode, msg=msg, color=color, timestamp=time))

def info(msg: str, color = Fore.CYAN):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (INFO)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))

def success(msg: str, color = Fore.GREEN):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (SUCCESS)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))

def crit(msg: str, errCode: int, color = Fore.MAGENTA):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (CRIT ERR - {code})  >>>  {msg}".format(code=errCode, msg=msg, color=color, timestamp=time))

def sys_msg(msg: str, color = Fore.LIGHTBLUE_EX):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (SYSTEM MSG)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))

def shutdown(msg: str, errCode: int, color = Fore.MAGENTA):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (SYSTEM ERR - {code})  >>>  {msg}\n--> WARNING: Process exiting due to a system error.".format(code=errCode, msg=msg, color=color, timestamp=time))
    return exit(404)

def warn(msg: str, color = Fore.YELLOW):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (WARNING)  >>>  {msg}".format(msg=msg, color=color, timestamp=time))

def log(msg: str, color = Fore.WHITE):
    time = datetime.datetime.now()
    print("{color}[-> {timestamp} <-] (LOG) >>>  {msg}".format(msg=msg, color=color, timestamp=time))