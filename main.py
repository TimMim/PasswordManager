def Read():
    file = open("Storage", "r")
    readOutput = file.readlines()
    
    alldata = []
    for line in readOutput:
        alldata.append(line.strip())
    
    while True: #Username
        chooserName = input("Which Username do you want to have (Example: 1, 3, 5)")
        
        try:
            print(alldata[int(chooserName) - 1])
            break
        except:
            print("This is not a valid number! Please enter again!")
            continue
    
    while True: #Passwort
        chooserPassword = input("Which Password do you want to have (Example: 1, 3, 5)")
        
        try:
            print(alldata[int(chooserPassword) - 1])
            break
        except:
            print("This is not a valid number! Please enter again!")
            continue
    print("If you want to add new Details or view others, restart the program!")
    file.close


def Add():
    file = open("Storage", "a")

    username = input("Input your Username:")
    password = input("Input your Password:")

    file.write("Username: " + username + "\n")
    file.write("Password: " + password + "\n")

    print("You have succesfully added "+ username + " and "+ password+ " to your Database!")
    print("If you want to add new Details or view others, restart the program!")
    file.close

while True:

    userInput = input("Do you want to Read (1) or Add(2) a Password to the list?")
    if userInput == "1":
        Read()
        break
    
    elif userInput == "2":
        Add()
        break

    else:
        print ("Please enter a valid command")
        continue