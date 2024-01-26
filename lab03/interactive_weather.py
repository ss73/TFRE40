from pathlib import Path
import os
import file_reader
import weather_functions as wf

# The file name is actually 'temperature_data.csv' but added some extra path-stuff here
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperature_data.csv'

def user_interface():
    os.system('clear')
    print('What do you want to do? \
          \n   Press 1 for average temperature\
          \n   Press 2 for the arrival of spring\
          \n   Press 3 for the "real" arrival of spring (after Feb 15)\
          \n   Press 4 for extremes\
          \n   Press 5 to exit')
    selection = int(input())
    if selection == 1:
        print('Which month do you want to calculate the average temperature for?\
              \nEnter month number (0 = The whole year)')
        month = int(input())
        temp_list = file_reader.read_from_file(file_path, month)
        displaytime = 'months Jan-Dec' if month == 0 else 'month ' + str(month)
        print('>> Average temperature for', displaytime, 'is', wf.calculate_avg_tmp(temp_list))
        input('press enter...')

    elif selection == 2:
        temp_list = file_reader.read_from_file(file_path)
        print('>> Spring arrives on day index:', wf.when_is_it_spring(temp_list))
        input('press enter...')

    elif selection == 3:
        date_temp_list = file_reader.read_from_file_with_dates(file_path,0,46)
        date_list, temp_list = zip(*date_temp_list)
        date = date_list[wf.when_is_it_spring(temp_list)]
        print('>> Spring arrives on day:', date)
        input('press enter...')

    elif selection == 4:
        print('Which month do you want to get the extreme temperatures for?\
              \nEnter month number (0 = The whole year)')
        month = int(input())
        temp_list = file_reader.read_from_file(file_path, month)
        displaytime = 'months Jan-Dec' if month == 0 else 'month ' + str(month)
        print('>> Minimum and maximum temperature for', displaytime, 'is', 
              wf.calculate_extremes(temp_list))
        input('press enter...')

    elif selection == 5:
        print('Good bye')
        return False

    else:
        print('Undefined selection:', selection)
        input('press enter...')

    return True

if __name__ == '__main__':
    cont = True
    while cont:
        try:
            cont = user_interface()
        except:
            print('An error occurred, please try again')
            input('press enter...')
