class Person():

    def __init__(self,
                 firstname="Ivan",
                 surname="Ivanov",
                 fathername="Ivanovich",
                 age=20,
                 gender=-1,
                 income=0,
                 outcome=0):
        self.firstname = firstname
        self.surname = surname
        self.fathername = fathername
        self.age = age
        self.gender = gender
        self.income = income
        self.outcome = outcome

    # Метод для получения полного имени человека
    def getFullname(self):
        return (self.surname + " " + self.firstname + " " + self.fathername)

    # Метод для получения возраста человека
    def getAge(self):
        return self.age

    # Метод для получения дохода человека
    def getIncome(self):
        return self.income

    # Метод для получения дохода человека в строковом виде
    def getIncomeStr(self):
        return str(self.income) + "rub."

    # Метод для изменения значения дохода человека
    def setIncome(self, income):
        self.income = income

    # Метод для получения расхода человека
    def getOutcome(self):
        return self.outcome

    # Метод для изменения значения расхода человека
    def setOutcome(self, outcome):
        self.outcome = outcome

    # Метод для получения пола человека в строковом виде
    def getGender(self):
        if self.gender == 0:
            return "Male"
        elif self.gender == 1:
            return "Female"
        else:
            return "Unknown"

    # Метод для вывода полной информации о человеке
    def printInfo(self):
        print("Full name:", self.getFullname(), "\nAge:",
              self.getAge(), "\nGender:", self.getGender(), "\nIncome:",
              self.getIncome(), "\nOutcome:", self.getOutcome())
