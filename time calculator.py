def add_time(start, duration, inputDay = False):

    #separate hours and minutes if start and duration time, and convert them into integers. 
    start_parts = start.split(":")
    start_hour =int(start_parts[0])
    start_minutes = int(start_parts[1].split()[0])
    ampm = start_parts[1].split()[1]

    duration_parts = duration.split(":")
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    total_minutes = duration_minutes + start_minutes
    carry_hours = 0

# day of the week
    daysOfWeek_first = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
        }
    daysOfWeek_second = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        }
    
# getting current day
    if inputDay != False:
        currentDay = daysOfWeek_first[inputDay.title()]
    else:
        currentDay = 0

# adding minutes 
    if total_minutes > 60:
        while total_minutes > 60:
            total_minutes = total_minutes - 60
            carry_hours += 1
    elif total_minutes == 60:
        total_minutes = 0
        carry_hours += 1

    different_day = False
    days = 0
# adding hours
    total_hours = start_hour + duration_hours + carry_hours
    if total_hours >= 12:
        while total_hours >= 12:
            total_hours = total_hours - 12
            if ampm == "AM":
                ampm = "PM"
            elif ampm == "PM":
                ampm = "AM"
                different_day = True
                days += 1
# adding number of days to current day

    newDayNumber = currentDay + days
    while newDayNumber > 7:
        newDayNumber = (newDayNumber%7)

    if inputDay != False:
        newDay = daysOfWeek_second[newDayNumber]

# modifying output
    if total_minutes < 10:
        total_minutes = "0" + str(total_minutes)
    if total_hours == 12 or total_hours == 0:
        total_hours = "12"
    
    if currentDay == 0:
        if days != 0 and days != 1:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm + " " +"(" + str(days) + " days later)"
        elif days == 1:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm + " " +"(next day)"
        elif days == 0:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm
    else:
        if days != 0 and days != 1:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm + ", " + newDay + " " +"(" + str(days) + " days later)"
        elif days == 1:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm + ", " + newDay + " " +"(next day)"
        elif days == 0:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + ampm + ", " + newDay

    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))