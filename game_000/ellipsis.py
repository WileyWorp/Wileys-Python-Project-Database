import sys
import time as t
# Function to update the line
def update_line(text):
    sys.stdout.write('\r' + text)  # Move the cursor to the beginning of the line and write text
    sys.stdout.flush()  # Ensure the text is displayed immediately

def ellipsis():
    message = "Your random game board will be"
    update_line(message)
    t.sleep(1)

    update_line(message + ".")
    t.sleep(.5)

    update_line(message + "..")
    t.sleep(.5)

    update_line(message + "...")
    t.sleep(.5)

    sys.stdout.write("\n")