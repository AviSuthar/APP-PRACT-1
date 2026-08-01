PRACTICAL !

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
