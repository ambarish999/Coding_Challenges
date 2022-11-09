'''
    An English text needs to be encrypted using the following encryption scheme.

    First, the spaces are removed from the text. Let "L" be the length of this text.

    Then, characters are written into a grid, whose rows and columns have the following constraints:

    floor(sqrt(L)) <= row <= column <= ceil(sqrt(L))
'''

import math

def encrypt(string):
    '''
        Encrypt/Encode a string

        :param string: <str> String to be encrypted

        :return: <str> Return the encrypted/encoded string
    '''

    # Remove whitespace
    new_string = string.replace(" ", "")

    list_new_string = list(new_string)

    new_string_length = len(new_string)
    print(new_string_length)

    # Square root of length
    length_sqrt = math.sqrt(new_string_length)
    print(length_sqrt)

    row = None
    column= None
    if math.floor(length_sqrt) == math.ceil(length_sqrt):
        row=column=math.floor(length_sqrt)
    else:
        row = math.floor(length_sqrt)
        column = math.ceil(length_sqrt)


    character_grid = []

    for i in range(0, row):
        temp_list = []
        for j in range(0, column):
            try:
                temp_char = list_new_string.pop(0)
                temp_list.append(temp_char)
            except IndexError:
                continue
        character_grid.append(temp_list)

    if len(character_grid[-1]) == 0:
        character_grid.pop()

    encrypted_string = ""

    while isListEmpty(character_grid) == False:
        for i in range(0, len(character_grid)):
            try:
                temp_char = character_grid[i].pop(0)
            except IndexError:
                continue
            encrypted_string = encrypted_string + temp_char
        encrypted_string = encrypted_string + " "

    return encrypted_string


def isListEmpty(inList):
    '''
        Checks if list is empty or not

        :param inList: <list> Input List

        :return: <bool> True if inList is empty, False otherwise
    '''
    
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList))
    return False

    

a = encrypt('Return the encrypted/encoded stringssss')
b = encrypt('if man was meant to stay on the ground god would have given us roots')
print(a)
print(b)
