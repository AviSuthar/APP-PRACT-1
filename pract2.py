# ==========================================================
# Experiment No. 2
# Dynamic Report Generator using Decorators, Class Methods,
# Static Methods and Magic Methods (Menu Driven)
# ==========================================================

# Decorator Function
def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("=" * 60)

        func(*args, **kwargs)

        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)
    return wrapper


# Report Class
class Report:

    company_name = "ABC Technologies Pvt. Ltd."

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self, text):
        self.contents.append(text)

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    @staticmethod
    def line():
        print("-" * 60)

    def __str__(self):
        return f"Report Title : {self.title}\nAuthor : {self.author}"

    def __len__(self):
        return len(self.contents)

    @report_decorator
    def display_report(self):

        print("Company :", Report.company_name)
        print(self)

        Report.line()

        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")

        Report.line()
        print("Total Sections :", len(self))


# ---------------- Report 1 ----------------
r1 = Report("Advanced Python Practical Report", "Mandar Joshi")

r1.add_content("Completed Experiment No. 2 successfully.")
r1.add_content("Implemented Decorators, Class Methods, Static Methods and Magic Methods.")
r1.add_content("Learned Object-Oriented Programming concepts.")
r1.add_content("Report prepared by Mandar Joshi.")


# ---------------- Report 2 ----------------
r2 = Report("Employee Performance Report", "Mandar Joshi")

r2.add_content("Attendance : 98%")
r2.add_content("Projects Completed : 8")
r2.add_content("Rating : Excellent")
r2.add_content("Department : Computer Engineering")
r2.add_content("Recommendation : Promotion Approved")


# ---------------- Report 3 ----------------
r3 = Report("Student Result Report", "Mandar Joshi")

r3.add_content("Student Name : Rahul")
r3.add_content("Roll No : 101")
r3.add_content("CGPA : 9.25")
r3.add_content("Status : Pass with Distinction")
r3.add_content("Result : Pass")


# ================= MENU =================

while True:

    print("\n")
    print("=" * 60)
    print("DYNAMIC REPORT GENERATOR".center(60))
    print("=" * 60)
    print("1. Display Practical Report")
    print("2. Display Employee Report")
    print("3. Display Student Report")
    print("4. Change Company Name")
    print("5. Exit")
    print("=" * 60)

    choice = input("Enter your choice: ")

    if choice == "1":
        r1.display_report()

    elif choice == "2":
        r2.display_report()

    elif choice == "3":
        r3.display_report()

    elif choice == "4":
        new_company = input("Enter New Company Name: ")
        Report.change_company(new_company)
        print("Company name changed successfully!")

    elif choice == "5":
        print("\nThank You for Using Dynamic Report Generator.")
        break

    else:
        print("Invalid Choice! Please try again.")