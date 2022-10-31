'''
    Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.
'''

def biggerIsGreater(string):
    '''
        Returns the next string in the lexicographical order

        :param string: <str> Input String
        :return: <str> Output String
    '''

##    list_of_characters = list(string)
    if check_if_descending(string):
        return None
    else:
        permute_list = generate_permutations(string)
        for permute_string in permute_list:
            if permute_string > string:
                return permute_string
##        return permute_list[0]


def generate_permutations(string, permute_string='', permute_list=[]):
    '''
        Generates all possible permutations of given string

        :param string: <str> String to generate permutation of
        :param permute_string: <str> Characters that are already permuted
        :param permute_list: <list(str)> List to store all permutations
        :return: <list(str)> Sorted list of strings of all possible permutations
    '''

    if len(string) == 0:
        print("PERMUTE STRING", permute_string)
        permute_list.append(permute_string)

    for i in range(len(string)):
        new_permute_string = permute_string + string[i]
        print("NEW PERMUTE STRING", new_permute_string)
        new_string = string[0:i] + string[i+1:]
        print("NEW STRING", new_string)

        generate_permutations(new_string, new_permute_string, permute_list)

    permute_list.sort()
    return permute_list

def check_if_descending(string):
    '''
        Checks if the string is in descending lexicographical order

        :param string: <str> String to check
        :return: <bool> True if string in descending lexicographical order, False otherwise
    '''

    for i in range(len(string) - 1):
        if string[i] > string[i+1]:
            continue
        else:
            return False

    return True

##a = biggerIsGreater('1234')
##b = biggerIsGreater('abcd')
c = biggerIsGreater('abcfdda')
##print(a)
##print(b)
print(c)
    
    
