from Classes.Person import Person


class Scholar(Person):

    def __init__(self,
                 firstname="Иван",
                 surname="Иванов",
                 fathername="Иванович",
                 age=7,
                 gender=1,
                 income=0,
                 outcome=0,
                 grade=1):
        # В классе "Школьник" есть доп. поле "Класс (например, 1, 5, 9)"
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.grade = grade

    # Метод для получения класса школьника
    def getGrade(self):
        return self.grade

    # Метод для получения класса школьника в строковом виде
    def getGradeStr(self):
        return f'{self.firstname} сейчас учится в {self.grade} классе'

    # Метод для изменения класса школьника
    def setGrade(self, grade):
        self.grade = grade

    def printInfo(self):
        super().printInfo()
        print("School grade:", self.getGrade())
