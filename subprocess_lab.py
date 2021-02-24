import subprocess

""" This is a simple python scrip that demonstrat the power of 
    subprocess module
"""
def choice():
    print("\nDo you want to assign ")
    operation = {   1:"peimery group",
                    2:"Multiple secondary group",
                    3:"create password",  
                    4:"Specific user ID",
                    5:"Specific group ID",
                    6:"Account Expirey Date",
                    7:"Password Expiry Date",
                    8:"Custome Comments",
                    9:"User Login shell",
                    10:"Lock useraccount",
                    11:"unlock user account",
                    12:"Add auser",
                    13:"Add a group"}            
               
    for key in operation:
            print(key, operation[key] )
    user_choice = int(input("Please choose one from 1 - 13: "))
    if user_choice not in operation:
        not_valid = True 
        while not_valid:
            user_choice = int(input("invalid choice, Please choose one from 1 - 11: "))
            if user_choice in operation:
                not_valid = False
    #return operation[user_choice]
    return user_choice
#choice()

def configer_user_account():
    user_pick = choice()
    if user_pick == 1:
        group_name, user_name = input("Please enter group and user name respctively: ").split()
        output = subprocess.run(["sudo", "usermod", "-g ", group_name, user_name])  
    elif user_pick == 2:
        user_pick = input("Enter user name: ")
        group_name = input("Please enter secondary group/s and user name respctively: ").split()
        output = subprocess.run(['sudo', 'usermod' ,'-a' ,'-G',  group_name ,user_name])

    elif user_pick == 4:
        id, user_pick = input("Please enter custom user ID, and along with the user name: ").split()
        output = subprocess.run(["sudo", "useradd", "-u", id , user_pick])
    elif user_pick == 10:
        user = input("Please enter user name  ")
        output = subprocess.run(["sudo","usermod","--lock", user])
    elif user_pick == 11:
        user = input("Please enter user name ")
        output = subprocess.run(["sudo","usermod","--unlock", user])
    elif user_pick == 13:                      
        group_name = str(input("Please enter group name that you wish to create: "))
        output = subprocess.run(["sudo","groupadd","-g", group_name])
    else:
        pass    


def tar_ball_file():
    new_tar_file, orginal_file = input("Enter the name of file and name that you wish archive and compresed: ")
    tar_bo = subprocess.run(["tar", ["-c"],["f"], "-z", new_tar_file, ".","tar", ".", 
    "gz",orginal_file ])

configer_user_account()

tar_ball_file()

"""
with open("tex.text", 'w') as f:
    x = subprocess.run(["ls" ,"-la "],stdout=f, text=True )
#y = subprocess.run(" ls -la ", capture_output=True )
    #f.write(str(x))
    print(x)
#print(y.returncode())
x = subprocess.run(["ls" ,"-la "],stdout=subprocess.PIPE, text=True 
)
print(x)
"""



