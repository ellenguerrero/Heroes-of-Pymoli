
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


#purchase_data.head()
#purchase_data.dtypes
#purchase_data is a df

#SN counts as a player because unique value

    
#totalPlayers=[]
totalPlayers = len(purchase_data["SN"].unique())

summary_table=pd.DataFrame(totalPlayers,index=[0],columns=["Total Players"])

summary_table


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


#purchase_data.head()
#purchase_date.dtypes
#Purchase ID      int64
#SN              object
#Age              int64
#Gender          object
#Item ID          int64
#Item Name       object
#Price          float64
#dtype: object

AveragePrice=purchase_data["Price"].mean()
#AveragePrice
#help(purchase_data.append)

Total_Revenue=purchase_data["Price"].sum()
#Total_Revenue

uniqueItems = len(purchase_data["Item ID"].value_counts())
Avg_Price = round(AveragePrice,2)
numPurchases = len(purchase_data["Purchase ID"].value_counts())
Total_Revenue

#format
fAvg_Price="$"+str(Avg_Price)
fTotal_Revenue="$"+str(Total_Revenue)

#List of values
# new df
newList=pd.DataFrame({'Number of Unique Items':uniqueItems, 
                      'Average Price':fAvg_Price, 
                      'Number of Purchases':numPurchases, 
                      'Total Revenue':fTotal_Revenue}, index=[0])
newList



#newdf=purchase_data[uniqueItems,Avg_Price,numPurchases,Total_Revenue]


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[67]:


#variables for values
#purchase_data.head()
gendf=purchase_data.drop_duplicates(["SN"])
GenderCounts=gendf["Gender"].value_counts()

Male=GenderCounts.iloc[0]
Female=GenderCounts.iloc[1]
Other=GenderCounts.iloc[2]

GenTotals=[Male, Female, Other]
TotalGen=GenderCounts.sum()

Percent=GenTotals/TotalGen*100

genderdf=pd.DataFrame({"Total Count":GenderCounts,
                      "Percentage of Players":Percent})

genderdf.round(2)


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[166]:


purchase_data.head()
PurchaseCount = len(purchase_data["Purchase ID"].value_counts())   
PurchaseCount=purchase_data["Gender"].value_counts()

Maleprice=purchase_data.loc[(purchase_data["Gender"]=="Male")]
Maleavg=Maleprice["Price"].mean()
Maleavg

Feprice=purchase_data.loc[(purchase_data["Gender"]=="Female")]
Feavg=Feprice["Price"].mean()
Feavg

Othprice=purchase_data.loc[(purchase_data["Gender"]=="Other / Non-Disclosed")]
Othavg=Othprice["Price"].mean()
Othavg

AvgPurPrice=[Maleavg, Feavg, Othavg]
AvgPurPrice

MaleTot=Maleprice["Price"].sum()
MaleTot

FeTot=Feprice["Price"].sum()
FeTot

OthTot=Othprice["Price"].sum()
OthTot

TotalPricesAll=[MaleTot, FeTot, OthTot]

AvMalePer=(Maleprice["Price"].sum())/GenderCounts[0]
AvFemalePer=(Feprice["Price"].sum())/GenderCounts[1]
AvOthPer=(Othprice["Price"].sum())/GenderCounts[2]

AvPers=[AvMalePer, AvFemalePer, AvOthPer]

PurchAnalysis=pd.DataFrame({"Purchase Count":PurchaseCount,
                            "Average Purchase Price":AvgPurPrice,
                            "Total Purchase Value":TotalPricesAll,
                           "Average Total Purchase Per Person":AvPers})

round_this=PurchAnalysis.sort_index(ascending=True)
round_this.round(2)


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[295]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]


#age_group=purchase_data.groupby("Age Range")


#print(age_group)

#TotalAges=[]
#TotalAges = len(purchase_data["Age Range"].value_counts())   
#TotalAges=purchase_data[""].value_counts()

#TotalAges
#AgeDemo=pd.DataFrame({"Total Count":totalAge})

#"Percentage of Players", "Total Count"

#AgeDemo


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 
