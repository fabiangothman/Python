#Libraries: there are three types:
# Own: Create by ourself
# third-party: https://pypi.org
# Python: https://docs.python.org/3/py-modindex.html

# You can install a 3-party module by using "pip" command (package manager)
# pip install colorama

from colorama import Fore, Style, init

init(convert=True)
print(Fore.RED + "Hello world")
