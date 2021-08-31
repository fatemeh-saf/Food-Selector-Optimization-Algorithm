#implementation of greedy algorithm

def greedy(items,constrain,keyFunction):
    # reversly sort the items based on the keyFunc
    sortedItems=sorted(items,key=keyFunction,reverse=True)      
    result = []
    totalValue,totalCost=0,0
    # take from the sorted items as long as cost<=constrains
    # for i in range(len(sortedItems)):
    #     if(totalCost+sortedItems[i].getCalories())<=constrain:
    #         result.append(sortedItems[i])
    #         totalCost+=sortedItems[i].getCalories()
    #         totalValue+=sortedItems[i].getValue()
    for item in sortedItems:
        if(totalCost+item.getCalories())<=constrain:
            result.append(item)
            totalCost+=item.getCalories()
            totalValue+=item.getValue()
    return (result,totalValue)



    
    



    
