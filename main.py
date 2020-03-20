#!/usr/bin/env python
# coding: utf-8

# # Pyber, A Ride-Sharing Company,  Data Analysis & Visualization

# #### Import dependencies

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# #### Load files and perform inital data analysis to become familiar with the datasets provided

# In[2]:


# File to Load (Remember to change these)
city_data_to_load = "./data/city_data.csv"
ride_data_to_load = "./data/ride_data.csv"

# Read the City and Ride Data

# potentially use city_data column for size bubble size reference
city_data = pd.read_csv(city_data_to_load)
ride_data = pd.read_csv(ride_data_to_load)

# Combine the data into a single dataset
cr_data = pd.merge(ride_data, city_data, on='city')

# Display the data table for preview
cr_data


# In[3]:


city_data.head()


# In[4]:


#checks:
#type(city_data)
#ride_data.head()

# city_data_df = city_data.groupby(['type', 'city'])

# calculate total fares for pie chart
#total_fares = cr_data['fare'].sum()


# In[5]:


# shape is (2375, 6)
cr_data.info()


# ## Bubble Plot of Ride Sharing Data

# ##### Obtain x and y coordinates, and prepare driver count by city by city type

# In[7]:


#slice by type, will have to make 3 df's for x, y, and s

# URBAN CALCULATION!
cr_urban_df = cr_data[cr_data['type']=='Urban']
# 2 df's - one for TOTAL COUNT OF RIDE ID  and   AVG FARE; group by city

#cr_urban_df.head()

#x_axis - within all urban data, groupby city and take the ride_id column
# the groupby puts it in alphabetical order
cr_urb_ridect_df = cr_urban_df.groupby('city').count()
cr_urb_ridect_df = cr_urb_ridect_df[['ride_id']]

# Y_axis
cr_urb_avgfare_df = cr_urban_df.groupby('city').mean()
cr_urb_avgfare_df = cr_urb_avgfare_df[['fare']]

# bubble size - referred back to the city data, pulled all urban data out and sorted it
urban_cities_df = city_data[city_data['type'] == 'Urban']
urban_cities_df = urban_cities_df.sort_values(by=["city"], ascending=True)
urban_cities_df = urban_cities_df[['driver_count']]


# cr_typenfare_df = cr_data.sort_values(by=["type", "fare"], ascending=False)
# cr_typenfare_df

####################################################################################

# # # Pie chart calculations # # # / dvided by all city types

#create data frame (sum the fares, total counts for last 2 pies) put into 1 data frame,

# use loops to make pie charts, put the percentages in pie chart, the piechart will automatically do itJ

# Calculate Total Fares Sums by City Type = / total count of all types
# target answers = Urb = 62.7%, sub = 30.5%, and rural = 6.8%
    # fares use sum
urb_fares = cr_urban_df['fare'].sum()


# Calculate Ride Percents = ride count by city type / total count of all rides
# target answers = Urb = 68.4%, sub = 26.3%, and rural = 5.3%
urb_totalrides = cr_urban_df['ride_id'].count


# Calculate Driver Percents = driver count by total count of all drivers
# target answers = Urb = 80.9%, sub = 16.5%, and rural = 2.6%

urb_driverpercent = urban_cities_df[['driver_count']].sum()


# In[8]:


urb_fares


# In[9]:


# Calculate total driver count for 3rd pie chart for reconciliation purposes
city_data['driver_count'].sum()

# check to before making pie chart
#print(2405/2973)


# In[10]:


# SUBURBAN
cr_suburban_df = cr_data[cr_data['type']=='Suburban']
#cr_suburban_df

#x_axis - within all suburban data, groupby city and take the ride_id column
# the groupby puts it in alphabetical order
cr_suburb_ridect_df = cr_suburban_df.groupby('city').count()
cr_suburb_ridect_df = cr_suburb_ridect_df[['ride_id']]

# Y_axis
cr_suburb_avgfare_df = cr_suburban_df.groupby('city').mean()
cr_suburb_avgfare_df = cr_suburb_avgfare_df[['fare']]

# bubble size - referred back to the city data, pulled all suburban data out and sorted it
suburban_cities_df = city_data[city_data['type'] == 'Suburban']
suburban_cities_df = suburban_cities_df.sort_values(by=["city"], ascending=True)
suburban_cities_df = suburban_cities_df[['driver_count']]

# Calculate Total Fares Sums by City Type = / total count of all types
# target answers = Urb = 62.7%, sub = 30.5%, and rural = 6.8%

suburb_fares = cr_suburban_df['fare'].sum()
suburb_fares


# Calculate Ride Percents = ride count by city type / total count of all rides
# target answers = Urb = 68.4%, sub = 26.3%, and rural = 5.3%

suburb_totalrides = cr_suburban_df['ride_id'].count

# Calculate Driver Percents = driver count by total count of all drivers
# target answers = Urb = 80.9%, sub = 16.5%, and rural = 2.6%
suburb_driverpercent = suburban_cities_df[['driver_count']].sum()


# In[11]:


#RURAL

# pull all rural data out into a seperate df
cr_rural_df = cr_data[cr_data['type']=='Rural']
#cr_rural_df

#x_axis - within all rural data, groupby city and take the ride_id column
# the groupby puts it in alphabetical order
cr_rural_ridect_df = cr_rural_df.groupby('city').count()
cr_rural_ridect_df = cr_rural_ridect_df[['ride_id']]

# Y_axis
cr_rural_avgfare_df = cr_rural_df.groupby('city').mean()
cr_rural_avgfare_df = cr_rural_avgfare_df[['fare']]

