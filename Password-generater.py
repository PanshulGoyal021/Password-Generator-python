from random import choice

chars = "qwertyuiopasdfghjklzxcvbnm1234567890!@$%&QWERTYUIOPASDFGHJKLZXCVBNM"
password = ""
passwords = []

with open("passwords.txt", "w") as f:
    pass

with open("passwords.txt", "r") as f:
    for line in f:
        passwords.append(line.strip())

length = int(input("enter length : "))
for i in range(length):
    password += (choice(chars))
print(password)
        
m = input(f" \n what is this password for : ")

passwords.append(f"{m} : {password}")

with open("passwords.txt", "w") as f:
    f.write("\n".join(passwords))