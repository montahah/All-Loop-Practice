print("For LOOP PRACTICE")
print("=" * 20)

#Level1
#example1: loop through a list
# fruits = ["potato", "tomato", "cabbage", "carrot"]
fruits = ["apple", "banana", "orange", "grape"]
for i in fruits:
    print(f"    I like {i}")

print("\n")
#example 2: Loop Through a string
word = "    python"
for character in word:
    print(f"    Character: {character}")

print("\n")
#example 3: using range() for numbers
for number in range(5):
    print(f"    Number: {number}")

print("\n")
# example 4: Range with start and stop
for i in range(1, 6):
    print(f"    Count: {i}")

print("\n")
#example 5: Range with Step
for i in range(0, 12, 2):
    print(f"    Even Numbers: {i}")

print("\n")
#example 6: Range with Step
for i in range(0, 12, 1):
    print(f"    Odd Numbers: {i}")

print("\n")
#example 7: Using enumerate() to get index and value
colors = ["red", "green", "blue", "yellow"]
for index, color in enumerate(colors):
    print(f"    position {index}: {color}")

print("\n")
# Example 8: Loop with calculations
for num in range(1, 6):
    square = num ** 2
    print(f"    {num}² = {square}")

print("\n")
#example 9: building a list inside loop
even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
print(f"    Even numbers: {even_numbers}")

print("\n")
#example 10: building a list inside loop
odd_numbers = []
for i in range(1, 10):
    if i % 2 == 1:
        odd_numbers.append(i)
print(f"    Odd numbers: {odd_numbers}")

print("\n")
#practice 11: Nested Loop
for i in range(1, 4):
    row = ""
    for j in range(1,5):
        result = i * j
        # row += f"{i}x{j} = {result:2d} "
        # row += f"{result:2d} "
        row += f"{result} "
        print(f"    {row}")

print("\n")
#practice 12: Loop through dictionary
student_grades = {"Karim": 85, "Rahim": 90, "Akash": 78}
for name, grade in student_grades.items():
    print(f"    {name}: {grade}")

print("\n   Grade Calculator")
#practice 13: Grade Calculator
student_scores = [87, 90, 84, 69, 76, 85]
total = 0
count = 0
for score in student_scores:
    total += score
    count += 1
    print(f"   Score {count}: {score}")

average = total / count
print(f"   Total: {total}")
print(f"   Average: {average:.1f}")

print("\n")
#Find Longest number
inword = "Banana"
for word in inword:
    if len(word) > len(inword):
        inword = word

print(f"   Word Count: '{inword}' ({len(inword)} letters)")

