# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phoneBook={}
for i in range(0,n):
    value=str(input()).split(" ")
    name=value[0]
    phoneNumber=int(value[1])
    phoneBook[name]=phoneNumber

while True:
    try:
        name = input()
        if name in phoneBook:
            phoneNumber=phoneBook[name]
            print(name +"=" +str(phoneNumber))
        else:
            print('Not found') 
    except: 
        break
