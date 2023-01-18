# Now let study about list and  tuple 
#   now let us create a list
 
# hnfioehsfgnlkn
list = ["shubham","kunam","apple",21,True]
# we have created a list 


# let use an loop 

for item in list:
    print(item,end=" ")
# output 
#     shubham kunam apple 21 True 


# Nice 

# Now let us try to insert new element in a empty list 

item=int(input("Enter the number of items to insert in the list: "))
list=[]
i=0
for i in range(item):
    data=input("Enter the item name : ")
    list.append(data)

print(list)

# now let do a student data project

item=int(input("Enter the number of data: "))
name=list=[]
Roll=list=[]
i=0
for i in range(item):
     nameoFstudent=input("Enter the student's name : ")
     studentRoll=int(input("Enter the student's Roll number : "))
     name.append(nameoFstudent)
     Roll.append(studentRoll)
     print("\n")

print("RollNo.  Name")
for item in range(item):

    print(Roll[item], "\t",name[item],"\n")


    # Nice done 
