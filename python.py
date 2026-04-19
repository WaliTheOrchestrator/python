class Student:
    def __init__(self, name, phy, chem, bio):
        self.name=name
        self.phy_marks=phy
        self.chem_marks=chem
        self.bio_marks=bio
    
    def average(self):
        avg=(self.phy_marks + self.chem_marks + self.bio_marks) / 3
        print("Average marks of the student is:", avg)
s1=Student("Waleed Khan", 98, 99, 100)
s1.average()