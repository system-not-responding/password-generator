# # for loop
#     # a for loop is used to repeat a specific block of code a known number of times.
#         # ex:
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     #  do something to each item
#     print(fruit)
#     # this returns the items in the list
#     print(fruit + " Pie")
#     # this adds the string "Pie" after the fruit
# print(fruits)
# # this adds the list fruits to the end of the for loop since removing the indentation closed it 


# # PLAYGROUND
# vegetables = ["Spinach", "Banana", "Potato"]

# for vegetable in vegetables:
#     print(vegetable + " Pie")



# alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# vowels = ["A", "E", "I", "O", "U", "Y"]

# alphabet_len = len(alphabet)
# vowels_len = len(vowels)

# print(f"There are {alphabet_len} letters in the alphabet.\n")
# for letter in alphabet:
    
#     print(letter)

# print(f"\nThere are {vowels_len} vowels in the alphabet.")
# for vowel in vowels:
#     print(vowel)

# objective: write a program that gets the average height of the students
# average = sum_of_num_of_items / num_of_items

# first i need to add all items in the list together


# # Input a Python list of student heights
# student_heights = ["151", "145", "179"]
# # student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
  
# # Write your code below this row 👇

# students_heights_len = len(student_heights)

# for student_height_sum in student_heights:
#   print(st)
# print(students_heights_len)


# write a code that gets the highest number using for loops

realized_pnl = ["-350", "125", "420", "-69"]
for n in range(0, len(realized_pnl)):
    realized_pnl[n] = int(realized_pnl[n])
highest_pnl = 0

for i in realized_pnl:
    if i > highest_pnl:
        highest_pnl = i

print(f"Your highest pnl today was: {highest_pnl}")

# for loop with range
# for number in range(1, 10, 2):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
    print(total)