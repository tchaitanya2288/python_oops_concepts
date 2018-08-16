class country:
    def __init__(self,name,population,area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name,self.population,self.area))

countries = [country('india','999','1200'),
             country('USA','200','2200'),
             country('india','240','1900')]
countries.append(country('Russia','800','1400'))

print(countries)

