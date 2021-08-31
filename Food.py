
#implementation of food class 
class Food(object):
    def __init__(self,name,value,calories):
        self.name=name
        self.value=value
        self.calories=calories
    
    def getName(self):
        return str(self.name)
    
    def getValue(self):
        return self.value

    def getCalories(self):
        return self.calories
    
    # def density(self):
    #     return self.value/self.calories
    
    def __str__(self):
        return self.name+": <"+str(self.value)\
            +' , '+str(self.calories)+">"

