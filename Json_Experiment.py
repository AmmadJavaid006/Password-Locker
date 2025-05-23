import json

try:
    with open('example.json', 'r' ) as file:
        data = json.load(file)
    
        for key, value in data.items():
            print(key.capitalize())
            print(f"Username : {value['username']}")
            print(f"Password : {value['password']}")

except FileNotFoundError:
    
    data = {}

action = input("want to add something? or want to find somthing? or want to change a password or usenamme?")

if action == "add":
    Svc = input("Service: ")
    Usn = input("Username: ")
    Pass = input("Password: ")

    data[Svc] = {

    "username" : Usn,
    "password" : Pass
    }   

elif action == "search":
    what = input("Service name: ")
    value = data.get(what, "NO SERVICE")
    print(what, value)

elif action == "change":
    uorp = input("Username or Password: ")
    if uorp == "Username":
            svc = input("OF WHICH SERVICE: ")
            data[svc]["username"] = input("Enter New Username: ")
    elif uorp == "Password":
            svc = input("OF WHICH SERVICE: ")
            data[svc]["password"] = input("Enter New Password: ")

elif action == "delete":
    svc = input("OF WHICH SVC: ")
    del data[svc]


else:
    exit()


    
with open('example.json', 'w') as file:
    json.dump(data, file, indent= 4)
