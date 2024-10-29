from Classes.Person import Person


class Student(Person):

    def __init__(self,
                 firstname="Иван",
                 surname="Иванов",
                 fathername="Иванович",
                 age=18,
                 gender=1,
                 income=3200,
                 outcome=1500,
                 areaOfStudies="нет информации"):
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.areaOfStudies = areaOfStudies
        print(f'Констурктор класса Student вызван')

    # Метод для получения направления обучения студента
    def getAreaOfStudies(self):
        return self.areaOfStudies

    # Метод для изменения направления обучения студента
    def setAreaOfStudies(self, areaOfStudies):
        self.areaOfStudies = areaOfStudies

    def getPlaceOfStudies(self):
        return f'Студент {self.getFullname()} учится в НГТУ!'

    def printInfo(self):
        super().printInfo()
        print("Area of studies:", self.getAreaOfStudies())
