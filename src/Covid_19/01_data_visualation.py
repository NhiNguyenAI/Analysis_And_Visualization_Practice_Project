"""
************************************************************************
 *
 * data_visualization.py
 *
 * Initial Creation:
 *    Author      Nhi Nguyen
 *    Created on  2025-26-03
 *
 ************************************************************************/
"""

#--------------------------------------------------------------------------------#
#                                 Libraries                                      #
#--------------------------------------------------------------------------------#
# Data analysis and Manipulation
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
import pandas as pd

# Data Visualization
import matplotlib.pyplot as plt

# Importing Plotly
import plotly.offline as py
from plotly.figure_factory import create_table
py.init_notebook_mode(connected=True)

# Initializing Plotly
pio.renderers.default = 'colab'

#--------------------------------------------------------------------------------#
#                                 Importing datasets                             #
#--------------------------------------------------------------------------------#
# Importing Dataset1
dataset_covid = pd.read_csv("../../data/Covid_19/raw/covid.csv")
dataset_covid.head()
dataset_covid.info()
print(dataset_covid.shape)
print(dataset_covid.size)


dataset_covid_grouped = pd.read_csv("../../data/Covid_19/raw/covid_grouped.csv")
dataset_covid_grouped.head()
dataset_covid_grouped.info()
print(dataset_covid_grouped.shape)
print(dataset_covid_grouped.size)

dataset_coviddeath = pd.read_csv("../../data/Covid_19/raw/coviddeath.csv")
dataset_coviddeath.head()
dataset_coviddeath.info()
print(dataset_coviddeath.shape)
print(dataset_coviddeath.size)

#--------------------------------------------------------------------------------#
#                         Creating table using plotly express                    #
#--------------------------------------------------------------------------------#

# Import create_table Figure Factory

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
table = create_table(dataset_covid.head(15), colorscale=colorscale)
py.iplot(table)

#--------------------------------------------------------------------------------#
# Bar chart using plotly express                                                 #
#--------------------------------------------------------------------------------#
# Orientation followed by vertical data x
px.bar(dataset_covid.head(15), x = 'Country/Region',
       y = 'TotalCases',color = 'TotalCases',
       height = 500,hover_data = ['Country/Region', 'Continent'])

px.bar(dataset_covid.head(15), x = 'Country/Region', y = 'TotalCases',
       color = 'TotalDeaths', height = 500,
       hover_data = ['Country/Region', 'Continent'])

# Orientation followed by horizontal data y
px.bar(dataset_covid.head(15), x = 'TotalCases', y = 'Country/Region',
       color = 'TotalCases',orientation ='h',  height = 500,
       hover_data = ['Country/Region', 'Continent'])

#--------------------------------------------------------------------------------#
# Bubble chart                                                                   #
#--------------------------------------------------------------------------------#
px.scatter(dataset_covid.head(30), x='Country/Region', y='TotalCases', 
           hover_data=['Country/Region', 'Continent'],
           color='Country/Region', size='TotalCases', size_max=80, log_y=True)


#--------------------------------------------------------------------------------#
# Advandced Data Visualization - Bar graphs for all top                          #
#--------------------------------------------------------------------------------#
px.bar(dataset_covid_grouped, x="Date", y="Confirmed", color="Confirmed", 
       hover_data=["Confirmed", "Date", "Country/Region"], height=400)


#--------------------------------------------------------------------------------#
# Choose the country and plot the data                                          #
#--------------------------------------------------------------------------------#
dataset_covid_grouped_us = dataset_covid_grouped[dataset_covid_grouped['Country/Region'] == 'US']
dataset_covid_grouped_us.head()

px.bar(dataset_covid_grouped_us, x="Date", y="Confirmed", color="Confirmed", height=400)

#--------------------------------------------------------------------------------#
# Line chart                                                                     #
#--------------------------------------------------------------------------------#
px.line(dataset_covid_grouped_us,x="Date", y="Recovered", height=400)

#--------------------------------------------------------------------------------#
# Scatter chart                                                                  #
#--------------------------------------------------------------------------------#
px.scatter(dataset_covid_grouped_us, x="Confirmed", y="Deaths", height=400)


#--------------------------------------------------------------------------------#
# Visualization of Data in terms of Maps                                                                  #
#--------------------------------------------------------------------------------#

px.choropleth(dataset_covid_grouped,
              locations="iso_alpha",
              color="Confirmed",
              hover_name="Country/Region", 
              color_continuous_scale="Blues",
              animation_frame="Date")


px.choropleth(dataset_covid_grouped_us,
              locations="iso_alpha",
              color="Confirmed",
              hover_name="Country/Region",
              color_continuous_scale="Blues",
              animation_frame="Date")
