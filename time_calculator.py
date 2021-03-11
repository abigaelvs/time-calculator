def add_time(start, duration, starting_day=False):

    # Index day of the week
    days_of_the_week_index = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    # am and pm flip
    am_and_pm_flip = {'AM': 'PM', 'PM': 'AM'}
    

    # day of the week in array
    days_of_the_week_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # split time and period(am or pm) (03:00 PM)
    clock, period = start.split()

    # split start_time to know start_hour and start_minute
    start_time = clock.split(':')
    start_hour = int(start_time[0])
    start_minute = int(start_time[1])

    # split duration to know duration_hour and duration_minute
    duration_clock = duration.split(':')
    duration_hour = int(duration_clock[0])
    duration_minute = int(duration_clock[1])

    amount_of_days = int(int(duration_hour) / 24)

    total_minute = start_minute + duration_minute
    if (total_minute >= 60):
        start_hour += 1
        total_minute = total_minute % 60
    
    amount_of_am_pm_flips = int((start_hour + duration_hour) / 12)

    total_hour = (start_hour + duration_hour) % 12

    total_minute = total_minute if total_minute > 9 else '0' + str(total_minute)
    total_hour = total_hour = 12 if total_hour == 0 else total_hour
    
    if (period == 'PM' and int(start_hour) + (int(duration_hour) % 12) >= 12):
        amount_of_days += 1

    period = am_and_pm_flip[period] if amount_of_am_pm_flips % 2 == 1 else period

    
    new_time = f"{total_hour}:{total_minute} {period}"
    
    if (starting_day):
        starting_day = starting_day.lower()
        print(starting_day)
        index = int((days_of_the_week_index[starting_day]) + amount_of_days) % 7
        new_day = days_of_the_week_array[index]
        new_time += f", {new_day}"
    
    if (amount_of_days == 1):
        return new_time + f" (next day)"
    elif (amount_of_days > 1):
        return new_time + f" ({amount_of_days} days later)"
    
    return new_time