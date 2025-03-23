from abc import abstractmethod
from abc import abstractclassmethod

class Group:
    pupils = True
    school_name = 42
    director = 'Marivanna'

    def study(self):
        print('sit down please')

    def __init__(self, title, pupils_count, group_leader):
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader



    @classmethod
    @abstractmethod
    def move(self):
        pass

class PrimaryGroup(Group):
    max_age = 11
    min_age = 6
    building_section = 'left'

    def __init__(self, title, pupils_count, group_leader, class_room):
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room


    def move(self):
        print('run fast')

class HighGroup(Group):
    max_age = 18
    min_age = 14

    def move(self):
        print('run slowly')

first_a = PrimaryGroup('la', 12, 'MF',3)
eleven_a = HighGroup('lb', 18, 'GF')
first_b = PrimaryGroup('la', 15, 'AT', 4)
print(first_a.pupils_count)
print(eleven_a.group_leader)
first_a.study()
first_a.move()
eleven_a.move()
print(first_a.pupils)
print(first_a.min_age)
