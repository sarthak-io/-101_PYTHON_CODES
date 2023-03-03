#WHATSAPP AUTOMATION
#pip install pywhatkit
#import pywhatkit
import pywhatkit
#TAKE THESE INPUTS
Mobile = input("ENTER RECEVIER MOBILE NO.(KINDLY USE +91):\n")
Message =input("WRITE YOUR MESSAGE HERE\n")
print("NOW ENTER SENDING TIME:")
Hours=int(input("WRITE HOURS IN 24HOURS TIME CYCLE:\n"))
Min=int(input("ENTER MINUTES:\n"))          
pywhatkit.sendwhatmsg(Mobile,Message,Hours,Min,15)
