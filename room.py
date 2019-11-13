'''
room.py

Class
-----

Room
'''
class Room:

    def __init__(self, unit_name, direction_of_doors=[]):
        self.unit_name = unit_name
        self.direction_of_doors = direction_of_doors

    def add_next_room(self, next_room, door_dirction):
        '''
        next_room is an instance
        '''
        self.next_room = next_room

    def interact_with_user(self):
        '''
        ask user to select direction and items 
        return user's answer
        '''
        # 1. print room name, list of doors(direction), list of item
        # 2. Ask what wnat to do "go which direction" or "take an item" or drop an item"
        # 3. Return ansers 
        pass

    def go_to_next_place(self, next_place):
        '''
        This is an action to go to a next place 
        parameter: 
            next_place name? 
        return:
            the next place's instance? 
        '''
