from Classes.Person import Person


class Preschooler(Person):

    def __init__(self,
                 firstname="Иван",
                 surname="Иванов",
                 fathername="Иванович",
                 age=20,
                 gender=0,
                 income=0,
                 outcome=0,
                 group=1):
        # В классе "Дошкольник" есть доп. поле "Группа в дет. саду"
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.group = group
        print(f'Констурктор класса Preschooler вызван')

    # Метод для получения группы дошкольника
    def getGroup(self):
        return self.group

    def getGroupStr(self):
        return f'{self.firstname} сейчас посещает {self.getGroup()} группу в дет. саде'

    # Метод для изменения группы дошкольника
    def setGroup(self, group):
        self.group = group

    def printInfo(self):
        super().printInfo()
        print("Kindergarden group:", self.getGroup())
