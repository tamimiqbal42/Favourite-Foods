# simple for loop using
for number in range(15):
    print(number)


    # list er khetre 
List = ['apple', 'bnana', 'lomba alu', 'A', 'b', 'C']
for eachItem in List:
    print(List[1])
    print(eachItem)

# Dictionary er jonno
examResult = {'phy':89, 'eng':70, 'ban':85}
for subject,marks in examResult.items():
    print("Subject:"+subject+ "Marks:"+str(marks))
    # othaba
    print(f"Subject:{subject} Marks:{marks}")
    
    print("{}= {}".format(subject, marks))
    # or 
    print(f"{subject} = {marks}")

# SET er jonno
numbers = {1,2,3,4,5,6,7,8,}
for number in numbers:
    if number == 5:
        continue
    elif number == 8:
        break
    print(number)
    