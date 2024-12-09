from Classes.Student import Student


class MastersStudent(Student):

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
        print(f'Констурктор класса MasterStudent вызван')

    def getPlaceOfStudies(self):
        return f'Студент {self.getFullname()} уже получил диплом бакалавра в {self.year_of_completion} и теперь учится в магистратуре НГТУ'
