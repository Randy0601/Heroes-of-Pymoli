
# Heroes Of Pymoli Data Analysis

Observation Trend:

1) Of the total 576 players, 780 purchases were made. Players in the age range of 20-24 accounts for 46.81% of the total spending. Players in age range of 35-39 spend more on average per item, and players in age range of 40+ are least likely to make a purchase.

2) Item "Oathbreaker, Last Hope of the Breaking Storm" is the top seller both in count and profitability. On the contrary, even though "Pursuit, Cudgel of Necromancy" is one of the top 5 seller, profitability on it is low, as the unit price is only set at $1.02.

3) The gender purchase analysis display purchase weightage by gender. It is only analyzing gender purchase as if each purchase is an individual count. However, since players can make multiple purchases, the more accurate representation should be looking at the gender weightage of unique players. Which should 83.59% of the players are male.


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
csvfile = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchasedf = pd.read_csv(csvfile)
purchasedf.head()

# Count total number of players
    #purchasedf["SN"].value_counts()
purchase_count = purchasedf["SN"].nunique()
purchase_unique = pd.DataFrame({"Total Players":[purchase_count]})
purchase_unique



# Purchasing Analysis (Total)
    # Number of Unique Items
    # Average Purchase Price
    # Total Number of Purchases
    # Total Revenue
purchase_item = purchasedf["Item ID"].nunique()
Average_purchase = purchasedf["Price"].mean()
Total_purchase = purchasedf["Item Name"].count()
Total_Revenue = purchasedf["Price"].sum()
# Create Table
Purchasing_Analysis = pd.DataFrame({"Number of Unique Items":[purchase_item],
                                   "Average Purchase Price":[Average_purchase],
                                   "Total Number of Purchases":[Total_purchase],
                                   "Total Revenue":[Total_Revenue]})
# Set Format
Purchasing_Analysis = Purchasing_Analysis.round(2)
Purchasing_Analysis["Average Purchase Price"] = Purchasing_Analysis["Average Purchase Price"].map("${:,.2f}".format)
Purchasing_Analysis["Number of Unique Items"] = Purchasing_Analysis["Number of Unique Items"].map("{:,}".format)
Purchasing_Analysis["Total Revenue"] = Purchasing_Analysis["Total Revenue"].map("${:,.2f}".format)
Purchasing_Analysis = Purchasing_Analysis.loc[:,["Number of Unique Items", "Average Purchase Price",
                                      "Total Number of Purchases", "Total Revenue"]]
Purchasing_Analysis


# Gender Demographics
    # Percentage and Count of Male Players
    # Percentage and Count of Female Players
    # Percentage and Count of Other / Non-Disclosed
    
# Count "Gender" and get percentage of "Gender"
gender_group = purchasedf["Gender"].value_counts()
gender_percent = gender_group / purchase_count * 100
# below formula will change the percentage calculation to be divide by total player count instead of unique player count.
# gender_percent = gender_group / Total_purchase * 100

# Set format
gender_percent = gender_percent.round(2)

#Create Table
gender_table = pd.DataFrame({"Total Count": gender_group,
                               "Percentage of Players": gender_percent})
gender_table
    
# # Count "Gender" and get percentage of "Gender"
# gender_group = purchasedf["Gender"].value_counts()
# gender_percent = gender_group / purchase_count

# # Set format to show %
# gender_percent = gender_percent.round(5)

# #Create Table
# gender_table = pd.DataFrame({"Total Count": gender_group,
#                                "Percentage of Players": gender_percent.map("{:,.2%}".format)})
# gender_table


The percentage of Players is calculated by unique count. which cause total percentage to be above 100%. Another way to look at the data would be to divide by total count instead of unique count.

# Purchasing Analysis (Gender)
# The below each broken by gender
    # Purchase Count
    # Average Purchase Price
    # Total Purchase Value
    # Average Purchase Total per Person by Gender
#Group data by Gender
gender_group = purchasedf.groupby("Gender")

# Calculate count, average, total of data
gender_count = gender_group["Item ID"].count()
gender_average = gender_group["Price"].mean()
gender_total = gender_group["Price"].sum()
average_per_person = gender_total / gender_count

# Create data table
gender_purchase_table = pd.DataFrame({"Purchase Count": gender_count,
                                     "Average Purchase Price": gender_average,
                                     "Total Purchase Value": gender_total,
                                     "Average Purchase Total per Person": average_per_person})

# Format data 
gender_purchase_table = gender_purchase_table.round(2)
gender_purchase_table["Average Purchase Price"] = gender_purchase_table["Average Purchase Price"].map("${:,.2f}".format)
gender_purchase_table["Total Purchase Value"] = gender_purchase_table["Total Purchase Value"].map("${:,.2f}".format)
gender_purchase_table["Average Purchase Total per Person"] = gender_purchase_table["Average Purchase Total per Person"].map("${:,.2f}".format)
gender_purchase_table = gender_purchase_table.loc[:,["Purchase Count", "Average Purchase Price",
                                      "Total Purchase Value", "Average Purchase Total per Person"]]


gender_purchase_table

# Age Demographics
# Determine the age Min and Max
    # Create a bin range for the min and max
    # Create labels for your bin ranges
    # Cut the data using the bin and labels create
