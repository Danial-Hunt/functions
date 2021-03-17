def is_leap(year):
    leap = False
    """
    Description: Calculates if year is leap year.
    Input: (int) Year
    Output: (boolean) True if leap year, False if not leap year or invalid input
    """
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                leap = True

            else:
                leap = False
        else:
            leap = False
    else:
        leap = False
    
    return leap

year = int(input())
