# Leap Year calculator

# Every year that is divisible by 4
# except every year that is divisible by 100
# unless the year is also divisible by 400

year = int(input())

if year % 4 == 0:
    if year % 100 == 0 and not year % 400 == 0:
        is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False


# !!! Python quirk!  is_leap_year is not scoped to the if statement above.
# They are scoped to the innermost function, class, or module
# In this case, is_leap_year is considered part of the global scope so 
# it is available here with the values set in the if statement.

if is_leap_year:
    print ("Leap year")
else:
    print ("Not leap year")

