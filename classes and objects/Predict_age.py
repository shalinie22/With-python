from datetime import date 

class CalculateAge:

    def __init__(self,name, country,date_of_birth) :
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age(self):

        current_year = date.today()
        age = current_year.year - self.date_of_birth.year 
        if current_year.year < self.date_of_birth.year:

            age-=1

        return age
    
person1 = CalculateAge("Sha","India",date(1998,9,22))

print(person1.name)
print(person1.country)
print(person1.age())