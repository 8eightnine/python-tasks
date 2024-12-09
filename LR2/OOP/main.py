from Classes.Person import Person
from Classes.Preschooler import Preschooler
from Classes.Scholar import Scholar
from Classes.Student import Student
from Classes.BachelorStudent import BachelorStudent
from Classes.MastersStudent import MastersStudent
from Classes.Worker import Worker

print('Тест 1: Создание экземпляра класса c заданными полями')
p2 = Preschooler(firstname='Арья', surname='Башинов', age=19, gender=1)
p2.printInfo()
print('------------')

print('Тест 2: Вызов собственных методов классов-наследников ')
p31 = Preschooler()
print(p31.getGroupStr())
p32 = Scholar()
print(p32.getGradeStr())
p33 = Student()
print(f'Студент {p33.getFullname()} изучает "{p33.getAreaOfStudies()}"')
p34 = Worker()
print(p34.GetJobInfo())
print('------------')

print('Тест 3: переопределение метода класса в наследнике')
p4 = Student("Engineering")
print(p4.getPlaceOfStudies())
p44 = BachelorStudent()
print(p44.getPlaceOfStudies())
p444 = MastersStudent()
print(p444.getPlaceOfStudies())
print('------------')

print('Тест 4: вывод информации о месте работы')
p5 = Worker(company='2GIS', jobTitle='Software Engineer')
p5.printInfo()
print(p5.GetJobInfo())
print('------------')

print('Тест 5: Смена информации в экземепляре класса')
p6 = Student()
print(p6.getAreaOfStudies())
p6.setAreaOfStudies("Прикладная информатика")
print(p6.getAreaOfStudies())
print('------------')

print('Тест 6: Смена значений заработка и затрат + вывод на экран')
p1 = Person()
p1.setIncome(1000)
p1.setOutcome(700)

print(
    f'{p1.getFullname()} зарабатывает {p1.getIncomeStr()} и тратит при этом {p1.getOutcomeStr()}'
)