students=[["id","name","grade"],[1,"Ravi","O"],[2,"Mitesh","A+"]]
print(students) #[['id', 'name', 'grade'], [1, 'Ravi', 'O'], [2, 'Mitesh', 'A+']]
# print(students[0])
# print(students[1])
# print(students[2])
# for i in students:
#     print(i)

#find student name and grade whose id is 2
# print("Student id 2 Name is=",students[2][1])
# print("Student id 2 Grade is=",students[2][2])

#find student name and grade by entering student id
id=int(input("enter student id to find name and grade="))
flag=False
for i in students:
    if i[0]==id:
        flag=True
        print("ID=",i[0])
        print("Name=",i[1])
        print("Grade=",i[2])

if flag==False:
    print("ID not found. Try again!!!")



