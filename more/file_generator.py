"""
================================================
  Python Problem Set Generator
  Run this script once to create 248 .py files,
  each containing one problem as a comment.
================================================
"""

import os
import re

# ── 1. Paste the full content of your Numbered_Questions.txt here ──
RAW_TEXT = """
Problem #1:
Professional Greeting: Input a user's first_name and last_name. Concatenate them with a space and print "Hello [Full Name], welcome to the portal!"

==================================================

Problem #2:
Address Formatter: Create a program that takes a street name, city, and zip code. Print them as a formatted mailing address with each part on a new line using \n

==================================================

Problem #3:
Invoice Tabulation: Create a string that displays a product name and its price separated by a tab space using \t

==================================================

Problem #4:
Character Limit Warning: A social media post allows 280 characters. Input a post and print its length. Use a boolean check to print True if it's within the limit

==================================================

Problem #5:
Multi-line Review: Use triple quotes to store a customer review that spans three lines and print it

==================================================

Problem #6:
Username Generator: Given a full name like "ShradhaKhapra", use slicing to extract only the first 7 characters to create a shortened username

==================================================

Problem #7:
Hidden Serial Number: A product code is "PROD-9982". Use negative indexing to print only the last 4 digits

==================================================

Problem #8:
Domain Extractor: You have an email string "user@gmail.com". Use slicing to extract and print only the "gmail.com" part

==================================================

Problem #9:
Initial Finder: Input a person's name and print only the character at index 0 to show their initial

==================================================

Problem #10:
Reverse Check (Conceptual): Take a 5-letter word and use slicing to print it from the 2nd character to the 4th character

==================================================

Problem #11:
Email Validator: Take an email input and use .endswith() to check if it ends with "@gmail.com". Print True or False

==================================================

Problem #12:
Name Fixer: A user enters their name in lowercase (e.g., "python"). Use .capitalize() to print it with the first letter in uppercase

==================================================

Problem #13:
Word Censorship: Write a program that takes a sentence and uses .replace() to change a specific "bad word" into "****"

==================================================

Problem #14:
Search Tool: Input a paragraph and a keyword. Use .find() to see if the keyword exists and print its starting index. If it returns -1, print that the word was not found

==================================================

Problem #15:
Symbol Counter: In a list of prices like "$10, $20, 30",use‘.count()‘tofindhowmanytimesthe"" symbol appears

==================================================

Problem #16:
Traffic Signal: Input a light color (Red, Yellow, Green). Use if-elif-else to print "Stop", "Look", or "Go"

==================================================

Problem #17:
Pass/Fail System: Input a student's marks. If marks are 33 or above, print "Passed", otherwise print "Failed" using an else statement

==================================================

Problem #18:
Age Group Classifier: Input an age. If less than 13, print "Child"; if between 13 and 19, print "Teenager"; otherwise print "Adult"

==================================================

Problem #19:
Temperature Alert: Input the current temperature. If it is above 35, print "It is a hot day"; if below 15, print "It is a cold day"; otherwise print "Pleasant weather"

==================================================

Problem #20:
Even/Odd Number: Input a number and use the modulo operator (%) with an if-else block to print if the number is Even or Odd

==================================================

Problem #21:
Login System: Store a saved_username and saved_password. Input a username and password from the user. Use the and operator to print "Access Granted" only if both match

==================================================

Problem #22:
Scholarship Eligibility: Input a student's marks and attendance_percentage. Use the and operator to print "Eligible" if marks > 90 and attendance > 75

==================================================

Problem #23:
Number Comparison: Input three numbers and find the greatest of them using if-elif-else with logical operators

==================================================

Problem #24:
Multiplicity Check: Input a number and check if it is a multiple of 7. If it is, print "Multiple of 7", otherwise print "Not a multiple"

==================================================

Problem #25:
Nested Discount Check: Input if a person is a "Member" (True/False). If they are a member, ask for their "Purchase Amount". If the amount is > 1000, give a 20% discount; otherwise, give a 10% discount. Use nesting for this logic

==================================================

Problem #26:
Student Record: Create a list containing a student’s name, their roll number, and their percentage. Print the list and its data type

==================================================

Problem #27:
Price Update: You have a list of prices for three items. The price of the second item has changed. Update it using its index and print the updated list

==================================================

Problem #28:
Inventory Count: Create a list of 5 items in a grocery store. Use a function to print how many total items are in your inventory list

==================================================

Problem #29:
Mixed Data Entry: Create a list that stores a city name (string), its population (int), and its average temperature (float). Access and print only the city name using its index

==================================================

Problem #30:
Index Error Safety: Create a list of 3 colors. Try to access the element at index 5 and observe the "out of range" error mentioned in the lecture

==================================================

Problem #31:
Monthly Sales: You have a list of sales for 5 months. Use slicing to create a "sub-list" containing only the first 3 months

==================================================

Problem #32:
Recent Orders: Given a list of 6 customer names, use negative indexing to print only the last two customers who placed an order

==================================================

Problem #33:
Mid-Week Extraction: Create a list of days from Monday to Friday. Use slicing to extract the middle three days (Tuesday, Wednesday, Thursday)

==================================================

Problem #34:
List Cloning: Use slicing without a starting or ending index ([:]) to create a complete copy of a fruit list

==================================================

Problem #35:
Reverse Slicing: Use negative indexing to extract the 3rd and 2nd items from the end of a list of car brands

==================================================

Problem #36:
Guest List: Start with an empty list. Ask the user for 3 guest names and use the .append() method to add them one by one

==================================================

Problem #37:
Price Sorting: You have a list of random prices. Use the .sort() method to arrange them from lowest to highest

==================================================

Problem #38:
High Score Ranking: Take a list of game scores and sort them in descending order (highest to lowest) using reverse=True inside the sort method

==================================================

Problem #39:
Alphabetical Directory: Create a list of 5 random names. Sort them alphabetically and print the result

==================================================

Problem #40:
Queue Management: You have a list of people in a line. A "VIP" guest arrives; use the .insert() method to place them at index 0

==================================================

Problem #41:
History Reverse: Create a list of steps taken to solve a math problem. Use the .reverse() method to show the steps in backward order

==================================================

Problem #42:
Cancel Order: A customer cancels an order for "Laptop". Use the .remove() method to find and delete "Laptop" from your product list

==================================================

Problem #43:
Task Completion: You have a "To-Do" list. Use the .pop() method to remove the item at index 2 once it is completed, and print the removed item

==================================================

Problem #44:
Clearance Sale: Use .pop() without any index to remove the very last item from a store shelf list

==================================================

Problem #45:
Duplicate Removal: You have a list with the name "Aman" appearing twice. Use .remove("Aman") and observe which occurrence gets deleted

==================================================

Problem #46:
Fixed Coordinates: Create a tuple to store the Latitude and Longitude of a location. Try to change the Latitude and observe the error, proving tuples are immutable

==================================================

Problem #47:
Product ID Check: Store 5 product IDs in a tuple. Use the .count() method to find out how many times a specific ID appears

==================================================

Problem #48:
Search Position: Given a tuple of months, use the .index() method to find the position (index) of "March"

==================================================

Problem #49:
Single Item Trap: Create a tuple with only one item (a single grade 'A'). Ensure you use a comma so Python recognizes it as a tuple rather than an integer or string

==================================================

Problem #50:
Palindrome Challenge: Create a list of numbers (e.g., ). Create a copy of it, reverse the copy, and check if the original list is equal to the reversed copy to determine if it is a palindrome

==================================================

Problem #51:
Student Profile: Create a dictionary called student with keys for name, age, and grade. Print the dictionary and its type

==================================================

Problem #52:
Price Check: Create a menu dictionary for a cafe (e.g., "coffee": 2.5). Ask the user for an item and print its price using the key

==================================================

Problem #53:
Update Inventory: You have a dictionary of fruit_stock. Update the quantity of "apples" and print the updated dictionary

==================================================

Problem #54:
New Entry: Create a phonebook dictionary. Add a new contact name and number using the assignment operator

==================================================

Problem #55:
Data Type Variety: Create a dictionary where one value is a string, one is an integer, and one is a list of hobbies

==================================================

Problem #56:
Key Listing: Create a warehouse dictionary. Use the .keys() method to print all product names available

==================================================

Problem #57:
Salary Audit: Create a staff_salaries dictionary. Use the .values() method to print only the salary amounts

==================================================

Problem #58:
Pair Display: Use the .items() method to print all "Product: Price" pairs from a grocery_store dictionary as tuples

==================================================

Problem #59:
Safe Access: Use the .get() method to check for a "discount_code" in a dictionary. Ensure the program doesn't crash if the code is missing

==================================================

Problem #60:
Merge Teams: You have two dictionaries, team_a and team_b. Use the .update() method to merge all members of team_b into team_a

==================================================

Problem #61:
Grade Book: Create a nested dictionary where each student's name is a key, and their value is another dictionary of subject: marks

==================================================

Problem #62:
Deep Access: From the student_marks nested dictionary, access and print only the "Math" marks of a specific student

==================================================

Problem #63:
Office Directory: Create a nested dictionary for a company with Departments. Each department should contain a list of employee names

==================================================

Problem #64:
City Weather: Create a dictionary where keys are city names and values are dictionaries containing temperature and humidity

==================================================

Problem #65:
Library System: Store book details (Author, Year) inside a nested dictionary where the Book Title is the main key

==================================================

Problem #66:
Unique Visitors: You have a list of names of people who entered a building (some names repeat). Convert this list into a set to find the unique visitors

==================================================

Problem #67:
Skill Set: Create a set of programming_languages. Use the .add() method to add a new language and see how it handles duplicates

==================================================

Problem #68:
Cleanup: Create a set of expired_items. Use the .remove() method to delete a specific item from the set

==================================================

Problem #69:
Empty Set Logic: Initialize an empty set correctly using set() and print its type to ensure it's not a dictionary

==================================================

Problem #70:
Random Pop: Create a set of raffle_tickets. Use the .pop() method to remove and print a random winning ticket

==================================================

Problem #71:
Mutual Friends: You have two sets of friends for "User A" and "User B". Use the intersection method to find common friends

==================================================

Problem #72:
Party Guest List: Combine two sets of guest names using the union method to create a final invitation list without duplicates

==================================================

Problem #73:
Classroom Requirement: Given a list of subjects like ["Math", "Science", "Math", "English"], use a set to find the total number of unique classrooms needed

==================================================

Problem #74:
Clear Cache: Create a set representing a temporary data cache. Use the .clear() method to empty it and print the result

==================================================

Problem #75:
Mixed Set Safety: Try to add a list to a set and observe the unhashable type error; then replace it with a tuple to see it succeed

==================================================

Problem #76:
Automated Emailer: Simulate sending 10 emails by printing "Email sent to user [i]" using a while loop

==================================================

Problem #77:
Countdown Timer: Create a variable timer = 10. Use a while loop to print the value and decrease it until it reaches 1

==================================================

Problem #78:
Login Attempts: Set a variable attempts = 0. While attempts < 3, ask for a password. If wrong, increment the attempt counter

==================================================

Problem #79:
Multiplication Table: Input a number n and use a while loop to print its table from 1 to 10 (n×1 to n×10)

==================================================

Problem #80:
Dynamic Summer: Ask the user for a number n. Use a while loop to calculate the sum of the first n natural numbers

==================================================

Problem #81:
Linear Search (Stop at Match): You have a list of product IDs. Search for ID 49. Use break to stop the loop immediately once found

==================================================

Problem #82:
Odd Number Filter: Print numbers 1 to 20, but use the continue keyword to skip all even numbers

==================================================

Problem #83:
Menu Selection: Create an infinite while loop (while True). Inside, ask for an order. If the user types "quit", use break to exit

==================================================

Problem #84:
Budget Guard: Keep adding expenses to a total_cost variable in a loop. If total_cost exceeds 500, print "Limit Reached" and break

==================================================

Problem #85:
Skip Restricted Items: Iterate through a list of items; if the item is "Restricted", use continue to avoid printing it

==================================================

Problem #86:
Inventory Checklist: Given a list of 5 grocery items, use a for loop to print each item with a "Stock Checked: " prefix

==================================================

Problem #87:
Character Verticalizer: Take a string like "PYTHON" and use a for loop to print each character on a separate line

==================================================

Problem #88:
Price Adjuster: You have a list of prices. Use a for loop to print each price after adding a 10% tax

==================================================

Problem #89:
Tuple Scanner: Create a tuple of high scores. Use a for loop to iterate through them and find if any score is above 100

==================================================

Problem #90:
Total Sales: Take a list of daily sales figures and use a for loop to calculate the final total of the week

==================================================

Problem #91:
Batch Numbers: Use for i in range(1, 101) to print every number from 1 to 100

==================================================

Problem #92:
Reverse Stock Check: Use the range() function with a negative step to print numbers from 100 down to 1

==================================================

Problem #93:
Even Batching: Use range(start, stop, step) to print all even numbers between 2 and 50

==================================================

Problem #94:
Step Calculator: Print every 5th number from 0 to 50 (e.g., 0, 5, 10...) using a step size in range()

==================================================

Problem #95:
Index-Based Loop: Use range(len(list_name)) to print each item's index and its value from a list of fruit

==================================================

Problem #96:
Factorial Machine: Use a for loop and the range() function to calculate the factorial (n!) of a number entered by the user

==================================================

Problem #97:
Loop Completion Alert: Use the optional else block with a for loop to print "All items processed" after the loop finishes naturally

==================================================

Problem #98:
Future Feature Placeholder: Create a loop to process "Advanced Data," but use the pass statement inside it so the code doesn't crash while you wait to write the logic later

==================================================

Problem #99:
Nested Condition Search: Search for a specific student in a list. If found, print "Student Found." If the loop finishes without finding them, use the loop's else block to print "Not Found"

==================================================

Problem #100:
Interactive Adder: Use a while loop to keep asking for numbers and adding them to a total until the user enters 0. Then print the final sum

==================================================

Problem #101:
Welcome System: Create a function greet_user() that takes a name and prints "Welcome [Name] to our platform!"

==================================================

Problem #102:
Rectangle Area: Write a function that takes length and width as parameters and returns the total area of a room

==================================================

Problem #103:
Default Health: Create a game function set_health() where the default health is 100 if the user doesn't provide a specific value

==================================================

Problem #104:
Fuel Cost: Write a function that takes distance and price_per_km to calculate the total cost of a trip

==================================================

Problem #105:
Single Line List Printer: Create a function that takes a list of grocery items and prints them all in a single line separated by spaces

==================================================

Problem #106:
Even/Odd Checker: Write a function that takes an integer and returns the string "Even" if the number is divisible by 2, otherwise returns "Odd"

==================================================

Problem #107:
Average Calculator: Create a function that takes marks for three subjects and returns their average

==================================================

Problem #108:
Currency Converter: Write a function to convert a given amount in USD to INR using a fixed conversion rate (e.g., 83)

==================================================

Problem #109:
Inventory Length: Create a function that takes any list (like a warehouse inventory) and prints its total length

==================================================

Problem #110:
Tax Calculator: Write a function that takes a bill_amount and a default tax_rate=0.18 to return the total price including tax

==================================================

Problem #111:
BMI Calculator: Create a function that calculates Body Mass Index (weight/height^2) and prints the result.
Temperature Converter: Write a function that converts Celsius to Fahrenheit and returns the value

==================================================

Problem #112:
Maximum Finder: Write a function that takes three numbers and returns the largest among them

==================================================

Problem #113:
Discount Applicator: Create a function that takes a price and a discount_percentage, then returns the final price after the discount.
Safe Division: Write a function that takes two numbers and returns their division result, but prints a warning and returns None if the second number is zero

==================================================

Problem #114:
Recursive Countdown: Write a recursive function that takes a number n and prints a countdown from n to 1

==================================================

Problem #115:
Natural Sum: Create a recursive function to find the sum of the first n natural numbers (e.g., if n=5, sum is 1+2+3+4+5)

==================================================

Problem #116:
Factorial Finder: Write a recursive function to calculate the factorial of a number

==================================================

Problem #117:
Recursive List Print: Write a function that uses recursion to print every item in a list one by one

==================================================

Problem #118:
Power Function: Create a recursive function to calculate a 
b
  (a raised to the power of b)

==================================================

Problem #119:
Voter Eligibility: Create a function that takes an age and prints "Eligible to Vote" if age is 18 or older, and "Not Eligible" otherwise

==================================================

Problem #120:
Bank Balance Check: Write a function that takes current_balance and withdrawal_amount. It should return True if the transaction is possible and False if the balance is too low

==================================================

Problem #121:
Search in List: Write a function that takes a list and a target item. It should return the index where the item is found or "Not Found"

==================================================

Problem #122:
Recursive Palindrome: Write a recursive function to check if a string (like "madam") is the same backward and forward

==================================================

Problem #123:
Character Verticalizer: Create a recursive function that takes a string and prints each character on a new line until the end of the string

==================================================

Problem #124:
Read Company Motto: Create a file named motto.txt. Write a Python program to open this file in read mode ('r') and print the entire motto to the console

==================================================

Problem #125:
Snapshot View: Open a large log file and use f.read(20) to read and print only the first 20 characters to get a quick preview

==================================================

Problem #126:
Line-by-Line Log Review: Use .readline() to read a file named server_logs.txt and print only the first two lines

==================================================

Problem #127:
Automatic Closure: Use the with syntax to open notes.txt and print its content. Verify that you don't need to call .close() manually

==================================================

Problem #128:
Default Mode Check: Open a file without specifying a mode and print its content. Prove that the default mode is 'r' (read)

==================================================

Problem #129:
Daily Journal: Create a program that opens diary.txt in write mode ('w') and writes "Today was a productive day." Note how it overwrites existing data

==================================================

Problem #130:
Guest Registry: Open a file guests.txt in append mode ('a') and add a new name "John Doe" to the end of the existing list

==================================================

Problem #131:
New Line Formatting: Write three separate sentences to tasks.txt, ensuring each sentence appears on a new line using the \n character

==================================================

Problem #132:
Exclusive Creation: Try to open backup.txt using the 'x' mode. If the file already exists, observe the error; otherwise, create it and write "Backup Created"

==================================================

Problem #133:
Dynamic User Input: Use input() to ask a user for their favorite quote and save that quote into a file called user_quotes.txt

==================================================

Problem #134:
Cleanup Operation: Import the os module and write a program to delete a temporary file named temp_cache.txt

==================================================

Problem #135:
Binary File Handling: Attempt to open an image file (photo.png) in binary read mode ('rb') and print the data type of the result

==================================================

Problem #136:
Safe File Removal: Write a program that asks for a filename from the user and then uses os.remove() to delete it

==================================================

Problem #137:
Mode Selection Logic: Open a file in 'r+' mode and write "UPDATED" at the very beginning of the file while keeping the rest of the text

==================================================

Problem #138:
Append and Read: Open a file in 'a+' mode. Append the text "End of File" and then explain why you cannot immediately read it without resetting the pointer

==================================================

Problem #139:
Keyword Search: Read practice.txt and check if the word "learning" exists within the data. Print "Found" or "Not Found"

==================================================

Problem #140:
Case-Sensitive Search: Search for the word "Python" in a file. If found, print the starting index where it first occurs using the .find() method

==================================================

Problem #141:
Line Tracker: Write a function check_for_line() that reads a file and tells the user exactly which line number a specific word (e.g., "Error") first appears on

==================================================

Problem #142:
Occurrence Counter: Create a program to count how many times the word "Data" appears throughout an entire text file

==================================================

Problem #143:
Validation System: Check if an email.txt file ends with the word "Regards" using the .read() string and .endswith() function

==================================================

Problem #144:
CSV Number Sum: A file stats.txt contains numbers separated by commas (e.g., 10, 20, 30). Read the file, split the data by the comma, and calculate the total sum

==================================================

Problem #145:
Even Number Filter: Read a file containing a list of ages separated by commas. Print only the even ages to the console

==================================================

Problem #146:
Word Replacement: Write a program to find every instance of the word "Java" in a file and replace it with "Python", then save the changes back to the file

==================================================

Problem #147:
Multi-Step Parsing: Read a file with names and marks. Split them into a list and find the student with the highest marks

==================================================

Problem #148:
Empty File Identifier: Write a program that reads a file and, if the result of .read() is an empty string, prints "The file is currently empty"

==================================================

Problem #149:
Student Identity: Create a Student class that stores a student's name. Create two different objects (s1, s2) for two friends and print their names to the console

==================================================

Problem #150:
Car Brand: Create a Car class with a color attribute. Instantiate an object for a "Blue" car and print its color

==================================================

Problem #151:
Product Catalog: Design a Product class. Create an object for a "Laptop" and another for a "Smartphone." Print the object types to show they belong to the same class

==================================================

Problem #152:
Furniture Blueprint: Create a Chair class. Use it to create three different chair objects. Explain why the class acts as a "blueprint" for these physical objects

==================================================

Problem #153:
Employee Data: Create an Employee class. Store the name of a manager in one object and a developer in another. Access their names using the dot (.) notation

==================================================

Problem #154:
Automatic Welcome: Create a class with an __init__ function that prints "Adding new member to the system..." every time a new object is created

==================================================

Problem #155:
Dynamic Profiles: Create a User class where the __init__ method takes name and age as parameters. Initialize two users with different data

==================================================

Problem #156:
Object Reference: In a class, use the print(self) statement inside the constructor. Create an object and compare the printed self address with the object's variable address

==================================================

Problem #157:
Multi-Data Entry: Create a Book class that initializes with a title, author, and price. Print all three details using a single object

==================================================

Problem #158:
Constructor Parameter Logic: Write a class for a Movie. Pass the title and rating during object creation and assign them to self.title and self.rating

==================================================

Problem #159:
Shared School Name: Create a Student class. Use a class attribute for the college_name (shared by everyone) and an instance attribute for the student's name

==================================================

Problem #160:
Company Directory: Create an Employee class where the company_name is a class attribute. Show how all 100 employees can share this one piece of data in memory

==================================================

Problem #161:
Attribute Priority: Create a class where both a class attribute and an instance attribute have the name status. Print the attribute for an object and explain why the instance value is shown (priority)

==================================================

Problem #162:
Global Brand: Design a Mobile class where brand = "Apple" is a class attribute. Access it directly using the class name (Mobile.brand) without creating an object

==================================================

Problem #163:
Memory Efficiency: Explain through a program why storing a "City" name as a class attribute is better for 1,000 objects than storing it as an instance attribute

==================================================

Problem #164:
Welcome Message: Create a Student class with a method called welcome(). It should print "Welcome [Name]!" using the self.name attribute

==================================================

Problem #165:
Average Marks: Create a class that takes a list of 3 subject marks. Add a method get_average() that calculates and prints the average score

==================================================

Problem #166:
Bank Transaction: Create an Account class with a balance. Add a debit(amount) method that subtracts money and a credit(amount) method that adds money

==================================================

Problem #167:
Balance Inquiry: Add a get_balance() method to your Account class that simply returns the current amount in the bank

==================================================

Problem #168:
Static Greeting: Use the @staticmethod decorator to create a header() method that prints a generic "System Information" message without using the self parameter

==================================================

Problem #169:
Car Start Logic (Abstraction): Create a Car class with a start() method. Inside, make it change clutch and accel to True. Show how the user only sees "Car Started" while the internal logic is hidden

==================================================

Problem #170:
Bank Security (Abstraction): Explain how a user withdraws money from an ATM using a withdraw() method without knowing the complex backend code that verifies the database

==================================================

Problem #171:
Data Capsule (Encapsulation): Create a class that combines a customer's ID, address, and purchase_history (data) along with a track_order() method (function) into a single unit

==================================================

Problem #172:
Attribute Modification: Create a Student object. Manually change the name attribute from "Tony Stark" to "Iron Man" and print the updated object data

==================================================

Problem #173:
Final System Check: Create a Library class that encapsulates book_list and a method total_books(). Instantiate it to show how data and functions are bundled together

==================================================

Problem #174:
Account Deactivation: Create a UserAccount class. Instantiate an object and then use the del keyword to delete the entire object from memory when the user closes their account

==================================================

Problem #175:
Secure Password: Create an Account class where the __password attribute is private. Attempt to print it from outside the class and observe the error

==================================================

Problem #176:
Internal Database Auth: Design a class with a private method __generate_token(). Create a public method login() that calls this private method internally to show how sensitive logic is hidden

==================================================

Problem #177:
Property Cleanup: Create a SmartDevice class. Use the del keyword to remove only a specific attribute, like temporary_cache, without deleting the whole object

==================================================

Problem #178:
Confidential Salary: Create an Employee class with a private attribute __salary. Write an internal method that uses this salary to calculate a bonus, showing that private data is accessible within the class

==================================================

Problem #179:
EV Factory (Single Inheritance): Create a base class Vehicle with a start() method. Create a derived class ElectricCar that inherits from Vehicle and adds a battery_level attribute

==================================================

Problem #180:
Tech Evolution (Multi-level Inheritance): Create a base class Phone, a derived class Smartphone, and a final derived class IPhone. Show how IPhone can access methods from both parent classes

==================================================

Problem #181:
Hybrid Device (Multiple Inheritance): Create two independent classes, Camera and MusicPlayer. Create a third class Smartphone that inherits from both, gaining features of both devices

==================================================

Problem #182:
Shared Features: Define a parent class Animal with an eat() method. Create a Dog class that inherits eat() so you don't have to rewrite the logic for every animal

==================================================

Problem #183:
Retail Hierarchy: Create a Product class. Create a Clothing class that inherits from it but adds specific attributes like size and fabric

==================================================

Problem #184:
Parent Constructor Call: Create a Manager class that inherits from Employee. Use the super() method in the Manager constructor to pass the name and age to the Employee constructor

==================================================

Problem #185:
Automatic Engine Start: In a Tesla class, use super().start() inside its own constructor so that the car automatically starts the base engine logic as soon as the object is created

==================================================

Problem #186:
Global Branding: Create a Mobile class with a class attribute brand_name = "Generic". Use a class method (@classmethod) to change the brand name for the entire class at once

==================================================

Problem #187:
Instance Counter: Use a class method to track how many total objects of a Student class have been created by incrementing a class-level variable

==================================================

Problem #188:
Data Reset: Create a class method that resets a class-level minimum_wage attribute, affecting every employee instance currently in the system

==================================================

Problem #189:
Live Invoice: Create a Bill class with amount and tax. Use the @property decorator to create a total_price method that automatically updates whenever the amount changes

==================================================

Problem #190:
Dynamic Greeting: Use @property to create a full_name attribute that combines first_name and last_name variables. Show how it reflects changes if either name is updated

==================================================

Problem #191:
Auto-Percentage: Create a Student class where the percentage is a property. If a teacher updates a student’s marks, the percentage should update automatically when accessed

==================================================

Problem #192:
Currency Converter: Create a class with a price_in_inr attribute. Use @property to provide a price_in_usd that calculates the conversion on the fly based on the current exchange rate

==================================================

Problem #193:
Stock Alert: Use a property decorator to return a string "Out of Stock" or "In Stock" based on a quantity integer attribute

==================================================

Problem #194:
Cart Addition: Create an Order class. Overload the + operator (__add__) so that adding two order objects returns the total combined price

==================================================

Problem #195:
Budget Comparison: Overload the > operator (__gt__) in a Project class so that you can compare two projects to see which one has a higher budget

==================================================

Problem #196:
Custom Subtraction: Create a Wallet class and overload the - operator (__sub__) to calculate the remaining balance when one wallet "pays" another

==================================================

Problem #197:
Multi-Type Plus: Demonstrate polymorphism by showing how the + operator behaves differently when used with two integers versus two strings or two lists

==================================================

Problem #198:
Complex Number Display: Create a Complex class. Overload the + operator to add the real parts and imaginary parts of two numbers separately, and use a method to display the result as 1i + 3j

==================================================

Problem #199:
Inventory Management: Create a dictionary to store product names as keys and their stock levels as values. Write a loop that asks the user for a product name and quantity sold, updates the stock, and uses a conditional to print a "Restock" warning if stock falls below 5

==================================================

Problem #200:
User Authentication: Store usernames and passwords in a dictionary. Create a while loop that allows 3 login attempts. Use string slicing to ensure the password entered doesn't contain the username within it

==================================================

Problem #201:
Unique Visitor Tracker: Take a list of visitor names (some duplicates). Use a Set to find unique visitors. Print the list of unique names in reverse alphabetical order using list methods

==================================================

Problem #202:
Grade Analyzer: Input a string of marks separated by commas (e.g., "85,90,78"). Use .split() and type casting to convert them to a list of integers. Calculate the average and assign a grade (A, B, C, D) using if-elif-else

==================================================

Problem #203:
Multiplication Table Generator: Ask for a number n. Use a for loop and the range() function to print its table up to 10, but use continue to skip the result if it is a multiple of 5

==================================================

Problem #204:
Palindrome List Checker: Write a program that takes a list of strings. Use a loop to check each string and print True if the string is a palindrome (same forward and backward)

==================================================

Problem #205:
Email Domain Counter: Given a list of email addresses, use a dictionary to count how many emails belong to "gmail.com", "yahoo.com", and "outlook.com" using string methods like .endswith()

==================================================

Problem #206:
Budget Tracker: Start with an initial balance. Continually ask the user for expenses in a loop until they type "done". Use if statements to prevent the balance from going negative

==================================================

Problem #207:
Voter Registration: Create a nested list containing [Name, Age] pairs. Use a loop to create a new list containing only the names of people who are eligible to vote (Age ≥ 18)

==================================================

Problem #208:
Sentence Statistics: Input a paragraph. Use string functions to count the total number of words, the number of spaces, and the frequency of a specific word entered by the user

==================================================

Problem #209:
Recursive Fibonacci: Write a recursive function to find the n-th number in the Fibonacci sequence (0,1,1,2,3,5,…)

==================================================

Problem #210:
Recursive Power: Create a function power(a, b) that calculates a^b using recursion instead of the ** operator

==================================================

Problem #211:
Safe Calculator: Write a function calc(a, b, op) where op is a string ("add", "sub", "mul", "div"). Use conditional logic to handle operations and return a "Division by Zero" error if b=0 and the operator is "div"

==================================================

Problem #212:
Recursive List Sum: Write a recursive function that takes a list of numbers and returns their total sum without using the sum() function or loops

==================================================

Problem #213:
Default Argument Billing: Create a function generate_bill(item_price, tax_rate=0.18). It should return the total price. Call it with and without the tax_rate to show default behavior

==================================================

Problem #214:
Prime Number Checker: Write a function that takes an integer and returns True if it is prime, using a loop and the modulo operator

==================================================

Problem #215:
Recursive String Reversal: Create a recursive function that takes a string and returns it reversed

==================================================

Problem #216:
Variable Argument Sum: Create a function that accepts a variable number of integers (as a list) and returns only the sum of the even numbers

==================================================

Problem #217:
Currency Converter Function: Write a function that converts USD to INR using a fixed rate. Use it inside a loop to convert a list of prices

==================================================

Problem #218:
Recursive Factorial: Implement a function to calculate the factorial of n using recursion, ensuring you have a proper base case

==================================================

Problem #219:
Log File Searcher: Create a function that reads a file server_log.txt line-by-line and prints the line number where the word "ERROR" first appears

==================================================

Problem #220:
Data Backup: Write a program that reads all data from source.txt and writes it into backup.txt using the with syntax

==================================================

Problem #221:
CSV Summarizer: Read a file numbers.txt where integers are separated by commas. Use .split() to convert them to a list, calculate their sum, and append the sum to the end of the same file

==================================================

Problem #222:
File Word Replacer: Write a program to find every occurrence of the word "Python" in a file and replace it with "Java", then save the updated content back to the same file

==================================================

Problem #223:
Secure Delete: Use the os module to check if temp.txt exists; if it does, print "Deleting..." and remove it

==================================================

Problem #224:
Line Counter: Write a program that opens a file and counts how many total lines it contains without using .read() (to save memory)

==================================================

Problem #225:
Dictionary to File: Store a dictionary of student grades. Write a program that iterates through the dictionary and saves each "Name : Grade" pair on a new line in grades.txt

==================================================

Problem #226:
Binary Image Copy: Open a binary file photo.jpg in rb mode and write its content into a new file copy.jpg in wb mode

==================================================

Problem #227:
Filtered File Read: Read a file and print only the lines that start with a capital letter using string methods

==================================================

Problem #228:
Interactive Journal: Use a while loop to take user input for daily notes. Save each note to journal.txt in append mode, adding a timestamp (as a string) before each note

==================================================

Problem #229:
Bank Account System: Create an Account class with private attributes __account_no and __password. Add methods for debit() and credit() that update a public balance attribute

==================================================

Problem #230:
Vehicle Hierarchy: Create a base class Vehicle with a start() method. Create a child class Car that inherits from it and uses super().start() to extend the functionality

==================================================

Problem #231:
Multi-level Inheritance: Create a class Person, a child class Employee, and a grandchild class Manager. Show how a Manager object can access the name attribute from the Person class

==================================================

Problem #232:
Operator Overloading (Math): Create a Complex class representing a+bi. Overload the + operator using the __add__ dunder function to add two complex objects

==================================================

Problem #233:
Property Decorator (Payroll): In an Employee class, use the @property decorator to create a salary_after_tax attribute that automatically calculates based on a base_salary attribute

==================================================

Problem #234:
Static Method Utility: In a MathUtils class, create a static method that calculates the average of any list of numbers provided as an argument

==================================================

Problem #235:
Class Method Tracker: Use a class method (@classmethod) to track how many total instances of a Student class have been created using a class attribute

==================================================

Problem #236:
Polymorphism in Shapes: Create classes Circle and Square with their own area() methods. Write a function that takes any shape object and calls its area() method to demonstrate polymorphism

==================================================

Problem #237:
Private Method Logic: Design a class DatabaseConnector with a private method __connect(). Use a public method get_data() that calls the private connection method internally

==================================================

Problem #238:
Comparison Overloading: In a Product class, overload the > operator (__gt__) to compare two products based on their price attribute

==================================================

Problem #239:
Library Management System: Create a Book class. Store book objects in a list. Write a program that allows a user to "add" a book, "search" for a book by title (string search), and "delete" a book from the list using the del keyword

==================================================

Problem #240:
Automated Grade Report: Read student names and marks from input.txt. For each student, create a Student object. Use a method to calculate their grade. Finally, save a summary report to report.txt

==================================================

Problem #241:
Smart Home System: Create a Device base class. Create Light and Fan subclasses. Use a loop to store multiple devices in a set (to ensure no duplicate IDs). Iterate through the set to turn all devices "ON" using a common method

==================================================

Problem #242:
Encapsulated Wallet: Create a Wallet class with a private __balance. Use a property decorator for the balance to ensure no one can set a negative balance. Overload the + operator so that adding two wallets combines their money into a new wallet

==================================================

Problem #243:
Recursive Directory Size (Conceptual): Write a recursive function that takes a list of file sizes (where some items might be sub-lists of sizes) and calculates the total size

==================================================

Problem #244:
E-Commerce Cart: Create an Item class with name and price. Create a Cart class that holds a list of Item objects. Add a method to calculate the total cost after applying a 10% discount if the total is over 1000

==================================================

Problem #245:
Password Manager: Write a class that saves encrypted passwords (just strings reversed) to a file. Add a method to "recover" the password by reading the file and reversing the string back

==================================================

Problem #246:
Student Attendance: Read a list of names from attendance.txt. Use a Set to find students who were present more than once (duplicates). Use a Dictionary to store each student's name and their total attendance count

==================================================

Problem #247:
Inheritance & Super: Create a Rectangle class with area(). Create a Square child class that inherits from Rectangle but only takes one side in its __init__ and uses super() to pass it as both length and width

==================================================

Problem #248:
The Final System: Build a class Course that has a name and a list of Student objects. The class should have a method to save the entire class roster and their average marks to a file named after the course
.

==================================================

"""

