import re
from collections import namedtuple, defaultdict

GuardLog = namedtuple('GuardLog', ['time', 'action', 'id'])

with open('data/day4') as data:
    input_list = [line.strip() for line in data]


on_duty = None
sleep_time = None
shift_pat = re.compile(r'#(\d+)')

sleep_totals = defaultdict(int)
guard_naps = defaultdict(list)

for log_line in input_list:
    time_str = log_line[1:17]
    event = log_line[19:]

    shift_id = shift_pat.search(log_line, pos=19)
    if shift_id:
        on_duty = int(shift_id.group(1))
    else:
        time = int(time_str[-2:])
        if 'sleep' in log_line[19:]:
            sleep_time = time
        else:
            sleep_totals[on_duty] += time - sleep_time
            guard_naps[on_duty].append((sleep_time, time))

sleepiest = max(sleep_totals, key=sleep_totals.get)

sleep_mins = defaultdict(int)
for start, end in guard_naps[sleepiest]:
    for minute in range(start, end):
        sleep_mins[minute] += 1

most_sleepy_min = max(sleep_mins, key=sleep_mins.get)
print('part 1: {} x {} = {}'.format(sleepiest, most_sleepy_min, sleepiest * most_sleepy_min))


minute_totals = defaultdict(lambda: defaultdict(int))
for guard, nap_list in guard_naps.items():
    for start, end in nap_list:
        for minute in range(start, end):
            minute_totals[minute][guard] += 1

most_min = None
most_guard = None
most_count = 0
for minute, guard_map in minute_totals.items():
    most_nap_guard = max(guard_map, key=guard_map.get)
    most_nap_count = guard_map[most_nap_guard]

    if most_nap_count > most_count:
        most_count = most_nap_count
        most_min = minute
        most_guard = most_nap_guard

print('part 2: {} x {} = {}'.format(most_guard, most_min, most_guard * most_min))
