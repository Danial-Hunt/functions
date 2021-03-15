##
#
#
#

def collatzSolution(num):
    '''
    Description:
                 Takes any number and if even divides number by 2, if odd
                 multiplies number by 3 and adds 1. Programs runs until
                 it reaches 1.

    Input:
                 (int or float) > 1.


    Returns:     (int) Length of Collatz chain.

    '''

    chainLength = 1
    while num != 1:
        if isEvenNumber(num) == True:
            num = (num / 2)
        else:
            num = (3 * num + 1)
        chainLength += 1
    return chainLength

def isEvenNumber(num):
    '''
    Description:
                 Calculates whether a number is even or odd.

    Input:
                 (int or float) Any number

    Returns:
                 Returns the boolen value True if even and False if odd.

    '''
    if num % 2 == 0:
        return True
    else:
        return False


print(collatzSolution(99999.99999999999))
    
