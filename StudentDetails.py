# Enter student name and three subject marks calculate
students=dict()
n=int(input("Enter Number of student:"))
for i in range(1,n+1):
    list1=[]
    temp=dict()
    temp["Name"]=input("Enter Student name:")
    temp["Roll No"]=input("Enter Roll Number:")
    temp["Marks"]=list1
    for j in range(1,4):
        m=int(input("Enter marks:"))
        list1.append(m)
    temp["total"]=list1[0]+list1[1]+list1[2]
    students[i]=temp
    for key in students.keys():
        print(key,students[key])