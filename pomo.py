#------------------------------------------------------------------------------
#   - Pomo Timer -
#   - By: Klassh -
#   A timer to run on the bottom of the terminal
#------------------------------------------------------------------------------

# import time and other dependancies
import sys
import time

def countDown(t):
    t = t * 60
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

if len(sys.argv) > 1:
    
    t = sys.argv[1]
else:
    t = 25
countDown(int(t))
