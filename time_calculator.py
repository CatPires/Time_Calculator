def add_time(start, duration, day = None):
    import re
    # begin
    start_time = re.findall('(\d+)(:)(\d+)(\s)(\w+)',start)
    duration_time = re.findall('(\d+)(:)(\d+)',duration)

    ## minutes
    first_minutes = int(start_time[0][2])
    second_minutes = int(duration_time[0][2])
    total_minutes = first_minutes + second_minutes
    final_minutes = total_minutes%60

    if final_minutes < 10:
        result_minutes = '0'+str(final_minutes)
    elif final_minutes >= 10:
        result_minutes = str(final_minutes)

    ## hours
    if start_time[0][4] == 'AM':
        first_hour = int(start_time[0][0])
    elif start_time[0][4] == 'PM':
        first_hour = int(start_time[0][0]) + 12

    second_hour = int(duration_time[0][0])
    my_hour = first_hour + second_hour + total_minutes//60

    if (my_hour%24 < 12) & (my_hour%24 > 0):
        final_time = str(my_hour%24)+':'+result_minutes+' AM'
    elif (my_hour%24 == 0):
        final_time = str(my_hour%24 + 12)+':'+result_minutes+' AM'
    elif my_hour%24 == 12:
        final_time = str(my_hour%24)+':'+result_minutes+' PM'
    elif my_hour%24 > 12:
        final_time = str(my_hour%24 - 12)+':'+result_minutes+' PM'

    weekdays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    # list out keys and values separately
    key_list = list(weekdays.keys())
    val_list = list(weekdays.values())

    if day == None:        
        if my_hour//24 == 0:
            clock = final_time
        elif my_hour//24 == 1:
            clock = final_time+' (next day)'
        elif (my_hour//24 != 1) & (my_hour//24 != 0):
            clock = final_time+' ('+str(my_hour//24)+' days later)'

    elif day != None:
        my_week_day = weekdays[day.lower().capitalize()] + my_hour//24
        if my_hour//24 == 0:
            clock = final_time+', '+str(key_list[val_list.index(my_week_day%7)])
        elif my_hour//24 == 1:
            clock = final_time+', '+str(key_list[val_list.index(my_week_day%7)])+' (next day)'
        elif my_hour//24 != 0:
            clock = final_time+', '+str(key_list[val_list.index(my_week_day%7)])+' ('+str(my_hour//24)+' days later)'

    return clock