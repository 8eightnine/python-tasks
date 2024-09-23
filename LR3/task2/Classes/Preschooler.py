from Classes.Person import Person


class Preschooler(Person):

    def __init__(self,
                 firstname,
                 surname,
                 fathername,
                 age,
                 gender,
                 income,
                 outcome,
                 group=0):
        # В классе "Дошкольник" есть доп. поле "Группа в дет. саду"
        super().__init__(firstname, surname, fathername, age, gender, income,
                         outcome)
        # Инициализируем поля класса методом наследуемого класса
        self.group = group

    def __init__(self, group=0):
        # Если была передана только группа, заполняем экземпляр стандартными значениями
        super().__init__()
        self.group = group

    # Метод для получения группы дошкольника
    def getGroup(self):
        return self.group

    # Метод для изменения группы дошкольника
    def setGroup(self, group):
        self.group = group

    def printInfo(self):
        super().printInfo()
        print("Kindergarden group:", self.getGroup())
