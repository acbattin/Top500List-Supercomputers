# Top500List-Supercomputers
Using the BeautifulSoup screen-scraper library, create a .csv file of all 500 supercomputers listed at https://top500.org/lists/top500/2021/11/. Using the Top500 dataset created previously, explore that dataset. Examine and explain the relationship between cores and Power.
* Code Author: Andie Battin
* Last Update: 12/14/2023

# Methods
* Import needed libraries for reading and parsing Web pages - get data for each page on the website
* Using Python, Beautiful Soup for screen-scraping, and other related libraries, successfully create a .csv file for the 500 supercomputers as of November 2021 called “lablist.csv” using the TOP500 website
* Create and read .csv file for top 500 supercomputers

# Clean and display the dataset; that is, remove any unwanted characters from the numeric data items
We confirm our formatting changes for the .csv file created by create and read .csv file for top 500 supercomputers into our environment and confirm formatting changes by checking the summary statistics
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/SummaryOutput.png?raw=true" width="500" height="250"/>
</p>

# Examine and explain the relationship between Cores and Power
Using Python, we generate the following scatterplot using the lablist.csv dataset we generated using the TOP500 website to visualize the relationship between the number of cores and the relative power of the supercomputer.
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/CoresvsPowerScatter1.png?raw=true" width="500" height="500"/>
</p>
