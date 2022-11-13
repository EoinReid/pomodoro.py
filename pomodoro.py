# pomodoro app
# python3 pomodoro.py
# enter pomodoro time
# starts counter, after pomodoro time says to take break
import time
import datetime
import sys
 
def pomodoro_timer(hour, minutes, seconds):
    # Calculate the total number of seconds
    total_seconds = hour * 3600 + minutes * 60 + seconds
 
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        # Prints the time left on the timer
        print(timer, end="\r") # using end = \r here returns the next stdout line to the beginning of the line without proceeding to the next line. i.e overwrites the previous print
        # so instead of the time printing every time it counts down, the same print is getting over written, like an actual clock.
      #  print(timer)
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1        
 
    print("ring ring, time for a break!")

if len(sys.argv) < 2:
    print("Usage: python3 pomodoro.py [h] [m] [s] e.g python3 pomodoro.py 0 30 0 = 30 minute timer" )
    sys.exit()
# assign h,m,s values based on terminal arguments
hour = sys.argv[1]
minutes = sys.argv[2]
seconds = sys.argv[3]
print("🍅Eoin's Pomodoro Timer".center(30))
pomodoro_timer(int(hour), int(minutes), int(seconds))