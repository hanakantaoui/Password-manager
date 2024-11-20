
print("\033[35m"+"----------------------------|| <<Welcome to my password manager>>||----------------------------"+"\033[0m")

from cryptography.fernet import Fernet

# generate encryption key

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fr = Fernet(key)


def add():
    name     = input("\033[32m"+"------------Account name------------ : "+"\033[0m")
    password = input("\033[32m"+"------------Password---------------- : "+"\033[0m")

    with open("password.txt","a") as f:
        f.write(f"{name} | {fr.encrypt(password.encode()).decode()}\n")


def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name,password = data.split("|")
            print(f"User : {name} , Password : {fr.decrypt(password.encode()).decode()}")


while True:
    print("\033[36m"+"========Menu=======:"+"\033[0m")
    print("add : to add a new psw.\nview : to view your psw . \nq|Q: quit form yor app.")

    mode = input("\033[34m"+
        "What do you want to do ? "+"\033[0m").lower()
    
    if mode == "q":
        cleck= input("\033[32m"+"---------------Are you sure?--------------:"+"\033[0m").lower()
        if cleck=="yes":
         print("\033[35m"+"---------------------------------|| <<Quit from your app !!>> ||-----------------------------------"+"\033[0m")
         break
        elif cleck =="no":
            continue

    elif mode == "add":
        add()
    elif mode == "view":
        view()   
    else:
        print("\033[31m"+"Invalid Mode !"+"\033[0m")
        continue   
