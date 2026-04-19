#Savings Goal: Input a monthly saving amount and print how much will be saved in 5 years
saving=int(input("the total savings of the month "))
years=int(input("the total number of years "))
months=years*12
saved=saving*months
print("the total saving is",saved)