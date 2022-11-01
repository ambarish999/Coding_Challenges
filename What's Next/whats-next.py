'''
    Johnny is playing with a large binary number, B. The number is so large that it needs to be compressed into an array of integers,
    A, where the values in even indices (0, 2, 4, …) represent some number of consecutive 1 bits and the values in odd indices (1, 3, 5, …)
    represent some number of consecutive 0 bits in alternating substrings of B.
    
    For example, suppose we have array A = [4, 1, 3, 2, 4]. A[0] represents 1111, A[1] represents 0, A[2] represents 111, A[3] represents 00, and A[4] represents 1111.
    When we assemble the sequential alternating sequences of 1’s and 0’s, we get 11110111001111.

    We define setCount(B) to be the number of 1’s in a binary number, B. Johnny wants to find a binary number, D, that is the smallest binary number >B
    where setCount(B) = setCount(D). He then wants to compress D into an array of integers, C (in the same way that integer array A contains the compressed form of binary string B).

    Johnny isn’t sure how to solve the problem. Given array A, find integer array C and print its length on a new line. Then print the elements of array C as a single line
    of space-separated integers.
'''

def find_next_permutation(string):
    '''
        Find the smallest binary number greater than given string.

        :param string: <str> Binary number string
        :return: <str> Next binary number in sequence
    '''

    list_of_string = list(string)

    i = len(list_of_string) - 1
    while i > 0 and list_of_string[i - 1] >= list_of_string[i]:
        i = i - 1


    if i <= 0:
        return None

    j = len(list_of_string) - 1
    while list_of_string[j] <= list_of_string[i - 1]:
        j = j - 1


    list_of_string[i - 1], list_of_string[j] = list_of_string[j], list_of_string[i - 1]


    list_of_string[i:] = list_of_string[len(list_of_string)-1 : i-1 : -1]

    return ''.join(list_of_string)

def binary_number_compressor(string):
    '''
        Compresses the binary number to a list such that,
        the values in even indices represent some number of consecutive 1 bits, and
        the values in odd indices represent some number of consecutive 0 bits

        :param string: <str> Binary number string
        :return: <list> Compressed binary number representation
    '''

    list_of_string = list(string)
    compressed_list = []
    count_of_ones = 0
    count_of_zeroes = 0
    i = 0

    while i < len(list_of_string):
        if list_of_string[i] == '1':
            try:
                if list_of_string[i + 1] == '1':
                    count_of_ones = count_of_ones + 1
                else:
                    count_of_ones = count_of_ones + 1
                    compressed_list.append(count_of_ones)
                    count_of_ones = 0
            except IndexError:
                count_of_ones = count_of_ones + 1
                compressed_list.append(count_of_ones)
                count_of_ones = 0

        if list_of_string[i] == '0':
            try:
                if list_of_string[i + 1] == '0':
                    count_of_zeroes = count_of_zeroes + 1
                else:
                    count_of_zeroes = count_of_zeroes + 1
                    compressed_list.append(count_of_zeroes)
                    count_of_zeroes = 0
            except IndexError:
                count_of_zeroes = count_of_zeroes + 1
                compressed_list.append(count_of_zeroes)
                count_of_zeroes = 0

        i = i + 1

    return compressed_list

def whats_next(string):
    '''
        Find the next binary number greater than given string, compress it, and return length
        of the compressed list and compressed list.

        :param string: <str> Binary number string
        :return: <int>, <str str str...> Return the length of compressed list, and compressed list
    '''

    next_binary_number = find_next_permutation(string)
    compressed_list = binary_number_compressor(next_binary_number)

    return {"Length of list": len(compressed_list), "List": compressed_list}


a = whats_next('1001001')
print(a)
