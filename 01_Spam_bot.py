#import Module pyautogui and time
import pyautogui,time
time.sleep(4)                    #set time to put your cursor 
i=0                              #variable
n=100                            #no. of messages  you wants to send

while i<n:                       #use while loop to type n times
    pyautogui.typewrite("hello world")      #use typwriter function of pyautogui to type message
    pyautogui.press("enter")                #use press on enter to send messages
    i=i+1                                   #for i incriment to execute while loop  n times


#how to use
#run this program in python compiler and put the cursor of mouse to the messenegrs, what's inbox
# where you put your cursor it start typing

#note: use it for fun, not for any illegal activity
