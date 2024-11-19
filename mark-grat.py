total_mark = int(input("Inter your mark for calculate your gade: ")) 

if total_mark <= 100 and total_mark >= 90:
    print("You got A+")
elif total_mark < 80 and total_mark >= 70:
    print("You got A")
elif total_mark <70 and total_mark >= 60:
    print("You got A-")
elif total_mark < 60 and total_mark >= 50:
    print("You got B")
elif total_mark < 50 and total_mark >= 40:
    print("You got C")
elif total_mark < 40 and total_mark >= 33:
    print("You got D")
    
else:
    print("F")