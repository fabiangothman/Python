#Libraries: there are three types:
# Own: Create by ourself
# third-party: https://pypi.org
# Python: https://docs.python.org/3/py-modindex.html

import time
from datetime import date, timedelta

print(type(date.today()))
print(date.today())

print(type(timedelta(minutes=70)))
print(timedelta(minutes=70))

print(time.localtime())
