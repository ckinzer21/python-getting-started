from employee_object import Employee #from (file name) import (class name)

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees')
        for i in self.employees:
            print(i.fname, i.lname, i.salary, '\n')
            print('--------------------------')

    def pay_employee(self):
        print('Paying Employees')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: {i.calc_paycheck():,.2f}')
            print('--------------------------')

def main():
    my_company = Company()

    employee1 = Employee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    employee2 = Employee('Foo', 'Bar', 25000)
    my_company.add_employee(employee2)
    employee3 = Employee('John', 'Doe', 60000)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employee()

main()