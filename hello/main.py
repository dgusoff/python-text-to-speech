import time
from datetime import date

greetings = []
greetings.append(dict(name = 'Derek', robot = 'wire01', stamp = time.time()))
greetings.append(dict(name = 'Kyle', robot = 'wire02', stamp = time.time()))

# looking to do...
# greetings.where(x => x.name == "Derek" && x.robot == "wire01")

found = False
for greeting in greetings:
    if greeting['name'] == "Derek" and greeting['robot'] == 'wire01' and greeting['stamp'] >  time.time() - 7200:
        found = True
        break

print(found)