# bubble size - referred back to the rural data, pulled all urban data out and sorted it
rural_cities_df = city_data[city_data['type'] == 'Rural']
rural_cities_df = rural_cities_df.sort_values(by=["city"], ascending=True)
rural_cities_df = rural_cities_df[['driver_count']]


# Calculate Total Fares Sums by City Type = / total count of all types
# target answers = Urb = 62.7%, sub = 30.5%, and rural = 6.8%
rural_fares = cr_rural_df['fare'].sum()
rural_fares

# Calculate Ride Percents = ride count by city type / total count of all rides
# target answers = Urb = 68.4%, sub = 26.3%, and rural = 5.3%

rural_totalrides = cr_rural_df['ride_id'].count

# Calculate Driver Percents = driver count by total count of all drivers
# target answers = Urb = 80.9%, sub = 16.5%, and rural = 2.6%
rural_driverpercent = rural_cities_df[['driver_count']].sum()


# In[12]:


# Pulling data for data analysis piece.
cr_rural_df['fare'].describe()


# In[13]:


#cr_rural_ridect_df.head()


# In[14]:


#cr_rural_avgfare_df.head()


# In[16]:


# Preapre scatter plot

fig, ax = plt.subplots(figsize=(7,7))


urban = ax.scatter(cr_urb_ridect_df, cr_urb_avgfare_df, s=urban_cities_df*6, color='lightsalmon', label='Urban', edgecolors='black', alpha=0.75)
suburban = ax.scatter(cr_suburb_ridect_df, cr_suburb_avgfare_df, s=suburban_cities_df*6, color='skyblue',label='Suburban', edgecolors='black', alpha=0.75)
rural = ax.scatter(cr_rural_ridect_df, cr_rural_avgfare_df, s=rural_cities_df*7, color='gold', label='Rural', edgecolors='black', alpha=0.75)

# title and labels
plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)\nNote: Circle sizes correlate with driver count per city")
plt.ylabel("Average Fare($)")

# set and format the legend
lgnd = plt.legend(title='City Types', loc="best")
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]

#grid lines and show
plt.grid()
plt.show()
plt.savefig('./Pyber_RideShare_Scatter.png')


# ## Total Fares by City Type

# In[17]:


# Calculate Type Percents
# Build Pie Chart
# Save Figure

plt.figure(2, figsize=(6,8))
fare_city_list = [urb_fares, rural_fares, suburb_fares]
labels = ['Urban', 'Rural', 'Suburban']
colors = ['lightcoral', 'gold', 'lightskyblue']
explode = (0.1, 0, 0)  

for city in fare_city_list:
    plt.pie(fare_city_list, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", shadow=True, startangle=270)

plt.axis('equal')
plt.title('% of Total Fares by City Type')

plt.show()
plt.savefig('./Pyber_TotalFares_CityType.png')


# ## Total Rides by City Type

# In[18]:


# Calculate Ride Percents

plt.figure(3, figsize=(6,6))

rides_city_list = [urb_totalrides, rural_totalrides, suburb_totalrides]
labels = ['Urban', 'Rural', 'Suburban']
colors = ['lightcoral', 'gold', 'lightskyblue']
explode = (0.1, 0, 0)  

for ride in rides_city_list:
    plt.pie(fare_city_list, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", shadow=True, startangle=270)

plt.axis('equal')
plt.title('% of Total Rides by City Type')

plt.show()
plt.savefig('./Pyber_TotalRides_CityType.png')


# ## Total Drivers by City Type

# In[19]:


# Calculate Driver Percents

plt.figure(4, figsize=(6,6))

driver_count_list = [urb_driverpercent, rural_driverpercent, suburb_driverpercent]
labels = ['Urban', 'Rural', 'Suburban']
colors = ['lightcoral', 'gold', 'lightskyblue']
explode = (0.1, 0, 0)  

for driver in driver_count_list:
    plt.pie(driver_count_list, labels=labels, colors=colors, explode=explode, autopct="%1.1f%%", shadow=True, startangle=270)

plt.axis('equal')
plt.title('% of Total Drivers by City Type')

plt.show()
plt.savefig('./Pyber_TotalDrivers_CityType.png')


# # Data Analysis:
# 
# ### The data suggests the following:
# 
# ##### Pyber Ride Sharing Scatter plot:
# 
# Average fares in urban cities have a heavy concentration between the 20 to 30 USD range, and total number of rides have a volume between 20 to 30 rides. Whereas, suburban areas have variability in average fares between 25 to 37 USD. Majority of the total number of rides in suburban cities range between 12 to 20 rides. Whereas in rural areas, there is significantly higher variability in average fares ranging from 24 to 48 USD, and  limited number of total rides and drivers per city.  
# 
# ##### % of Total Fares and Rides by City Type Pie Charts:
# 
# Urban cities produced 62.7 percent of total fare revenue, and 68.4 percent of total rides of all three city types for the entire period. Suburban cities followed up with 30.5 percent of the fare revenues, and 26.3 percent of total rides. Rural cities only produced 6.8 percent of the remaining fare revenues, and 5.3 percent of the total rides. 
# 
# ##### % of Total Drivers by City Type Pie Charts:
# 
# Approximately 81 percent of Pyber drivers work in urban areas, where the average fares and volume of rides are significantly higher than the rural areas  (refer to % of Total Fares and Rides by City Type Pie Charts). Suburban areas have consistently fell into the middle ranges, bridging the gap between the urban and rural cities in terms of average fares, total volumes, and even in the type of cites Pyber drivers choose to work.
# 
# 

# In[ ]:




