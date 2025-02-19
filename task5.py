class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self):
        amount = float(input("Enter raise amount: PHP"))
        if amount > 0:
            self.salary += amount
            print(f"{self.name} received a raise of PHP{amount:.2f}. New salary: PHP{self.salary:.2f}")
        else:
            print("Invalid raise amount.")

    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: PHP{self.salary:.2f}")


employee1 = Employee("John Rophi Bautista", "QA DEV", 50000)

employee1.display_employee()
employee1.give_raise()
employee1.display_employee()
