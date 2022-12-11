import datetime

class Person:
    def __init__(self, name, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex

    def getBirthyear(self):
        now = datetime.datetime.now()
        return now.year - self.age

# returns the individuals birthyear

    def setMood(self, happy=False):
        if happy:
            self.mood ='happy'
            print (f'{self.name.split()[0]}: I am in a good mood!')
        else:
            self.mood = 'stressed'
            print(f'{self.name.split()[0]}: I have too much work to do..')
#returns the individuals mood based on boolean

class Student(Person):
    def __init__(self, tired=True, areas=['study'], **kwargs):
        super(Student, self).__init__(**kwargs)
        self.areas = areas

    def setEnergy(self, tired=True):
        if tired:
            self.energy = 'tired'
            print(f'{self.name.split()[0]}: I need more sleep...')
        else:
            self.energy = 'energized'
            print(f'{self.name.split()[0]}: I can do this!')
        return tired
 #returns the energy level of the student 
       
    def getAreas(self):
        print (f'{self.name.split()[0]}: I am studying {self.areas}.')
            
#prints out the areas of study 

    def __repr__(self):
        return f'[Person: {self.name}, {self.age}, {self.sex}]'
#overrides the printable string of the Person class

    def setStudy(self, intensity=True):
        if intensity:
            self.intensity = 'low'
            print(f'{self.name.split()[0]}: I am procrastinating, please help me!')
        else:
            self.intensity = 'high'
            print(f'{self.name.split()[0]}: I am getting things done.')
#the intensity of the study session


class BaStudent(Student):
    def __init__(self, seniority = 0, Enrollmentyear=None, **kwargs):
        super(BaStudent, self).__init__(**kwargs)

    def getSeniority(self):
        return self.seniority 
    
    def setSeniority(self, seniority):
        self.seniority = seniority
        print(f'{self.name.split()[0]} is currently {self.seniority} into their schooling.')


    def getEnrollmentyear(self):
        now = datetime.datetime.now()
        Enrollmentyear = now.year - self.seniority
        print(f'{self.name.split()[0]} is {self.seniority} years into their schooling, started in {int(self.getEnrollmentyear())}')
        return Enrollmentyear
#determines the enrollment year of the student based on their seniority
def main():
        ssl = BaStudent(
            name='Simone S. Lewis',
            age=23, sex="female",
            seniority=4,
            areas='linguistics and TESL'
            )
        ssl.setMood(happy=False)
        ssl.setEnergy(tired=False)
        ssl.setStudy(intensity=False)
        ssl.getAreas()
        ssl.getSeniority()
        ssl.getEnrollmentyear()
        
#returns those values 
if __name__ == '__main__':
    main()


