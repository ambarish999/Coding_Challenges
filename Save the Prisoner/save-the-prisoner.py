'''
    For example, there are 4 prisoners and 6 pieces of candy.
    The prisoners arrange themselves in seats numbered 1 to 4.
    Let’s suppose two is drawn from the hat. Prisoners receive candy at positions 2, 3, 4, 1, 2, 3.
    The prisoner to be warned sits in chair number 3.
'''

def save_the_prisoners(n, m, s):
    '''
        :param n: <int> number of prisoners
        :param m: <int> number of sweets
        :param s: <int> chair number to begin passing out sweets from

        :return: <int> prisoner at <seat number> to be warned
    '''

    if s > n or s < 1:
        s = 1
    list_of_prisoners = [i for i in range(n)]
    list_of_sweets = [i for i in range(m)]
    seat_num_of_prisoner_to_be_warned = None
    #num_of_places_from_start = s - 1
    num_of_seats_from_start = (n + 1) - s # Inclusive of the starting position

    if n > m:
        if s == 1:
            seat_num_of_prisoner_to_be_warned = m
            return seat_num_of_prisoner_to_be_warned
        else:
            if num_of_seats_from_start > m:
                seat_num_of_prisoner_to_be_warned = (m + s) - 1
                return seat_num_of_prisoner_to_be_warned
            elif num_of_seats_from_start == m:
                seat_num_of_prisoner_to_be_warned = n
                return seat_num_of_prisoner_to_be_warned
            elif num_of_seats_from_start < m:
                seat_num_of_prisoner_to_be_warned = m - num_of_seats_from_start
                return seat_num_of_prisoner_to_be_warned
    elif n == m:
        if s == 1:
            seat_num_of_prisoner_to_be_warned = n
            return seat_num_of_prisoner_to_be_warned
        else:
            seat_num_of_prisoner_to_be_warned = n - num_of_seats_from_start
            return seat_num_of_prisoner_to_be_warned
    else:
        if s == 1:
            seat_num_of_prisoner_to_be_warned = m % n
            return seat_num_of_prisoner_to_be_warned
        else:
            seat_num_of_prisoner_to_be_warned = m % num_of_seats_from_start
            if seat_num_of_prisoner_to_be_warned == 0:
                seat_num_of_prisoner_to_be_warned = s
            return seat_num_of_prisoner_to_be_warned


print(save_the_prisoners(4, 6, 2))
print(save_the_prisoners(6, 6, 4))
print(save_the_prisoners(10, 4, 4))
