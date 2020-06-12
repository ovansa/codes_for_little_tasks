#! python3
from datetime import datetime

# 1. Basic string print formatting
# library = [('i', 'am', 'not'),
#            ('afraid', 'to', 900),
#            ('a stand', 'everybody', 60)]
#
# for first, second, third in library:
#     print(f"{first:{10}} {second:{10}} {third :.>{10}}")


# 2. Basic date print formatting
today = datetime(year=2020,month=10,day=30)
print(f"{today:%a %d, %Y}")
