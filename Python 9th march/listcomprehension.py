# #method-index(),append(),insert(),pop(),remove(),reverse(),sort(),copy(),extend(),clear(),count()
# for i in range(1,11):
#     print(i,end=" ")
# #list comprehension 
# #syntax [output for iterable_variable in sequence_object]

# #print 1 to 10
# print([i for i in range(1,11)]) #1 2 3 4 5 6 7 8 9 10 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# #print 1 to 10 sqaure
# print([i*i for i in range(1,11)]) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# #print even numbers from 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i)

# print([i for i in range(1,11) if i%2==0]) #[2, 4, 6, 8, 10]

#WAP to create mylist add numbers as per count enter
# mylist=[] 
# or
# mylist=list()
# count=int(input("Enter count for numbers="))
# for i in range(count):
#     number=int(input(f"enter {i+1} number="))
#     mylist.append(number)
# print(mylist)
# or

# count=int(input("Enter count for numbers="))
# mylist_new=[int(input(f"enter {i+1} numbers=")) for i in range(count)]
# print(mylist_new)

#WAP to show even and odd numbers seperately
# mylist=[12,4,2,67,256,600,2]
# even=[]
# odd=[]
# for i in mylist:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

#OR

# [even.append(i) if i%2==0 else odd.append(i) for i in mylist]
# print("Even numbers=",even) #Even numbers= [12, 4, 2, 256, 600, 2]
# print("odd numbers=",odd) #odd numbers= [67]





