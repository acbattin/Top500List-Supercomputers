#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Scraping and Graphing with Python
Andie Battin
@author: andersonbattin

Created Feb 2023
Use the BeautifulSoup screen-scraper library and the link  
(https://top500.org/lists/top500/2021/11/) to modify and read the TOP500 sites
and create a .csv file of all 500 supercomputers.
"""

#Import needed libraries for reading / parsing Web pages, and graphing library
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# display and set working/data directory
os.chdir('/Users/andersonbattin/Desktop/Python')
pages = range(1,6)
rows = []
# Get data for each page on the website, page span should equal range span
for page in pages:

  page = requests.get("https://www.top500.org/lists/top500/list/2021/11/?page="
                      +str(page))
  soup = BeautifulSoup(page.content, 'html.parser')
  # Find list tags
  listitems = soup.find_all('li')
  # Find every computer record by the tr tags
  for record in soup.findAll('tr'):

    computers=[]  #Blank list to store row data

    for data in record.findAll('td'):
      # Create complete rows
      computers.append(data.text.replace('\n', ''))
      # Append all rows to list
    rows.append(computers)
# Filter blank rows
rows = list(filter(None, rows)) 

# Create dataframe to hold all data
df = pd.DataFrame(data = rows,columns = ['Rank','System','Cores',
                                         'Rmax (PFlop/s)','Rpeak (PFlop/s)',
                                         'Power (kW)'])

# Clean the unwanted characters from the data frame for numeric data items
df['Cores'] = df['Cores'].replace(',','',regex=True) #get rid of commas
df['Rmax (PFlop/s)'] = df['Rmax (PFlop/s)'].replace(',','',regex=True)
df['Rpeak (PFlop/s)'] = df['Rpeak (PFlop/s)'].replace(',','',regex=True)
df['Power (kW)'] = df['Power (kW)'].replace(',','',regex=True)
# Finalization - Create and read .csv file for top 500 supercomputers
df.to_csv(r'lablist.csv', index = False)
df = pd.read_csv('lablist.csv', na_filter=True)
# Confirm proper formatting changes
print('Summary Stats for "TOP500" Supercomputers as of November, 2021')
print('Using newly created .csv file:')
print(df.describe().round(1))


'''
Import the data. See here that the data being imported is the .csv file I coded
coded & saved for Part 2A of this lab (Mod 4, Lab 2). In Part 2A, I installed 
and used specialized libraries such as BeautifulSoup to scrape information from 
the web, specifically from the pages containing the TOP500 List Report from 
November 2021, and created a .csv file containing the records for the top 500 
supercomputers. The variables present in my .csv file are 'Rank', 'Cores', 
'Rmax (PFLOPs/s)', 'Rpeak (PFLOPs/s)', and 'Power (kW)'

'''
# Read in Super Computer csv file from previous assignment, load into
# a Pandas DataFrame
df = pd.read_csv('lablist.csv', na_filter=True)

# Dtypes of variables for reference
print(df.dtypes) 
# Find summary statistics and create appropriate visualization of a variable
# based on its data type, some are more appropriate than others.
#Rank                 int64
#System              object
#Cores                int64
#Rmax (PFlop/s)     float64
#Rpeak (PFlop/s)    float64
#Power (kW)         float64

# Summary statistics and Visualizations for Cores, Rmax, Rpeak, and Power
print('Note the missing values in the Power (kW) column in this data set,')
print('there are no missing values for any other variable.')

# Summary Statistics for Cores
print('Summary Statistics and Visualizations for Cores:')
print(df['Cores'].describe().round(1))
# Visualizations for Core
plt.plot(df['Cores'], color = 'blue')
plt.title('Core Values for the Top 500 Supercomputers as of 11/2021', fontsize=
          9)
plt.xlabel('Supercomputer Rating')
plt.ylabel('Number of Cores')
plt.show()

# Summary statistics for Rpeak
print('Summary Statistics and Visualizations for Rpeak:')
print(df['Rpeak (PFlop/s)'].describe().round(1))
# Visualization for Rpeak
plt.plot(df['Rpeak (PFlop/s)']) 
plt.title('Rpeak (PFlop/s) Value of Top 500 Supercomputers as of 11/2021 List')
plt.xlabel('Supercomputer Rating')
plt.ylabel('PFlop/s')
plt.show()

# Summary Statistics for Rmax
print('Summary Statistics and Visualizations for Rmax:')
print(df["Rmax (PFlop/s)"].describe().round(1))
# Visualizations for Rmax
plt.plot(df['Rmax (PFlop/s)'])
plt.title('Rmax (PFlop/s) Value of Top 500 Supercomputers as of 11/2021 List')
plt.xlabel('Supercomputer Rating')
plt.ylabel('PFlop/s')
plt.show()

# Summary Statistics for Power
print('Summary Statistics and Visualizations for Power:')
print(df['Power (kW)'].describe().round(1))
# Visualizations for Power
plt.hist(df['Power (kW)'])
plt.title('Power (kW) Value of Top 500 Supercomputers as of 11/2021 List')
plt.xlabel('Power in Kilowatts (kW)')
plt.ylabel('Frequencies')
plt.show()

# Create CSV file with dataframe info to designated folder
df = pd.read_csv('lablist.csv', na_filter=True)

#Examine and explain the relationship between cores and Power.
print('Scatter plot of cores vs. power:')
plt.scatter(df['Cores'],df['Power (kW)'])
plt.title('Cores vs. Power (kW)')
plt.xlabel('Cores')
plt.ylabel('Power (kW)')
plt.show()

# Tranform data with log function.
df['Cores Log2'] = np.log2(df['Cores'])
df['Power (kW) Log2'] = np.log2(df['Power (kW)'])

# Examine relationship between cores and power based on their log values.
print('Scatterplot of cores vs. power after log2 calculations:')
plt.scatter(df['Cores Log2'],df['Power (kW)'])
plt.title('Cores vs. Power (kW) (Log2)')
plt.show()

# Run correlation coefficient test after removing NaN values from data set.
df.dropna(inplace=True)
cor_matrix = np.corrcoef(df['Cores'],df['Power (kW)'])
corr = cor_matrix[0,1]
rsquared = corr**2
print('Our correlation coefficient is: ',corr)
# Our rsquared value is 0.6075 which indicates that 60.75% of the observed
# variation in Power is described by the model.
print('Our r-squared value is:',rsquared)

# Calculate line of best fit and create scatterplot 
a, b = np.polyfit(df['Cores Log2'],df['Power (kW) Log2'],1)
plt.scatter(df['Cores Log2'],df['Power (kW) Log2'])
plt.plot(df['Cores Log2'],a*df['Cores Log2']+b)
plt.title('Line of Best Fit for Cores vs. Power')
plt.xlabel('Cores')
plt.ylabel('Power')
plt.show()

# Use the mean values of Rmax and Power to determine the requirements for a
# 1.5 exaflop supercomputer.
rmaxmean = df['Rmax (PFlop/s)'].mean()
powermean = df['Power (kW)'].mean()
# 1.5 exaflops = 1500 petaflops
x = 1500 / rmaxmean 
exaPower = powermean * x
exaCores = df['Cores'].mean() * x

print('\nBonus Response - See Working Code for calculations')
print('The number of cores required for a 1.5 exaflop supercomputer is:',
      exaCores)
print('The power required for a 1.5 exaflop supercomputer is: ',exaPower,' kW')
