#! python3
# stopwatch.py - A simple stopwatch program.

import time

print('Enter to start, Ctrl+C to stop')
c = input()

start = time.time()
previous = start
lapnum = 1

try:
    while True:
        c = input()
        current = time.time()
        print('Lap #%s %s (%s)' % (lapnum, round(current-start,2), round(current-previous,2)))
        lapnum += 1
        previous = current
except KeyboardInterrupt:
    print('\nDone')
