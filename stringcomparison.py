


def stringOnstring(str1, str2):
    '''
    Description:

        Accepts two strings as arguments and returns True if either
        string occurs anywhere in the other.

    Parameters:

        str1 (str): The first string to be compared.
        str2 (str): The second string to be compared.

    Returns:

        True: If either string occurs anywhere in the other.
        False: If neither string occurs anywhere in the other.


    '''

    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False


print(stringOnstring("This is a cake", "potato"))
