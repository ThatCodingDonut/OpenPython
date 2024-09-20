from openpython.pkgs import better_logs, licenses
from colorama import Fore

# Example Logging System
better_logs.err("This is an error.", 404)
better_logs.info("This is an info log.")
better_logs.success("Successfully passed!")
better_logs.crit("System Failure.", 500)
better_logs.sys_msg("This is a message from the system")
better_logs.warn("This is a warning!")
better_logs.log("This is a simple console log.")
"""better_logs.shutdown("This is a shutdown error.", 404) -> Enabling this will disable all lines below."""


# Example Licensing System
key = licenses.generate_key()
keyfile = licenses.storekey("./licenses", key)
filename = keyfile['filename']
"""
    The commands below will not work, since the license key file was just created in the same script.
    The key file must be created, THEN IN ANOTHER SCRIPT (Or using async/await) it can be checked.
"""
# print(licenses.retrievekey("{}".format(filename)))
# print(licenses.validate_key(licenses.retrievekey("{}".format(filename)), "**-*****-*****-*****"))

