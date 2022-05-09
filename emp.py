class Employee:
    def GetEmployee(self):
        print("Enter Employee Details : ")
        self.__id = input("Id : ")
        self.__name = input("Name : ")
        self.__lastname = input("Surname : ")
        self.__salary = int(input("Salary : "))
        self.__grade = input("Designation Level (I,II,III) : ")

    def PutEmployee(self):
        print(self.__id, self.__name, self.__salary)

    def Perks(self):
        self.PutEmployee()
        if (self.__grade == '1'):
            da = self.__salary * 40 / 100;
            hra = self.__salary * 16 / 100;
        elif (self.__grade == '2'):
            da = self.__salary * 50 / 100;
            hra = self.__salary * 18 / 100;
        elif (self.__grade == '3'):
            da = self.__salary * 60 / 100;
            hra = self.__salary * 20 / 100;

        ns = self.__salary + da + hra
        print(da, hra, ns)

    def Search(self, id):
        if id == self.__id:
            return True
        else:
            return False

    def search(self, grade):
        if grade == self.__grade:
            return True
        else:
            return False

    def tsearch(self, lastname):
        if lastname == self.__lastname:
            return True
        else:
            return False

n = int(input("Enter Total No. of Employees?"))
L = list()
for i in range(n):
    E = Employee()
    E.GetEmployee()
    L.append(E)
id = input("Enter Id U Want to Search?")

found = False
for e in L:
    found = e.Search(id)

    if (found):
        e.Perks()
        break
if (not found):
    print("Employee Not Exist")

lastname = input("Employee does not exist")
found = False
for e in L:
    found = e.tsearch(lastname)

    if (found):
        e.Perks()
        break
if (not found):
    print("Employee does not exist")

grade =input ("enter designation")

found = False
for e in L:
    found = e.search(grade)

    if (found):
        e.Perks()
        break
if (not found):
    print("Employee does not exist")
