#Apple Sharing: Input the total number of apples and the number of students. Print how many apples each student gets and how many are left over using %
student=int(input("the student are "))
apples=int(input("the apples are "))
apples_got=apples//student
apples_remaining=apples%student
print("apples every student got ",apples_got)
print("the remaining apples are",apples_remaining)