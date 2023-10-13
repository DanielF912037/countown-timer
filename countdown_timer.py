# import the time module
import time

# define the countdown function
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)

        # Print the timer with carriage return to overwrite the previous timer
        print(timer, end="\r")

        # Wait for 1 second 
        time.sleep(1)   
        t -= 1

    # Display a message when the countdown reaches zero
    print("Your time is up")  

# Get the input from the user for the countdown time
t = int(input("Enter the time you want in seconds: "))

while True:
    countdown(t)

    # asks the yser if they want to reset the timer
    reset = input("Do you wantr to reset the timer? (y/n):  ").strip().lower()
    
    # cheak if the user presses y or yes
    if reset in ['yes', 'y']: 
        t = int(input("Enter the time you want for the new countdown in seconds: "))
    else:
        break

print("Timer stoped.")