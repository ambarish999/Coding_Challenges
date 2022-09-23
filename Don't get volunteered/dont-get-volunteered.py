'''
    write a function called solution(src, dest) which takes in two parameters: the source square, on which you start,
    and the destination square, which is where you need to land to solve the puzzle.
    The function should return an integer representing the smallest number of moves it will take for you to travel
    from the source square to the destination square using a chess knight’s moves (that is, two squares in any direction
    immediately followed by one square perpendicular to that direction, or vice versa, in an “L” shape).
    Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered as below.

    0  1  2  3  4  5  6  7
    -----------------------
    8  9  10 11 12 13 14 15
    -----------------------
    16 17 18 19 20 21 22 23
    -----------------------
    24 25 26 27 28 29 30 31
    -----------------------
    32 33 34 35 36 37 38 39
    -----------------------
    40 41 42 43 44 45 46 47
    -----------------------
    48 49 50 51 52 53 54 55
    -----------------------
    56 57 58 59 60 61 62 63
'''

import random

def solution(src, dest):
    '''
        :param src: <int> The source
        :param dest: <int> The destination
        :return: <int> Minimum number of moves to go from source to destination
    '''

    if src < 0 or dest > 63:
        return "Invalid source or destination. Source and destination must be between 0 and 63 both included."

    if src == dest:
        minimum_number_of_moves = 0
        return minimum_number_of_moves

    is_left_bound, is_right_bound, is_top_bound, is_bottom_bound = get_boundaries_for_chessboard(src)

    # Get the list of tuples containing
    # all the possible moves from source to destination

    all_possible_moves = get_possible_moves(src, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)
    
    #all_moves_downward = move_downward(src, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)
    #all_moves_upward = move_upward(src, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)

    #print(all_moves_downward, all_moves_upward)

    #all_moves = all_moves_downward + all_moves_upward

    #all_possible_moves = [(i, j) for (i, j) in all_moves if j != None]

    #print(all_possible_moves)

    moves_taken = []
    tile_seen = []
    for (i, j) in all_possible_moves:
        if j == dest:
            moves_taken.append((i, j))
            tile_seen.append(j)
            #return moves_taken
            break
        else:
            moves_taken.append((i, j))
            if j in tile_seen:
                continue
            else:
                tile_seen.append(j)
                is_left_bound, is_right_bound, is_top_bound, is_bottom_bound = get_boundaries_for_chessboard(j)
                new_possible_moves = get_possible_moves(j, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)
                all_possible_moves.extend(new_possible_moves)

    # Last move to destination
    #path.append(moves_taken[-1])
    #print("PATH ", moves_taken)
    map_dict = map_source_to_destination_from_moves(moves_taken)
    minimum_number_of_moves = get_shortest_path(map_dict, src, dest)

    return minimum_number_of_moves
    


def move_downward(src, is_left_bound=False, is_right_bound=False, is_top_bound=False, is_bottom_bound=False):
    '''
        Moves the knight downward
        :param src: <int> The source
        :param is_left_bound: <bool> If src is on leftmost vertical boundary of the chessboard
        :param is_right_bound: <bool> If src is on rightmost vertical boundary of the chessboard
        :param is_top_bound: <bool> If src is on topmost horizontal boundary of the chessboard
        ::param is_bottom_bound: <bool> If src is on bottommost horizontal boundary of the chessboard
        :return: <list(tuple)> Returns the list of tuples of all the moves downward
    '''

    # right-right-down(+10)
    if is_right_bound or is_bottom_bound:
        temp_dest = None
    else:
        if src + 10 > 63 or src > 63:
            temp_dest = None
        else:
            temp_dest = src + 10
    
    # right-down-down(+17)
    if is_right_bound or is_bottom_bound:
        temp_dest2 = None
    else:
        if src + 17 > 63 or src > 63:
            temp_dest2 = None
        else:
            temp_dest2 = src + 17

    # left-left-down(+6)
    if is_left_bound or is_bottom_bound:
        temp_dest3 = None
    else:
        if src + 6 > 63 or src > 63:
            temp_dest3 = None
        else:
            temp_dest3 = src + 6

    # left-down-down(+15)
    if is_left_bound or is_bottom_bound:
        temp_dest4 = None
    else:
        if src + 15 > 63 or src > 63:
            temp_dest4 = None
        else:
            temp_dest4 = src + 15

    possible_moves_downward = [(src, temp_dest), (src, temp_dest2), (src, temp_dest3), (src, temp_dest4)]

    return possible_moves_downward

def move_upward(src, is_left_bound=False, is_right_bound=False, is_top_bound=False, is_bottom_bound=False):
    '''
        Moves the knight upward
        :param src: <int> The source
        :param is_left_bound: <bool> If src is on leftmost vertical boundary of the chessboard
        :param is_right_bound: <bool> If src is on rightmost vertical boundary of the chessboard
        :param is_top_bound: <bool> If src is on topmost horizontal boundary of the chessboard
        ::param is_bottom_bound: <bool> If src is on bottommost horizontal boundary of the chessboard
        :return: <list(tuple)> Returns the list of tuples of all the moves downward
    '''

    # right-right-up(-6)
    if is_right_bound or is_top_bound:
        temp_dest = None
    else:
        if src - 6 < 0 or src < 0:
            temp_dest = None
        else:
            temp_dest = src - 6

    # right-up-up(-15)
    if is_right_bound or is_top_bound:
        temp_dest2 = None
    else:
        if src - 15 < 0 or src < 0:
            temp_dest2 = None
        else:
            temp_dest2 = src - 15

    # left-left-up(-10)
    if is_left_bound or is_top_bound:
        temp_dest3 = None
    else:
        if src - 10 < 0 or src < 0:
            temp_dest3 = None
        else:
            temp_dest3 = src - 10

    # left-up-up(-17)
    if is_left_bound or is_top_bound:
        temp_dest4 = None
    else:
        if src - 17 < 0 or src < 0:
            temp_dest4 = None
        else:
            temp_dest4 = src - 17

    possible_moves_upward = [(src, temp_dest), (src, temp_dest2), (src, temp_dest3), (src, temp_dest4)]

    return possible_moves_upward

def get_possible_moves(src, is_left_bound=False, is_right_bound=False, is_top_bound=False, is_bottom_bound=False):
    '''
        Gets all the possible moves from the source
        :param src: <int> The source
        :param is_left_bound: <bool> If src is on leftmost vertical boundary of the chessboard
        :param is_right_bound: <bool> If src is on rightmost vertical boundary of the chessboard
        :param is_top_bound: <bool> If src is on topmost horizontal boundary of the chessboard
        ::param is_bottom_bound: <bool> If src is on bottommost horizontal boundary of the chessboard
        :return: <list(tuple)> Returns the list of tuples of all the moves possible
    '''

    all_moves_downward = move_downward(src, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)
    all_moves_upward = move_upward(src, is_left_bound=is_left_bound, is_right_bound=is_right_bound, is_top_bound=is_top_bound, is_bottom_bound=is_bottom_bound)

    #print(all_moves_downward, all_moves_upward)

    all_moves = all_moves_downward + all_moves_upward

    all_possible_moves = [(i, j) for (i, j) in all_moves if j != None]

    #print(all_possible_moves)

    return all_possible_moves

def check_if_new_source_closer_to_destination(new_src, dest, all_possible_moves):
    '''
        Checks if the new source is the closest to the destination out of all the possible sources in all_possible_moves
        :param new_src: <int> The new source
        :param dest: <int> The destination
        :param all_possible_moves: <list> List of all the possible moves
        :return: <bool> True if new_src is closest, False otherwise
    '''

    num_of_places = 0
    list_num_of_places = []

    for (i, j) in all_possible_moves:
        if j < dest:
            temp = dest - j
            list_num_of_places.append(temp)
        else:
            temp = j - dest
            list_num_of_places.append(temp)
    
    if new_src > dest:
        num_of_places = new_src - dest
    else:
        num_of_places = dest - new_src

    print("list of num places ", list_num_of_places)
    print("num places ", num_of_places)
    print("MINIMUM ", min(list_num_of_places))

    if num_of_places == min(list_num_of_places):
        #print("IN IF")
        return True
    else:
        return False

def get_boundaries_for_chessboard(src):
    '''
        Gets the boundaries of the chessboard beyond which moves cannot exist
        :param src: <int> The source
        :return: 4<bool> The boolean flags for this src
    '''

    # Boundaries of the chessboard
    left_bound = [i for i in range(0, 63) if i%8 == 0]
    right_bound = [i for i in range(7, 71, 8)]
    top_bound = [i for i in range(0, 8)]
    bottom_bound = [i for i in range(56, 64)]

    # Initializing the flags to check for boundaries
    is_left_bound=False
    is_right_bound=False
    is_top_bound=False
    is_bottom_bound=False

    if src in left_bound:
        is_left_bound = True
    else:
        is_left_bound = False
    if src in right_bound:
        is_right_bound = True
    else:
        is_right_bound = False
    if src in top_bound:
        is_top_bound = True
    else:
        is_top_bound = False
    if src in bottom_bound:
        is_bottom_bound = True
    else:
        is_bottom_bound = False

    return is_left_bound, is_right_bound, is_top_bound, is_bottom_bound

def get_shortest_path(map_dict, src, dest):
    '''
        Get the minimum number of moves to take to reach the destination
        :param map_dict: <dict> Mapping between source to destination for all tiles in 'moves_taken' above
        :param src: <int> The source
        :param dest: <int> The destination
        :return: <int> Minimum number of moves
    '''

    path = []
    item = dest
    while src not in path:
        for key in map_dict.keys():
            if item in map_dict[key]:
                path.append(key)
                item = key
                break
    #print("PATH", path)
    return len(path)

def map_source_to_destination_from_moves(moves_taken):
    '''
        Maps each source tile to destination tile 
        :param moves_taken: <list(tuple)> Moves taken to reach given destination
        :return: <dict> dictionary with key: source, value: list(destinations)
    '''

    map_dict = {}

    for i in range(len(moves_taken)):
        #print("i", moves_taken[i])
        current_source = moves_taken[i][0]
        temp_list = []
        for j in range(len(moves_taken)):
            if moves_taken[j][0] == current_source:
                #print("j", moves_taken[j])
                temp_list.append(moves_taken[j][1])
        map_dict[current_source] = temp_list

    return map_dict
        
    
        





print(solution(0, 1)) # 3
print(solution(19, 36)) # 1
print(solution(29, 0)) # 4
