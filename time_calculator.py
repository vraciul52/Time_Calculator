def add_time(start_time, duration, starting_day=None):
    # Split the start_time into hours, minutes, and period (AM/PM)
    start_time, period = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Split the duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start_time to 24-hour format
    if period == "PM":
        start_hour += 12
    
    # Calculate total minutes
    totminutes = (start_hour * 60 + start_minute) + (duration_hour * 60 + duration_minute)
    
    # Calculate the new time in 12-hour format
    new_hour = totminutes // 60 % 24
    new_minute = totminutes % 60
    
    # Determine the period (AM/PM) for the new time
    new_period = "AM"
    if new_hour >= 12:
        new_period = "PM"
    if new_hour > 12:
        new_hour -= 12
    
    # Calculate the number of days later
    days_later = totminutes // (24 * 60)
    
    # Determine the day of the week if starting_day is provided
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        starting_day_index = weekdays.index(starting_day)
        new_day_index = (starting_day_index + days_later) % 7
        new_day = weekdays[new_day_index]
    
    # Generate the new_time string
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    if starting_day:
        new_time += f", {new_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time
