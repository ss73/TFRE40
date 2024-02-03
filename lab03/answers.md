# Assignment 3 - Temperature Data

## Task 1-4
No answers requested. The source code available in [`weather_report.py`](weather_report.py)

## Task 5
> Let’s assume that you don’t have access to the built-in functions `sum` and `len`, what can you do instead? Write a function `calculate_avg_temp` that, given a list of numbers,
> calculates and returns the average of all numbers *without using either `sum` or `len`*.

```python
def calculate_avg_tmp(temp_list):
    s, l = 0, 0
    for t in temp_list:
        s += t
        l += 1
    return round(s/l, 4)

```    

## Task 6
>Now, call the function `calculate_avg_temp` and compare the result with your previous
result. Does your algorithm output the same value as you got when using the sum and
temp built-in functions?

Yes

## Task 7
>Create a file called `weather_functions.py` and move your function `calculate_avg_temp` there.

 The source code is available in [`weather_report.py``](weather_report.py) and [`weather_functions.py``](weather_functions.py)

>What happens when you run your code in the weather_report.py file?

Unless the external function is imported, there is an error: 
`Exception has occurred: NameError name 'calculate_avg_temp' is not defined`


>What happens if you run the file weather_functions.py? Why?

Nothing happens since there is no code outside of a function to execute

## Task 8
>To fix the code, we need to import the functions in the other module. Write `import
>weather_functions` at the top of `weather_report.py`. Does it make a difference when you try to run the program now? Why?

No, unless prefixing with the module name, it still produces an error

## Task 9
> If you didn’t figure it out on the previous task, to call the function `calculate_avg_temp`,
> we must now also specify in which module the function is. The module has the same name
> as the file (without the .py extension), so the following code is now required to call the
> function: `weather_functions.calculate_avg_temp(temp_list)`. 
>
> Change your code and test that it works.

Yes, it works. The source code is available in [`weather_report.py`](weather_report.py) and [`weather_functions.py`](weather_functions.py)

## Task 10, 11, 12, 13

> No answers requested

## Task 14
> Implement the function `when_is_it_spring`. The
> function takes a list of temperatures as a parameter and must return the index in the list
> that represents that day when spring arrives, i.e. first day in a period of 7 consecutive days with average temperature above 0 degrees C.

The relevant source code from [`weather_functions.py`](weather_functions.py):

```python
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
```

## Task 15
> When you run your test, what response do you get from the when_is_it_spring function?

```python
11
```

> What date does it correspond to?

*Jan 12*

> Check it by looking at the data file, does it seem reasonable?

 Yes, it's reasonable. Counting the number of consecutive days with positive temperatures starting at Jan. 12, it sums to more than 7 days. The temperature on Jan. 11 is also below 0.
```
date, temp
...
2022-01-10,1.8
2022-01-11,-0.5    <-- Negative on Jan. 11
2022-01-12,2.9     <-- Start of 7 day period above 0 
2022-01-13,7.2
2022-01-14,5.9
2022-01-15,0.5
2022-01-16,4.1
2022-01-17,3
2022-01-18,2.9     <-- End of 7 day period above 0
2022-01-19,3.5
2022-01-20,0.6
```

## Task 16
> Run the file [`spring_test.py`](spring_test.py), this file contains code that will check that your functions work.
> Instead of using the data from the CSV file, this test file will use some other data. If the test
> file reports errors, you need to fix the function so the tests show that the function works.

After fixing errors, the following output is produced:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.012s

OK
```

## Task 17
> Now, improve your main program so that it asks the user
> what it wants to do. A run could look something like this:
```
What do you want to do?
Press 1 for average temperature and 2 for the arrival of spring
1
Which month do you want to calculate the average temperature for?
Enter month number
3
The average temperature was 3.94516129032258 degrees in month 3
```

The source code is available in a separate file, [`interactive_weather.py`](interactive_weather.py)

## Task 18

No answers requested

## Task 19

> Expand your program so that the user also has the
> choice to look for the maximum and minimum temperature during a certain month.

The relevant code snippet that calculates the minimum and maximum temperature during a month (from [`weather_functions.py`](weather_functions.py)):

```python
def calculate_extremes(temp_list):
    return min(temp_list), max(temp_list)        

```    

## Task 20
> Extend your main program so that instead of the index it prints which day and month spring started.

The solution is using the fact that well formed dates are part of the `csv` file contents. An alternative load function is added to [`file_reader.py`](file_reader.py):

```python
def read_from_file_with_dates(filename, month = 0, start_index = 0):
    result_list = []
    with open(filename, "r", newline="") as csv_file:
        for line in csv.DictReader(csv_file):
            if month == 0 or datetime.date.fromisoformat(line.get("date")).month==month:
                result_list.append((line.get("date"), float(line.get("temp"))))
    # Not optimal to read all values just to discard them, but what the fudge, 365 values is like nothing
    return result_list[start_index:]
```

Rather than appending the temperatures only to the list, each day now contains a tuple with the well formed date and the temperature for that day.

Now in [`interactive_weather.py`](interactive_weather.py), the list of tuples is loaded. Since the weather functions expects a one-dimensional array of temperatures, the tuples are split up into two lists using the `*` operator and the built-in `zip` function:

```python
    date_temp_list = file_reader.read_from_file_with_dates(file_path,0,46)
    date_list, temp_list = zip(*date_temp_list)
    date = date_list[wf.when_is_it_spring(temp_list)]
    print('>> Spring arrives on day:', date)
```

Since both "sliced" lists represent the same day, the output date value has the same index as the index of the calculated first day of spring.

## Task 21
> Extend `read_from_file` so that it also takes an optional parameter
> `day`. If day&nbsp;>&nbsp;0, only temperatures for this day and later should be added to the list.

The source code is available in [`file_reader.py`](file_reader.py)

