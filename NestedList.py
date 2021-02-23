# Utilize  Nested  List  concept  to  display multiplication tables from 1-10
list1= [] # create a empty list
table=1
for i in range(10):

    # Append an empty sublist inside the list
    list1.append([])

    for j in range(1,11):
        list1[i].append(table*j)

    table=2+i
print(list1)