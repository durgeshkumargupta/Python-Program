# Find Employee basic salary and HRA
d=dict()
n=int(input("Enter Number of Employee:"))
for i in range(1,n+1):
    temp=dict()
    emp_no=input("Enter Employee Number:")
    temp['name']=input("Enter employee name:")
    temp["basic-salary"]=input("Entre basic salary:")
    temp['hra']=input("Enter HRA:")
    temp['salary']=temp['basic-salary']+temp['hra']
    d[emp_no]=temp
print(d)