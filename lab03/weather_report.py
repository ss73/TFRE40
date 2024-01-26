from pathlib import Path
import file_reader

# Alternative import: import as ...
import weather_functions as wf

# Import single function from module
#from weather_functions import calculate_avg_tmp

# The file name is actually 'temperature_data.csv' but added some extra path-stuff here
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperature_data.csv'

#read month 2 temperatures from data.csv
temp_list = file_reader.read_from_file(file_path, 2)

avg_temp = sum(temp_list)/len(temp_list)

# Formatting decimal output
print('Average temperature, unformatted:', avg_temp)
print('Average temperature, using format():', format(avg_temp, '.2f'))
print('Average temperature, using round():', round(avg_temp, 2))

# Alternative import: import as...
print('Average temperature using custom loop:', wf.calculate_avg_tmp(temp_list))

# Import single function from module
#print('Average temperature using custom loop:', calculate_avg_tmp(temp_list))

temp_list = file_reader.read_from_file(file_path)
print('First day of spring is at index:', wf.when_is_it_spring(temp_list))

temp_list = file_reader.read_from_file_with_dates(file_path,0,1)
print(temp_list[0:20])
