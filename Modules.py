import random
from random import randint,randrange
import sys
import helper
from utils import assists_second
from utils.assists_second import second_assist


assists_second.second_assist()

print(sys.platform)

print(random.random())

#включительно
random.randint(1, 5)

#не включительно
random.randrange(1, 5)

users = ['user1', 'user2', 'user3']
print(random.choice(users))

print(users[random.randrange(0, len(users))])

helper.assist()
print(helper.variable)

