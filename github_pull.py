import os
from datetime import date

path = os.path.realpath(__file__).split('github')[0]

os.chdir(path)

print(os.path)
output = os.popen('git pull origin main').read()
print(output)

