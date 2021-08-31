''' code the get the user input for the max allowable calories 
    OR exit keyword to end the code
    returns the list of selected foods with food value and callories selected by: 
    -Greedy Algorithm
    -Brute Force Algorithm
    -Dynamic Brute Force Algorithm
'''
from numpy import NaN
from Food import Food
from Greedy import greedy
from BruteForce import bruteForce,dynamicBForce

#return list of selected food based on the selected algorithm and constrain
def foodSelector(optimizationMethod,items,constrain,keyFun=None):    
    if optimizationMethod==greedy: 
        selectedFood,totalValue=optimizationMethod(items,constrain,keyFun)
    else:
        selectedFood,totalValue=optimizationMethod(items,constrain)
    print("selected algorithm: ",optimizationMethod.__name__)
    if selectedFood!=[]:
        print(f"Total value of your selected items: ",totalValue)
        for food in selectedFood:
            print(food)
    

#return list of Food class obj
def buildMenue(name,value,calories):
    menue=[]
    for i in range(len(value)):
        menue.append(Food(name[i],value[i],calories[i]))
    return menue    


# asks for the user input for the total allowable calories.
#if user type cancel, exit the program
if __name__=="__main__":
    print("Program is Running ...","\n")
    
    names=['wine', 'beer', 'pizza', 'burger', 'fries',
        'cola', 'apple', 'donut', 'cake']
    values=[89,90,95,100,90,79,50,10]
    calories=[123,154,258,354,365,150,95,195]
    foods=buildMenue(names,values,calories)
    
    min=min(calories)
    max=max(calories)
    
    #start with invalid constrain and only run the foodSelector if user provids valid data
    constrain=min-10
    
    #get user input for the allowable total calories or cancel to exit the code
    while True:
        try:            
            userInput=input(f"enter total allowale calories between {min} and {max}\
            \nor type exit to exit \n")
            print()
        except ValueError:
            print(f"please enter valid number!") 
        
        if userInput.lower()=="exit":                
            break
        elif userInput.isdigit() and int(userInput)<=max and int(userInput)>=min:
            constrain=int(userInput)
            break
        else: continue
           
    if(constrain!=min-10):
        print("----------------------RESULT---------------------------")
        print()
        foodSelector(greedy,foods,constrain,lambda x: 1/x.getCalories())
        print()
        foodSelector(bruteForce,foods,constrain)
        print()
        foodSelector(dynamicBForce,foods,constrain)
        
        
    
    
   
