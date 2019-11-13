'''
start.py

Game start and controlled

Class Room
-----
properties:
    location
    items
    description


    winning_condition
    changine element
'''
# 1. Import room module
# 2. Create multiple rooms( Enterance, Living, Kitchen, Bathroom, etc)
#    - Each room unit has one to four doors to north/sourth/west/east
#    - Each room unit has some items, hummer, knife, key, candle 
#    - Person can do action take or drop
#    - Only if the person has a proper key, secret door can be opend for a treasure
# 3. Connect them 

from room import Room

# This disctionary decides how many rooms and connections to rooms
play_space = {
}


def main():
    '''
    main function
    '''
    kitchen = Room("kitchen", "kitchen is spacious", ['knife'], ['east'])
    living = Room("living", "living has couch and tv",['painting'], ['west'])

    kitchen._print_properties()
    living._print_properties()
    living.interact_with_user() 
    
    



if __name__ == '__main__':
    main()