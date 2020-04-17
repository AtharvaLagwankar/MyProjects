def rem(inputlist , inputvalue):
    number = inputlist.count(inputvalue)
    for i in range(0,number):
        inputlist.remove(inputvalue)
    return inputlist

my_list = []
print("ENTER NUMBERS FOR THE LIST (TYPE 'q' TO STOP ENTRY)")
w = input()

while w != "q":
     my_list.append(float(w))
     w = input()

print(my_list)
num = input("ENTER THE VALUE TO BE REMOVED FROM THE DISPLAYED LIST :")
while num != "q":
    my_list = rem(my_list, float(num))
    print(my_list)
    num = input("ENTER THE VALUE TO BE REMOVED FROM THE DISPLAYED LIST (TYPE 'q' TO END EDITING) :")

print("THE FINAL LIST IS : ", my_list)