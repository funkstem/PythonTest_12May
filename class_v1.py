class school:
    no=0
    def __init__(self,name,number) -> None:
        self.name=name
        self.number=number
        school.no+=1

    def description(self):
        print("%s has %d students" %(self.name,self.number))


s1=school("HWA",1000)
s2=school("Chong",2000)

print(school.no)
s1.description()