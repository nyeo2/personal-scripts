#! python3
# stopwatch.py - A simple stopwatch program.

import time, os, win32api

while True:
    timelength = input('How long?(Usage: h m s): ')
    hmstime = timelength.split(' ')
    hmsint = []
    for i in range(len(hmstime)):
        hmsint.append(int(hmstime[i]))


    start = time.time()
    end = start + hmsint[0]*3600 + hmsint[1]*60 + hmsint[2]
    current = 0
    elapse = [0]*3
    print('Started. Good luck!')
    #loop while time is not up
    while current < end:
        time.sleep(1)
        current = time.time()
        elapsed = current - start
        elapsed = int(round(elapsed))
    #calculate h m s
        elapse[0] = elapsed // 3600
        elapsed %= 3600
        elapse[1] = elapsed // 60
        elapse[2] = elapsed % 60
    
    #print timer
        os.system('cls')
        print('%.2d:%.2d:%.2d' % (elapse[0], elapse[1], elapse[2]))
    
    #when out of loop, end timer
    alerttext = hmstime[0] +  ' Hours, ' + hmstime[1] + ' Minutes, ' + hmstime[2] + ' Seconds have elapsed! Continue?'

    val = win32api.MessageBox(0, alerttext, 'Time\'s up! Have a break.', 0x00001034) 
    if val == 7:
        break

input('Good Work! (enter to exit)')

