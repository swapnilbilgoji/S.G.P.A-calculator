name=input("Enter the name :")
noOfElement=int(input("Enter the number of subject you have"))
marks=[]
credits=[]
result=[]
totalResult=0
totalCredits=0

for i in range (noOfElement):
    marks.append(int(input(f"Enter the mark of sub {i+1} marks")))
    
for i in range (noOfElement):
    credits.append(int(input(f"Enter the credits point of sub {i+1} marks")))
     
for i in range(len(marks)):
    if marks[i]>100:
        print(f"You have enter marks more than 100  it is {marks[i]} please check it")
        exit()
        

if len(marks)==len(credits):
             for i in range(len(marks)):
                 result.append(marks[i]*credits[i])
                 
print(result)
        
for i in range (len(credits)):
            totalCredits+=credits[i]            
print(totalCredits)
            
for i in range (len(result)):
             totalResult +=result[i]             
print(totalResult)
         

SGPA=totalResult/totalCredits 
if SGPA >999:
             print(SGPA/1000)
elif SGPA >99:
             print(SGPA/100)
elif SGPA >9:
             print(SGPA/10)                                
    
        
    


   



       





# list1 = [2, 4, 6, 8]
# list2 = [1, 3, 5, 7]
# result = []

# Check if the two lists have the same length
# if len(list1) == len(list2):
#     # Loop through the two lists and multiply corresponding elements
#     for i in range(len(list1)):
#         result.append(list1[i] * list2[i])
#     print(result)
# else:
#     print("The two lists do not have the same length")
