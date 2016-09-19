year=raw_input();
def leap(year):
    if int(year)%4==0:
        if int(year)%100==0:
            if int(year)%400==0:
                return "Leap year";
            else:
                return "Not a leap year";
        else:
            return "Leap year";
    else:
        return "Not a leap year";
print leap(year)
