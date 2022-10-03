import functools


def smallest_time():
    """
        This method return smallest time from a list of given time in a day
    """
    all_visit_time = [
        '2:36 AM', '4:05 AM', '1:22 PM', '1:03 AM', '3:04 PM', '2:17 AM',
        '1:55 AM', '10:12 AM', '5:12 PM'
    ]
    am_12h_time = []
    am_time = []
    pm_12h_time = []
    pm_time = []

    for visit_time in all_visit_time:
        if 'AM' in visit_time:
            if '12' == visit_time[:2]:
                am_12h_time.append(visit_time.split(' ')[0])
            else:
                am_time.append(visit_time.split(' ')[0])
        elif 'PM' in visit_time:
            if '12' == visit_time[:2]:
                pm_12h_time.append(visit_time.split(' ')[0])
            else:
                pm_time.append(visit_time.split(' ')[0])

    print(am_12h_time, am_time, pm_12h_time, pm_time)

    def smallest_12h_time(_12h_time, am_pm):
        minute_list = list(map(lambda hour_minute: int(hour_minute.split(':')[1]), _12h_time))
        smallest_minute = functools.reduce(lambda m1, m2: m1 if m1 < m2 else m2, minute_list)
        return f'12:{str(smallest_minute).zfill(2)} {am_pm}'

    def smallest_time(time1, time2):
        time1_hour, time1_minute = [int(x) for x in time1.split(':')]
        time2_hour, time2_minute = [int(x) for x in time2.split(':')]

        if time1_hour == time2_hour:
            if time1_minute < time2_minute:
                return time1
            else:
                return time2
        elif time1_hour < time2_hour:
            return time1
        else:
            return time2

    if len(am_12h_time) > 0:
        return smallest_12h_time(am_12h_time, 'AM')

    elif len(am_time) > 0:
        smallest_am_time = functools.reduce(lambda t1, t2: smallest_time(t1, t2), am_time)
        return f'{smallest_am_time} AM'

    elif len(pm_12h_time) > 0:
        return smallest_12h_time(pm_12h_time, 'PM')

    elif len(pm_time) > 0:
        smallest_pm_time = functools.reduce(lambda t1, t2: smallest_time(t1, t2), pm_time)
        return f'{smallest_pm_time} PM'


print("Smallest time: ", smallest_time())
