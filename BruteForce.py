# implementation of Brute force algorithm to optimize the selection from a list that meets the given constrains

def bruteForce(items,constrain):
    if items==[] or constrain==0:
        result=([],0)
    elif items[0].getCalories()>constrain:
        result=bruteForce(items[1:],constrain)
    else:
        nextItem=items[0]
        #check right and left branches and keep track of selected items,value:
        withItem,withValue=bruteForce(items[1:],constrain-nextItem.getCalories())
        withValue+=nextItem.getValue()
        withoutItem,withoutValue=bruteForce(items[1:],constrain)
        if withValue>withoutValue:
            result=(withItem+[nextItem],withValue)
        else:
            result=(withoutItem,withoutValue)
    return result


# implementation of dynamic brute force to optimize the run time for big items size 
def dynamicBForce(items,constrain,memo={}):
    #memo[(len(items),availCost)] :  
    # key:item remained in the list,available cost
    # if the same sub-problem has been explored before, use the result
    #otherwise find the result 
    if (len(items),constrain) in memo: 
        result=memo[(len(items),constrain)]
    elif items==[] or constrain==0:
        result=([],0)
    elif items[0].getCalories()>constrain:
        result=dynamicBForce(items[1:],constrain,memo)
    else:
        nextItem=items[0]
        #left brach:
        withItem,withValue=dynamicBForce(items[1:],constrain-
                                nextItem.getCalories(),memo)
        withValue+=nextItem.getValue()
        #right branch 
        withoutItem,withoutValue=dynamicBForce(items[1:],constrain,memo)

        if withValue>withoutValue:
            result=(withItem+[nextItem],withValue)            
        else:
            result=(withoutItem,withoutValue)
        memo[(len(items),constrain)]=result
    return result
            

    


        
















