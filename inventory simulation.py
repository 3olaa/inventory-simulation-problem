from random import choices

#Deterministic inputs
sellingPrice = 450  
storageCost = 50       #carrying cost holding cost
compensationCost = 100 #shortage cost
#List to store profit
profitList = []
AvgProfit1 = 0
AvgProfit2 = 0

#Probabilistic input 
Demand = [0,1,2,3,4]
Probability = [0.2, 0.4, 0.2, 0.1, 0.1]
x = choices(Demand, Probability, k = 500)

#Function
for order in range(1,3):
    AvailablePCs = 0
    for week in range(0,500):
        AvailablePCs += order
        if x[week] < AvailablePCs:  #if demand less than available PCs
            soldPCs = x[week]  
            AvailablePCs -= x[week]
            loss = AvailablePCs * storageCost
            
        elif x[week] > AvailablePCs:
            soldPCs = AvailablePCs
            AvailablePCs = 0
            loss = (x[week] - soldPCs) * compensationCost
            
        else:
            soldPCs = x[week]
            AvailablePCs = 0
            loss = 0
        profit = (soldPCs * sellingPrice) - loss
        
        if profit > 0:
            profitList.append(profit)
    if order == 1:
        AvgProfit1 = sum(profitList) / 500
        profitList.clear()
        
    else:
        AvgProfit2 = sum(profitList) / 500


print("The average profit of 500 weeks if the shop owner ordered 1 PC per week is $", AvgProfit1, "\n")
print("The average profit of 500 weeks if the shop owner ordered 2 PCs per week is $", AvgProfit2, "\n")

if AvgProfit1 > AvgProfit2:
    print("Therefore, the right decision is to order 1 PC per week")
elif AvgProfit1 < AvgProfit2:
    print("Therefore, the right decision is to order 2 PCs per week")
