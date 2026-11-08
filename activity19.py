from getpass import getpass
isLogin = False
loginAttempt = 0

u = "rhom02"
p = "hell0000"

while isLogin == False:
    uname = input("Input USERNAME --> ")
    pword = getpass("Input PASSWORD --> ")
    
    if uname == u and pword == p:
        print("Login Successfully ")
        print("Total Login Attempts ", loginAttempt)
        isLogin = True
    else:
        print("Incorrect Username and Password ")
        loginAttempt += 1
        isLogin = False     