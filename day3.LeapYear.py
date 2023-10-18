# Leap Year calculator

# Every year that is divisible by 4
# except every year that is divisible by 100
# unless the year is also divisible by 400

year = int(input())

is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0 and not year % 400 == 0:
        is_leap_year = False
    else:
        is_leap_year = True

if is_leap_year:
    print ("Leap year")
else:
    print ("Not leap year")