# ── 2. Parse problems ──────────────────────────────────────────────
def parse_problems(text):
    """Split raw text into a dict  {number: full_problem_text}"""
    pattern = re.compile(r'Problem #(\d+):\n(.*?)(?=Problem #\d+:|$)', re.DOTALL)
    problems = {}
    for match in pattern.finditer(text):
        num  = int(match.group(1))
        body = match.group(2).strip()
        # Remove trailing separator lines
        body = re.sub(r'\n=+\s*$', '', body).strip()
        problems[num] = body
    return problems

# ── 3. Create output folder & files ───────────────────────────────
def create_files(problems, output_dir="python_problems"):
    os.makedirs(output_dir, exist_ok=True)

    header = (
        "# ============================================================\n"
        "# Python Course – Problem Set\n"
        "# ============================================================\n"
        "#\n"
    )

    for num, body in sorted(problems.items()):
        filename = os.path.join(output_dir, f"problem_{num:03d}.py")

        # Wrap every line of the problem as a comment
        commented_body = "\n".join(f"# {line}" for line in body.splitlines())

        content = (
            f"{header}"
            f"# Problem #{num}:\n"
            f"#\n"
            f"{commented_body}\n"
            f"#\n"
            f"# ============================================================\n\n"
            f"# ✏️  Write your solution below:\n\n"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

    return output_dir

# ── 4. Run ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    problems = parse_problems(RAW_TEXT)
    out = create_files(problems)
    total = len(problems)
    print(f"✅  Done! {total} files created inside the '{out}/' folder.")
    print(f"    Files are named: problem_001.py  →  problem_{total:03d}.py")