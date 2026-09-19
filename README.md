PRACTICAL 1

# 📖 Key Concepts

## Object-Oriented Programming (OOP)
A programming approach that represents real-world entities as objects.

## Class
A blueprint used to create objects.

## Object
An instance of a class.

## Constructor (__init__)
Initializes object data automatically when an object is created.

## Instance Variable
Variables that belong to a particular object. Each object has its own copy.

## Instance Method
Methods that operate on object data using the `self` keyword.

## Encapsulation
Encapsulation means combining data and methods into a single class to improve security and organization.

## Library Management System
A software application that manages books, patrons, borrowing, and returning operations.

## Book Availability
A Boolean value (`True` or `False`) that indicates whether a book can be borrowed.

## Object Interaction
Objects communicate with each other by calling methods. For example, the `Library` object interacts with `Book` and `Patron` objects to perform borrowing and returning operations.

## Data Management
Lists are used to store books, patrons, and borrowed books, making it easy to manage records.

## Reusability
Reusability means writing code once and using it multiple times. The same `Report` class is reused to generate different reports without rewriting the logic.


PRACTICAL 2
# 📖 Key Concepts

## 1. Object-Oriented Programming (OOP)
Object-Oriented Programming (OOP) is a programming paradigm that organizes a program into objects. It helps in writing modular, reusable, and easy-to-maintain code by combining data and methods into a single unit called a class.

## 2. Class
A class is a blueprint or template for creating objects. It defines the attributes (data members) and methods (functions) that the objects created from it will have.

**Example:**
```python
class Report:
```

---

## 3. Object
An object is an instance of a class. Each object has its own data and can use the methods defined in the class.

**Example:**
```python
r1 = Report("Advanced Python Practical Report", "Mandar Joshi")
```

---

## 4. Constructor (__init__)
A constructor is a special method that is automatically called when an object is created. It initializes the object's attributes.

**Example:**
```python
def __init__(self, title, author):
```

---

## 5. Instance Variable
Instance variables are variables that belong to a specific object. Every object has its own copy of these variables.

**Examples:**
- title
- author
- contents

---

## 6. Instance Method
An instance method operates on a specific object and can access or modify its data using the `self` keyword.

**Example:**
```python
add_content()
display_report()
```

---

## 7. Class Variable
A class variable is shared among all objects of a class. If its value is changed, the change is reflected in every object.

**Example:**
```python
company_name = "ABC Technologies Pvt. Ltd."
```

---

## 8. Class Method
A class method works with class-level variables instead of object-level variables. It is defined using the `@classmethod` decorator and uses `cls` as its first parameter.

**Example:**
```python
@classmethod
def change_company(cls, new_company):
```

---

## 9. Static Method
A static method belongs to the class but does not access instance variables or class variables. It is mainly used for utility or helper functions.

**Example:**
```python
@staticmethod
def line():
```

---

## 10. Decorator
A decorator is a special function that modifies or extends the behavior of another function without changing its original code.

In this project, the decorator automatically prints the report header and footer.

**Example:**
```python
@report_decorator
```

---

## 11. Magic Methods
Magic methods are predefined special methods in Python that start and end with double underscores (`__`). They allow developers to customize the behavior of objects.

### __str__()
Returns a readable string representation of an object.

### __len__()
Returns the number of report sections.

---

## 12. Menu-Driven Program
A menu-driven program allows users to choose different operations by selecting options from a menu, making the application interactive and user-friendly.

---

## 13. Reusability
Reusability means writing code once and using it multiple times. In this project, the same `Report` class is reused to generate different reports without rewriting the logic.

---

## 14. Encapsulation
Encapsulation is the process of combining data and methods into a single class. It protects the data and improves code organization.

---

## 15. Benefits of this Project

- Demonstrates advanced Python programming concepts.
- Improves understanding of Object-Oriented Programming.
- Shows practical use of Decorators and Magic Methods.
- Encourages code reusability and modular programming.
- Provides an interactive menu-driven application.
- Generates well-formatted reports automatically.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
2. nth Fibonacci Number

This program finds the number at position n in the series. For example, if n = 10, the answer is 55.

3. Input from the User

The input() function takes a value from the keyboard. Since it returns text, int() is used to convert it into a number.

Example:

python
n = int(input("Enter the value of n: "))
4. Conditional Statements (if - elif - else)

Used to handle different cases:

If n is 0, the answer is 0.
If n is 1, the answer is 1.
Otherwise, the program calculates the answer using a loop.
5. Iterative Approach (Loop)

Instead of calling a function again and again (recursion), this program uses a for loop. It keeps only the last two numbers and moves forward step by step.

Example:

python
for i in range(2, n + 1):
    c = a + b
    a = b
    b = c
6. Variables Used
a : the previous number
b : the current number
c : the next number (a + b)
7. Why is it "Efficient"?
Approach	Time Taken	Extra Memory
Simple Recursion	Very slow (grows exponentially)	Uses call stack
Loop (this program)	O(n)	O(1)

Time Complexity O(n): the loop runs about n times. Space Complexity O(1): only three variables are used, no matter how big n is.

8. Sample Output
Enter the value of n: 10
Fibonacci number is: 55
9. Benefits of this Project
Teaches how to replace slow recursion with a fast loop.
Introduces time and space complexity in a simple way.
Uses very little memory.

