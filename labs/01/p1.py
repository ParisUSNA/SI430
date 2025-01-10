filename = input("Filename: ")

fruit = {}
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            i = line.split()
            fruit[i[0]] = float(i[1])
except OSError:
    print("File not found!")
    exit()

cart = {}

cmd = ""
while(cmd != "checkout"):
    cmd = input("command: ")
    cmdsplit = cmd.split()
    if(cmdsplit[0] == "add"):
        if(cmdsplit[3] in fruit):
            if(cmdsplit[3] in cart):
                cart[cmdsplit[3]] += float(cmdsplit[1])
            else:
                cart[cmdsplit[3]] = float(cmdsplit[1])
        else:
            print(f"Error! {cmdsplit[1]} not found!")
    elif(cmdsplit[0] == "price"):
        try: 
            print(f"{cmdsplit[1]} are ${fruit[cmdsplit[1]]} per pound")
        except:
            print(f"Error! {cmdsplit[1]} not found!")


total = 0
for i in cart:
   total += cart[i] * fruit[i]

print(f"total is ${total}")
