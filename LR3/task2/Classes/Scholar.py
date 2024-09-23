from Classes.Person import Person


class Scholar(Person):

    def __init__(self,
                 firstname,
                 surname,
                 fathername,
                 age,
                 gender,
                 income,
                 outcome,
                 grade=1):
        # В классе "Школьник" есть доп. поле "Класс (например, 1, 5, 9)"
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.grade = grade

    def __init__(self, grade=1):
        # Если был передан только класс, заполняем экземпляр стандартными значениями
        super().__init__()
        self.grade = grade

    # Метод для получения класса школьника
    def getGrade(self):
        return self.grade

    # Метод для изменения класса школьника
    def setGrade(self, grade):
        self.grade = grade

    def printInfo(self):
        super().printInfo()
        print("School grade:", self.getGrade())
