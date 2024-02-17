def calculate_avg_temp(temps):
    sum = 0
    measures = 0
    for temp in temps:
        sum += temp
        measures += 1
    return (sum/measures)


def when_is_it_spring(temp_list):
    # Keeps track of whether we have found the first day or not
    first_found = False
    # Keeps track of how many days with a
    # positive temperature we have found

    if len(temp_list) < 7:
        return -1

    n = 0
    # Keeps track of where the first day with positive temperatures
    # was found
    index = 0
    while n < 7:
        try:
            if temp_list[index] > 0:
                n += 1
            else:
                n = 0
            index += 1
        except IndexError:
            return -1 
    return index-7
