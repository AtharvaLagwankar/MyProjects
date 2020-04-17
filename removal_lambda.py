my_list = []
print("ENTER NUMBERS FOR THE LIST (TYPE 'q' TO STOP ENTRY)")
w = input()
while w != "q":
    my_list.append(float(w))
    w = input()
print(my_list)
num = input("ENTER THE VALUE TO BE REMOVED FROM THE DISPLAYED LIST :")
my_list = list(filter(lambda x: x != float(num), my_list))
print("THE FINAL LIST IS : ", my_list)