# Create bins for age range
age_bins = [0, 9.90, 14.90, 19.90, 24.9, 29.9, 34.90, 39.90, 9999999]
group_names = ["0-10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Use Cut to categorize players
purchasedf["Age Range"] = pd.cut(purchasedf["Age"], age_bins, labels=group_names)

# Calculate total by age range and percentage of players in each range
agerange_total = purchasedf["Age Range"].value_counts()
agerange_percent = agerange_total / purchase_count * 100

# Below formula will calculate percentage of total count in each bucket instead of by unquie players. Showing 100% total
# agerange_percent = agerange_total / Total_purchase * 100

# Creating dataframe and format to match with example solution
agerange_table = pd.DataFrame({"Total Count": agerange_total, "Percent of Players": agerange_percent})
agerange_table = agerange_table.sort_index()
agerange_table = agerange_table.round(2)

agerange_table

The percentage of Players is calculated by unique count. which cause total percentage to be above 100%. Another way to look at the data would be to divide by total count instead of unique count

# Calculate the total for the Age Ranges
# Calculate the Average for the Age Ranges Price
# Calculate Average Purchase Total per Person by Age Group

total_purchase = purchasedf.groupby(["Age Range"]).sum()["Price"]
average_purchase = total_purchase / agerange_total
average_per_person = total_purchase / agerange_total

# Create Dataframe for result
agerange_purchase = pd.DataFrame({"Purchase Count": agerange_total,
                                  "Average Purchase Price": average_purchase,
                                  "Total Purchase Value": total_purchase,
                                 "Average Purchase Total per Person": average_per_person})

# Format Table
agerange_purchase = agerange_purchase.round(2)
agerange_purchase["Average Purchase Price"] = agerange_purchase["Average Purchase Price"].map("${:,.2f}".format)
agerange_purchase["Average Purchase Total per Person"] = agerange_purchase["Average Purchase Total per Person"].map("${:,.2f}".format)
agerange_purchase["Total Purchase Value"] = agerange_purchase["Total Purchase Value"].map("${:,.2f}".format)

# Arrange Table columns
agerange_purchase = agerange_purchase.loc[:,["Purchase Count", "Average Purchase Price",
                                      "Total Purchase Value", "Average Purchase Total per Person"]]
agerange_purchase.sort_index(ascending=False)
agerange_purchase


# Top Spenders
  # Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  # SN
  # Purchase Count
  # Average Purchase Price
  # Total Purchase Value
player_total = purchasedf.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
player_average = purchasedf.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
player_count = purchasedf.groupby(["SN"]).count()["Price"].rename("Purchase Count")

# Create Table to store data
player_table = pd.DataFrame({"Total Purchase Value": player_total,
                          "Average Purchase Price": player_average,
                          "Purchase Count": player_count})
player_table = player_table.round(2)

# Re-organize column order
player_table = player_table.loc[:,["Purchase Count","Average Purchase Price", "Total Purchase Value"]]

# Create new table to keep format. Sort by Total Purchase Value and show top 5
new_player_table = player_table.sort_values("Total Purchase Value", ascending=False)
new_player_table["Average Purchase Price"] = new_player_table["Average Purchase Price"].map("${:,.2f}".format)
new_player_table["Total Purchase Value"] = new_player_table["Total Purchase Value"].map("${:,.2f}".format)
new_player_table.head(5)

# Most Popular Items
  #Identify the 5 most popular items by purchase count, then list (in a table):
  # Item ID
  # Item Name
  # Purchase Count
  # Item Price
  # Total Purchase Value

item_total = purchasedf.groupby(["Item ID","Item Name"]).sum()["Price"].rename("Total Purchase Value")
item_count = purchasedf.groupby(["Item ID","Item Name"]).count()["Price"].rename("Purchase Count")
item_price = item_total / item_count

# Create Table to store data and format
item_table = pd.DataFrame({"Purchase Count": item_count,
                           "Item Price": item_price,
                           "Total Purchase Value": item_total})

# Re-organize column order
item_table = item_table.loc[:,["Purchase Count","Item Price", "Total Purchase Value"]]
item_table["Item Price"] = item_table["Item Price"].map("${:,.2f}".format)
item_table["Total Purchase Value"] = item_table["Total Purchase Value"].map("${:,.2f}".format)

# Sort by Purchase Count and show top 5
item_table.sort_values("Purchase Count", ascending=False).head(5)


# Most Profitable Items
  # Identify the 5 most profitable items by total purchase value, then list (in a table):
  # Item ID
  # Item Name
  # Purchase Count
  # Item Price
  # Total Purchase Value
item_total = purchasedf.groupby(["Item ID","Item Name"]).sum()["Price"].rename("Total Purchase Value")
item_count = purchasedf.groupby(["Item ID","Item Name"]).count()["Price"].rename("Purchase Count")
item_price = item_total / item_count

# Create Table to store data and format
item_table = pd.DataFrame({"Purchase Count": item_count,
                           "Item Price": item_price,
                           "Total Purchase Value": item_total})

# Re-organize column order
item_table = item_table.loc[:,["Purchase Count","Item Price", "Total Purchase Value"]]
item_table["Item Price"] = item_table["Item Price"].map("${:,.2f}".format)

# Create new table to store format. Sort by Purchase Count and show top 5
new_item_table = item_table.sort_values("Total Purchase Value", ascending=False)
new_item_table["Total Purchase Value"] = new_item_table["Total Purchase Value"].map("${:,.2f}".format)
new_item_table.head(5)
