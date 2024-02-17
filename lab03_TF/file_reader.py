import csv
import datetime

# read temperature data from the file filename, 
# read temperatures only for the month given as argument for month or alla months if month is 0 
# (if no month given all months are included by default)
def read_from_file(filename, month=0):
    result_list = []
    #open the file and process it
    with open(filename, "r", newline="") as csv_file:
        
        #csv module will handle the comma-seperated values
        for line in csv.DictReader(csv_file):
            #print(line) # uncomment if you want to know how the line appears after interpreted by the csv module
            
            #find out if the current line matches the wanted month
            if month == 0 or datetime.date.fromisoformat(line.get("date")).month==month:
                result_list.append(float(line.get("temp")))
    return result_list