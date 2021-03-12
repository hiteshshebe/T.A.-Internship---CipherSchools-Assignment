#pattern1
print("they 1 st pattern are below")
l1=10
for x in range(1,6):
    print(" "*l1,end='')
    print('* '*x)
    l1=l1-2


#the 2 nd pattern are above


print("2 nd pattern of alphabates")


num = 65
for i in range(0, 5):
    for j in range(0, i + 1):
        ch = chr(num)
        print(ch, end=" ")
        num = num + 1
    print("\r")

