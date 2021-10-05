import os
from datetime import date

path = os.path.realpath(__file__).split('github')[0]
os.chdir(path)

user_name = os.popen('git config --list ').read().split('user.name=')[1].split('\n')[0]

print(os.path)
output = os.popen('git init')
print(output)
output = os.popen('git add .').read()
print(output)
output = os.popen('git commit -m "{}  {}"'.format(user_name, date.today())).read()
print(output)
output = os.popen('git push origin main').read()
print(output)