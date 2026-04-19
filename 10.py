#Simple Interest: Input principal, rate, and time. Calculate and print the Interest (P×R×T/100)
principal=int(input("the principal is  "))
rate=int(input("the rate is  "))
time=int(input("the time is  "))
interest=(principal*rate*time)/100
print("the interest is ",interest)