PRACTICAL 5

📖 Key Concepts
1. Subsequence

A subsequence is formed by picking characters from a string in the same order, but they do not need to be next to each other.

Example: "ACE" is a subsequence of "ABCDE".

2. Longest Common Subsequence (LCS)

LCS is the longest subsequence that appears in both strings.

Example:

String 1: AGGTAB
String 2: GXTXAYB
LCS: GTAB (length 4)
3. Dynamic Programming (DP)

Dynamic Programming solves a big problem by breaking it into small problems, solving each one only once, and storing the answers so they are not calculated again.

4. DP Table

A 2D list (table) where dp[i][j] stores the LCS length of the first i characters of string X and the first j characters of string Y.

Example:

python
dp = [[0] * (n + 1) for _ in range(m + 1)]

The extra row and column (of zeros) represent an empty string.

5. Filling the Table

For every pair of characters:

If the characters match: take the diagonal value and add 1.
If they do not match: take the larger of the top cell and the left cell.
python
if X[i - 1] == Y[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
6. Backtracking

The table only gives the length. To get the actual LCS string, the program starts from the bottom-right cell and moves back:

Characters match: add the character and move diagonally.
Otherwise: move towards the larger neighbouring cell (up or left).

Because we move from the end to the start, the result is reversed at the end.

7. Function Returning Two Values

The lcs() function returns both the length and the actual sequence.

python
return dp[m][n], lcs_string
8. Time and Space Complexity
Time: O(m × n), where m and n are the lengths of the two strings.
Space: O(m × n) for the DP table.
9. Sample Output
Enter first string: AGGTAB
Enter second string: GXTXAYB

Length of LCS: 4
Longest Common Subsequence: GTAB
10. Benefits of this Project
Shows a classic Dynamic Programming problem.
Teaches how to use a 2D table and backtracking.
Used in real life, for example in file comparison tools such as diff.

PRACTICAL 6

📖 Key Concepts
1. Knapsack Problem

You have a bag with limited capacity and several items, each with a weight and a profit. The goal is to choose items so that the total profit is maximum without crossing the bag's capacity.

2. 0/1 Knapsack

"0/1" means each item is either taken completely (1) or not taken at all (0). You cannot take half an item.

3. Input Data Used
python
weights  = [3, 2, 4, 5, 1]
profits  = [50, 40, 70, 80, 10]
capacity = 7
4. Dynamic Programming (DP)

DP stores answers of smaller problems in a table so they are not calculated again.

5. DP Table

dp[i][w] stores the maximum profit using the first i items with a bag capacity of w.

python
dp = [[0] * (capacity + 1) for _ in range(n + 1)]
6. Two Choices for Every Item

For each item, the program decides between:

Exclude the item: keep the answer from the previous row.
Include the item: add its profit and use the remaining capacity.
python
dp[i][w] = max(
    dp[i-1][w],
    profits[i-1] + dp[i-1][w - weights[i-1]]
)

If the item is heavier than the current capacity, it cannot be included, so the previous answer is copied.

7. Finding the Selected Items (Backtracking)

The program moves from the last item to the first. If dp[i][w] is different from dp[i-1][w], that item was included, so:

its index is saved, and
its weight is subtracted from the remaining capacity.

The list is reversed at the end to show items in their original order.

8. Indexing Note

Python lists start from index 0, so item i in the table is weights[i-1] in the list.

9. Time and Space Complexity
Time: O(n × capacity)
Space: O(n × capacity)
10. Sample Output
Maximum Profit: 120
Items in Knapsack: [0, 2]

Items 0 and 2 have weights 3 + 4 = 7 (full bag) and profits 50 + 70 = 120.

11. Benefits of this Project
Teaches a very common DP problem asked in exams and interviews.
Shows how to make "take or skip" decisions.
Helps in understanding resource allocation problems.

PRACTICAL 7

📖 Key Concepts
1. File Handling

File handling means reading data from a file and writing data to a file using a program.

2. Opening a File (open())

The open() function opens a file. The second argument is the mode:

Mode	Meaning
"r"	Read the file
"w"	Write to the file (creates it, or overwrites if it exists)
3. with Statement

The with statement opens a file and automatically closes it when the block ends, even if an error occurs. This is the recommended way to work with files.

Example:

python
with open("input.txt", "r") as file:
    lines = file.readlines()
4. readlines()

Reads the whole file and returns a list, where each element is one line of the file (including the newline character \n).

5. Counting Lines

Since lines is a list, len(lines) gives the total number of lines.

python
line_count = len(lines)
6. List Slicing

Slicing takes a part of a list. Negative indexing counts from the end.

lines[-3:] means "the last three lines".

python
last_three_lines = lines[-3:]
7. strip()

Removes extra spaces and the newline character from the start and end of a line, so the output prints neatly.

8. writelines()

Writes a list of lines into a file in one go.

python
with open("output.txt", "w") as file:
    file.writelines(last_three_lines)
9. What the Program Does
Reads all lines from input.txt.
Prints the total number of lines.
Prints the last three lines.
Saves those three lines into output.txt.
10. Before Running

Create an input.txt file in the same folder as pract7.py. Otherwise Python will show a FileNotFoundError.

11. Benefits of this Project
Teaches reading from and writing to files.
Shows how list slicing works in a practical way.
Introduces safe file handling using with.
