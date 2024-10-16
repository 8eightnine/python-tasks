from Classes.Person import Person


class Worker(Person):

    def __init__(self,
                 firstname="Иван",
                 surname="Иванов",
                 fathername="Иванович",
                 age=25,
                 gender=1,
                 income=50000,
                 outcome=35700,
                 company="нет информации",
                 jobTitle="нет информации"):
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.company = company
        self.jobTitle = jobTitle

    # Метод для получения направления обучения студента
    def getCompany(self):
        return self.company

    def getJobTitle(self):
        return self.jobTitle

    # Метод для изменения направления обучения студента
    def setCompany(self, company):
        self.company = company

    def setJobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def GetJobInfo(self):
        return f'{self.getFullname()} работает в компании "{self.getCompany()}" на должности "{self.getJobTitle()}"'

    def printInfo(self):
        super().printInfo()
        print("Company:", self.getCompany())
        print("Job title:", self.getJobTitle())
