from Classes.Person import Person


class Student(Person):

    def __init__(self,
                 firstname,
                 surname,
                 fathername,
                 age,
                 gender,
                 income,
                 outcome,
                 areaOfStudies="Unknown"):
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.areaOfStudies = areaOfStudies

    def __init__(self, areaOfStudies=1):
        # Если было передано только направление, заполняем экземпляр стандартными значениями
        super().__init__()
        self.areaOfStudies = areaOfStudies

    # Метод для получения направления обучения студента
    def getAreaOfStudies(self):
        return self.areaOfStudies

    # Метод для изменения направления обучения студента
    def setAreaOfStudies(self, areaOfStudies):
        self.areaOfStudies = areaOfStudies

    def printInfo(self):
        super().printInfo()
        print("Area of studies:", self.getAreaOfStudies())
