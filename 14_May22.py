

class human:
    nohuman=0
    def __init__(self,name,height):
        self.name=name
        self.height=height
        human.nohuman+=1

    def description(self):
        print("%s's height is %d" %(self.name,self.height))


h1=human("Owen",60)
h2=human("Henry",80)
h3=human("David",80)

print(human.nohuman)
h3.description()