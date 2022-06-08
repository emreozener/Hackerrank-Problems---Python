def is_leap(year):
    #tells if the year is leap year or not
    if year % 4 != 0:
         return False
    elif year % 4 == 0 and year % 100 != 0:
         return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
