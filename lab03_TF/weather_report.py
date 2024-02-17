from pathlib import Path
import file_reader
import weather_functions as wf

# The file name is actually 'temperature_data.csv' but added some extra path-stuff here
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperature_data.csv'


choice = ""
while not (choice == "q" or choice == "Q"):
    print("1 - average temperature")
    print("2 - arrival of spring")
    print("Q - quit")
    choice = input("Enter your choice: ")
    month = int(input("For month (1-12, 0 = all): "))
    while month not in range(13):
        print("Input ERROR - Incorrect month")
        month = int(input("For month (1-12, 0 = all): "))
    temp_list = file_reader.read_from_file(file_path,month)

    if choice == "1":
        #read month 2 temperatures from data.csv
        avg_temp =  wf.calculate_avg_temp(temp_list)
        print(format(avg_temp,'.2f'))
    elif choice == "2":
        print(wf.when_is_it_spring(temp_list))