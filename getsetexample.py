class Person:
    def __init__(self, firstName, lastName):
        self.firstname = firstName
        self.lastname = lastName


    def getName(self):
        return self.firstname + " " + self.lastname



class Employee(Person):

    def setWorkDetail(self,job1,job2):
        self.job1 = job1
        self.job2 = job2

    def getWorkDetail(self):
        return self.job2 + ', ' + self.job1


emp1 = Employee('Mladen', 'Solomun')
emp1.setWorkDetail('Software Engineer', 'C++ programmer')

print('Name: ' + emp1.getName())
print('Work: ' + emp1.getWorkDetail())

emp2 = Employee('John', 'Askew')
emp2.setWorkDetail('Sound Engineer', 'Musical acoustics')

print('Name: ' + emp2.getName())
print('Work: ' + emp2.getWorkDetail())