# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phoneBook={}
for i in range(0,n):
    value=list(input().split(" "))
    phoneBook[value[0]] = (value[1])

for j in range (0,n):
    key = input()
    if key in phoneBook.keys():
        print(key + "=" +phoneBook[key])
    else:
        print('Not found') 
