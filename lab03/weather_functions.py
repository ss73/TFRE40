def calculate_avg_tmp(temp_list):
    s, l = 0, 0
    for t in temp_list:
        s += t
        l += 1
    return round(s/l, 4)
    

def when_is_it_spring(temp_list):
    # Keeps track of whether we have found the first day or not
    first_found = False
    # Keeps track of how many days with a
    # positive temperature we have found
    n = 0
    # Keeps track of where the first day with positive temperatures
    # was found
    index = -1

    # For each day (temperature value in temp_list)
    for i, temp in enumerate(temp_list):
        if temp > 0:
            if not first_found:
                # If it is the first day where the temperature is positive:
                # note that the first day was found and save the index
                first_found = True
                index = i
                n = 1
            else:
                # Otherwise if the temperature is positive,
                # but the first day has already been found:
                # count that another day with positive temperatures
                # has been found
                n += 1
        else:
            # Otherwise if the temperature is negative:
            # The series of enumerated days is broken,
            # we must reset all variables, and mourn
            n = 0
            index = -1
            first_found = False
        if n >= 7:
            # If a total of seven days with a positive temperature are found:
            # Cancel, return the result and rejoice
            return index
    return -1

def calculate_extremes(temp_list):
    return min(temp_list), max(temp_list)        
    

