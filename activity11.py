#import demo
import getpass 

username = "minii"
password = "rhom02"

u = input("Input USERNAME ---> ")
P = getpass.getpass("Input PASSWORD ---> ")

if u == username or p == password:
        print("username and password correct")
else: 
        print("access denied ")
