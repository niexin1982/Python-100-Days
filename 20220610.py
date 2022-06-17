from operator import truediv
import os
from pickle import FALSE, TRUE
str = 'py'
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.split(x)[1].find(str) > 0])

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)

print(s)

import re

def is_valid_email(addr):
    if re.match(r'[\w.]+@\w+.com$',addr):
        return True
    else:
        return False

print (is_valid_email('someone@gmail.com'))