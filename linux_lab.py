

# This code demonstrat dictionary, list, if condition, function and while loop
#  First validat user credential, then let user to take a short Linux test 
#  finaly print the the result and prompt user whether to take the test agin #  or not
# Date 11/01/2020

# create a dictionary
user_data = { "user1":"u1", "user2": "u2","user3":"u3", "user4":"u4","user5":"u5" }


account = input("Do you have account (yes/no): ").lower()
#validat user input
def yes_no(account):
    while not (account == "yes" or account == "no" ):
        account = input(account + " Is not valid, please type only  (yes/on) in/up ")
        if(account == "yes" or account == "no"):
            return account

yes_no(account)

#promte a new user to create account
if(account != "yes"):
    user_name = input("Enter your user name to create account: ")
    password = input("Enter your password:  ")
    user_data[user_name]= password
    print(user_name + " Account successfully created, Now you can start the test")

#validat existing user credential
if(account == "yes"):
    user_name = input("Enter your user name: ")
    check_user = user_name in user_data.keys()
    while (check_user != True):
        user_name = input("user name is not valid, try again  ")
        check_user= user_name in user_data.keys()

    password = input("Please enter your password: ")
    check_password = password in user_data.values()
    attempt = 0
    while (check_password == False):
        attempt += 1
        password = input("Invalid password, try again: ")
        check_password = password in user_data.values()
        if(attempt == 2):
            print(f"Good bye! ")
            quit()

while True:
        correct = 0
        wrong = 0
        answer1 = input("which key will give you the ability to auto complete sequence of letter  ").lower()
        if answer1 != "tab":
            wrong += 1
            print(f"Sorry {answer1} is not correc")
        else:
            print("Correct!")
            correct += 1

        answer2 = input("Validate that you are in home directory ")
        if answer2 != "pwd":
            wrong += 1
            print(f"Sorry {answer2} is not correc")
        else:
            correct += 1
            print("[labsuser@"+ user_name + "~]$\n/home/" + user_name)
   
        create_dir1 = input("create a folder under your home directory ").split()
        size = len(create_dir1)
        if (size >= 2):
            if (create_dir1[0] != "mkdir"):
                wrong += 1
                while (True):
                    create_dir1 = input(f"Sorry, {create_dir1[0]} is not correct command to create {create_dir1[1]} directory, try agine ").split()
                    if(create_dir1[0] == "mkdir"):
                        break
        elif (size == 1):
            wrong += 1
            while (create_dir1[0] != "mkdir"):
                create_dir1 = input(f"Sorry, {create_dir1[0]} is not a correct command to create a director, also you did not pass directory name  try agine ").split()
            if (create_dir1[0] == "mkdir"):
                issize = True
                while (issize):
                    create_dir1 = input(f"Sorry, you did not passed directory name after {create_dir1[0]}  command, try agine ").split()
                    if (len(create_dir1) >= 2):
                        issize = False
                
        else:
            correct += 1
            print(f"{create_dir1[1]} directory has been successfully created")

        cd = input(f"change your dir to {create_dir1[1]} ").split()
        size_cd = len(cd)
        if (size_cd >= 2) :
            while (cd[0] != "cd"):
                wrong += 1
                cd = input(f"Sorry, {cd[0]} is not a correct command to change directory {create_dir1[1]} directory, try agine ").split()
            if(cd[1] != create_dir1[1]):
                while True:  
                    cd = input(f"""Sorry, there is no such {cd[1]}  directory, check your path and try agine """).split()
                    if(cd[1] == create_dir1[1]):
                        break
        elif (size_cd == 1):
            wrong += 1
            while (cd[0] != "cd"):
                    cd = input(f"Sorry, {cd[0]} is not a correct command to change directory {create_dir1[1]} directory, try agine ").split()
            if(cd[0] == "cd"):
                while True:
                    cd = input(f"Sorry You forgot to pass the path of {create_dir1 [1]} directory, try agine ").split() 
                    if len(cd) >= 2:
                        break
        else: 
            correct +=1
            check = input(f"Great job!, your current direcory is {create_dir1 [1]} ")

        create_dir2 = input(f"create sub folder inside your {create_dir1[1]} home directory ").split()
        siz = len(create_dir2)
    
        if siz >= 2:
            while (create_dir2[0] != "mkdir"):
                create_dir2 = input(f"Sorry, {create_dir2[0]} is not a correct command to create {create_dir1[1]} directory, try agine ").split()

        elif siz == 1:
            while (create_dir2[0] != "mkdir"):
                create_dir2 = input(f"""Sorry, {create_dir2[0]} is not a correct command to create a 
                director, also you did not pass directory name  try agine """).split()
                if (create_dir2[0] == "mkdir"):
                    while (True):
                        create_dir2 = input(f"Sorry, you did not passed directory name after {create_dir2}[0]command, try agine ").split()
                        if (len(create_dir2) >= 2):
                            break

        else:
            correct += 1
            print(f"{create_dir2[1]} directory has been successfully created inside {create_dir1[1]}")

        cd1 = input(f"change your dir to {create_dir2[1]} ").split()
        if (cd1[0] != "cd"):
            wrong += 1
            ans = True
            while (True):  
                cd1 = input(f"""Sorry, {cd1[0]} is not a correct command to change directory 
                {create_dir2[1]} directory, try agine """).split()
                if(cd1[0] == "cd"):
                    break

        if (cd1[1] != create_dir2[1] ):
            chang_d = True   
            while chang_d:  
                cd1 = input(f"""Sorry, no such {cd1[1]} directory {create_dir2[1]} directory, try agine """).split()
                if(cd1[1] == create_dir2[1]):
                    chang_d =False
        else:
            correct +=1
            print("Nice job")
        file = input(f"Please create empty file inside {create_dir2[1]} ")
        if (file[0] != "thouch"):
            wrong += 1
            while (cd1[0] != "cd"):  
                file = input(f"""Sorry, {file.get(0)} is not the correc command to create file
                {create_dir2[1]} directory, try agine """).split()
            else:
                correct +=1
                print(f"Nice job, you have created {file[0]} inside [{create_dir2[1]}] directory ")
        
        validat = input("Great job,  validat your current directory ").lower()
        
        if (validat == "pwd"):
            correct += 1
            print(f"/home/labsuser/{create_dir1[1]}/{create_dir2[1]}")
        else:     
                wrong += 1
                validat = input(f"Sorry,  {validat} not correct use (pwd) to check your current directory ")
                print(f"/home/labsuser/{create_dir1[1]}/{create_dir2[1]}")
            
        add = correct + wrong
        total = (correct * 100)//add
        print(f""" *** SCORE ***
            Correct: {correct}       
            Wrong  : {wrong} 
            total  : {total}% """ )
            
            
        response = input("Do you want to take the test again? (Yes) or (no) ").lower()
        yes_no(response)
        if response == "no":
            print("Good buy!")
            quit()



