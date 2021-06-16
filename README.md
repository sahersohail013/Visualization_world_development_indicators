# Short Description
This repository has been created to showcase information visualization project about visualizing the world development indicators over the span of 30 years and in south asia. We have used tableau desktop to create two different type of visualizarions for each indicator i.e static and dynamic. An in depth exploratory data analysis was carried out and we observed the various trends that have occured. The analysis was done keeping the various data visualization principles in view and to make the analysis more impactful we projected the population in pakistan for the next 10 years using regression

# Dataset
Tne data set has been taken from the following source <a href="https://www.kaggle.com/manchunhui/world-development-indicators#">2020 World Development Indicators</a>


# Repository Files
Project.rar - Tableau Dashboard File<br>
lr.py - Jupyter Notebook for Regression Analysis<br>
xlxs.rar - Dataset in csv format<br>
screenshots.rar - Dashboard images<br>


# Libraries: 
  numpy, matplotlib, sklearn.metrics, sklearn.linear_model, pandas

# Detailed documentation:
This project consists of two parts <br>
1.EDA and Dashboard in Tableau<br>
2.Regression Analysis in Python Jupyter Notebook<br>
To run the Tableau Dashboard download the .twb file and import to Tableau. Please note this dashboard has been created in Licensed Tableau Desktop. Therefore, it might not be compatible with Tableau public.<br>
Now extract these features/columns along with the country names: <br>
-Mobile cellular subscription<br>
  -Arms import<br>
  -Population<br>
-Refugee count by country<br>
-Number of new businesses registered<br>
After extracting these features convert these files from ‘csv’ format to ‘xlsx’ that is an excel workbook otherwise Tableau wont connect to it.
Download Table Desktop from the official website of Tableau and sign up for a trial.
Now place the tableau files and excel workbooks in the same folder and try to open a dashboard using tableau desktop. 
Keep in mind that dynamic visualizations won’t run on Table public and you have to download Tableau Desktop. <br>

To run the python code please install Jupyter Notebook software and load .ipynb file provided in the repository. The python pacakges used for visulization and data handling are as follows.

Pandas and Numpy - To handle and anlyse the data<br>
Matplotlib - To visualize data<br>
Sklean - To apply reggression<br>

# Project Architecture
Dataset Chosen: 2020 World Development Indicators <br>
Indicators Chosen:<br>
Arms Imports<br>
Mobile Cellular Subscriptions<br>
New Businesses Registered<br>
Population Total<br>
Refugee Population by Country or Territory of Origin<br>
Data Preprocessing: <br>
Filtered Data into subsets w.r.t. the 5 indicators<br>
Filtered out the population data for Pakistan<br>
Predictions:<br>
Using Linear regression, predicted the population of Pakistan for the next 10 years.<br>
Data Preprocessing Tools:<br>
Python 3<br>
Jupyter Notebook<br>
Visualizations:<br>
Racing Bar Chart<br>
World Map<br>
Bar Chart<br>
Visualization Tools:<br>
Tableau Desktop<br>

# Members: 
-Nikhar Azhar <br>
-Huma Ameer<br> 
-Saher Sohail<br>
-Fasih Ashfaq<br>
-Usama Naveed
