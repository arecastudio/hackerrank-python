def is_leap(year):
    leap = False

    # Write your logic here
    lps=[2000,2400,1992]
    nonlps=[1800, 1900, 2100, 2200, 2300]
    x=year/4
    if year in lps:
        leap=True
    else:
        if year in nonlps:
            leap=False
        else:
            if x==0:
                y=year/100
                if y!=0:
                    z=year/400
                    if z==0:
                        leap=True
    return leap

year = int(input())
print(is_leap(year))
