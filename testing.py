import pandas as pd
# from os import listdir
# from os.path import isfile, join

#allData = pd.read_csv("./Sales_Data/Sales_December_2019.csv")
allData = pd.read_csv("alldata.csv")


# b) make dataframe to keep track of month, total sum of sales and number of sales
monthlySales = pd.DataFrame()
monthlySales['Month'] = [1,2,3,4,5,6,7,8,9,10,11,12]
monthlySales['Sum of Sales'] = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
monthlySales['Num of Sales'] = [0,0,0,0,0,0,0,0,0,0,0,0]
monthlySales.head()
for i in range(len(allData)):
    # check valid row
    cell = allData.iloc[i]['Order ID']
    if (type(cell) == type(float) or str(cell).isnumeric() == False):
        allData.at[i] = None
        continue
    # get month of row
    month = allData.iloc[i]['Order Date'].split('/')[0]
    # get $ for row (quantity * price)
    cash = float(allData.iloc[i]['Quantity Ordered']) * float(allData.iloc[i]['Price Each'])

    # print("Month: " + month)
    # print("Cash: " + str(cash))
    # print("Index: " + str(i))

    newCash = float(monthlySales.at[int(month)-1,'Sum of Sales']) + float(cash)

    # update monthlySales dataframe
    #monthlySales.loc[monthlySales['Month'] == month, ['Sum of Sales']] = newCash
    #monthlySales.loc[monthlySales['Month'] == month, ['Num of Sales']] = newCash
    monthlySales.at[int(month)-1,'Sum of Sales'] = float(monthlySales.at[int(month)-1,'Sum of Sales']) + float(cash)
    monthlySales.at[int(month)-1,'Num of Sales'] = int(monthlySales.at[int(month)-1,'Num of Sales']) + int(1)

    # monthlySales.loc[int(month)]['Sum of Sales'] = monthlySales.loc[int(month)]['Sum of Sales'] + cash
    # monthlySales.loc[int(month)]['Num of Sales'] = monthlySales.loc[int(month)]['Num of Sales'] + 1

print("finished")