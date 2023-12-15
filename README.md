# Top500List-Supercomputers
Using the BeautifulSoup screen-scraper library, create a .csv file of all 500 supercomputers listed at https://top500.org/lists/top500/2021/11/. Using the Top500 dataset created previously, explore that dataset. Examine and explain the relationship between cores and Power.
* Code Author: Andie Battin
* Last Update: 12/14/2023

# Methods
* Import needed libraries for reading and parsing Web pages - get data for each page on the website
* Using Python, Beautiful Soup for screen-scraping, and other related libraries, successfully create a .csv file for the 500 supercomputers as of November 2021 called “lablist.csv” using the TOP500 website
* Create and read .csv file for top 500 supercomputers

# Clean and display the dataset
We confirm our formatting changes for the .csv file created by create and read .csv file for top 500 supercomputers into our environment and confirm formatting changes by checking the summary statistics
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/SummaryOutput.png?raw=true" width="500" height="250"/>
</p>

# Examine and explain the relationship between Cores and Power
Using Python, we generate the following scatterplot using the lablist.csv dataset we generated using the TOP500 website to visualize the relationship between the number of cores and the relative power of the supercomputer.
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/CoresvsPowerScatter1.png?raw=true" width="600" height="500"/>
</p>
We now tranform data with log function in Python and use these results to generate a scatterplot using their log values.
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/CoresvsPowerScatter2.png?raw=true" width="600" height="500"/>
</p>
Examine relationship between cores and power based on their log values.
We remove all missing values and run a correlation coefficient test on the data. Our Console output was as follows: Our rsquared value is 0.6075 which indicates that 60.75% of the observed variation in Power is described by the model.

Calculate line of best fit and create scatterplot
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/BestFit.png?raw=true" width="600" height="500"/>
</p>

# Requirements for a Hypothetical 1.5 𝐸𝑥𝑎𝐹𝐿𝑂𝑃 system
Using the mean values of Rmax and Power we determine the requirements for a 1.5 exaflop supercomputer.
<p align="center">
<img src="https://github.com/acbattin/Top500List-Supercomputers/blob/main/ExaflopOutput.png?raw=true" width="400" height="200"/>
</p>
