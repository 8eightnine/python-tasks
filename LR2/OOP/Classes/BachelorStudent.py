from Classes.Student import Student


class BachelorStudent(Student):

    def __init__(self,
                 firstname="Иван",
                 surname="Иванов",
                 fathername="Иванович",
                 age=18,
                 gender=1,
                 income=3200,
                 outcome=1500,
                 areaOfStudies="нет информации",
                 year_of_completion=2026):
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.areaOfStudies = areaOfStudies
        self.year_of_completion = year_of_completion
        print(f'Констурктор класса BachelorStudent вызван')

    # Метод для получения направления обучения студента
    def getAreaOfStudies(self):
        return self.areaOfStudies

    # Метод для изменения направления обучения студента
    def setAreaOfStudies(self, areaOfStudies):
        self.areaOfStudies = areaOfStudies

    def printInfo(self):
        super().printInfo()
        print("Area of studies:", self.getAreaOfStudies())
