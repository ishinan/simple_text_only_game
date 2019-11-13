'''
room.py

Class Room
-----
properties:
    location
    items
    description
'''

available_items = []
items_kept_by_user = []
possible_verbs = ['take', 'drop', 'use', 'go']


class Room:
    '''
    Create a room or garden    
    parameters for instantiation
        unit_name: str
        room_info: str
        items: list
        direction_of_doors: list
    '''

    def __init__(self, unit_name, room_info, items=[], direction_of_doors=[]):
        self.unit_name = unit_name
        self.room_info = room_info
        self.unit_items = items
        self.direction_of_doors = direction_of_doors
        global available_items
        available_items += self.unit_items

    def _print_properties(self):
        '''
        print properties
        '''
        print(f"""
Location: {self.unit_name}
Doors: {self.direction_of_doors} 
Items: {self.unit_items}
Description: {self.room_info}
""")

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
        # 3. Return an answer
        print(f"You are in location: {self.unit_name} ")
        print(f"   You have choices actions: either 'verb item' or 'go to a next location'")
        print(f"   Available verbs: [take, drop, use, go]")
        print(f'   Example of answer: "take knife" or "go west"')
        print("Available items: ", ', '.join([ item for item in self.unit_items ]))
        print("Available directions: ", ', '.join([ door for door in self.direction_of_doors ]))

        self.answer = 'default'
        while len(self.answer.split()) != 2 or self.answer.split()[0] not in possible_verbs:
            self.answer = input("What is your action?['verb item' or 'go direction']? ")
        self.verb, self.x = self.answer.split()
        print("Your answer is: ", self.verb, self.x)


    def go_to_next_place(self, next_place):
        '''
        This is an action to go to a next place 
        parameter: 
            next_place name? 
        return:
            the next place's instance? 
        '''
        pass

