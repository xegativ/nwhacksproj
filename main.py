#from django.db import models
"""
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
"""

class User():
    def __init__(self, firstName, lastName, userName):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName 


class Closet():
    # Closet per user; contains list of clothes
    def __init__(self, closet_name, desc="", cl_lst=[]):
        self.cl_lst = cl_lst 
    
    def addTop(self, name, desc="", colour="#ffffff", sleeves=True, clean=True):
        self.cl_lst.append(Top(name, desc, colour, sleeves, clean))

    def addBottom(self, name, desc="", colour="#ffffff", clean=True):
        self.cl_lst.append(Bottom(name, desc, colour, clean))

    def addShoes(self, name, desc="", colour="#ffffff", clean=True):
        self.cl_lst.append(Shoes(name, desc, colour, clean))

class Clothing():
    def __init__(self, name, desc="", colour="#ffffff", clean=True):
        self.name = name
        self.desc = desc
        self.colour = colour
        self.clean = clean

class Top(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", sleeves=True, clean=True):
        super().__init__(name, desc, colour, clean)
        self.sleeves = sleeves

class Bottom(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", clean=True):
        super().__init__(name, desc, colour, clean)

class Shoes(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", clean=True):
        super().__init__(name, desc, colour, clean)
        

def main():
    return 0

if __name__ == "__main__":
    main()