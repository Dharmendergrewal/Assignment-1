"""
    This program reads in data on penguin species and 
    three different types of plots to visualize the 
    data: a line plot of body mass over time for different species, 
    a pie plot of the distribution of penguin species, 
    and a scatter plot of bill length vs bill depth for different species. 
"""
# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt


def plot_line(df):
    plt.plot(df['body_mass_g'], label='Body Mass') # Plots a line chart of body mass against the observation number
    plt.title('Body Mass of Penguins over Time') # Sets the title of the chart
    plt.xlabel('Observation Number') # Sets the label for the x-axis
    plt.ylabel('Body Mass (g)') # Sets the label for the y-axis
    plt.legend() # Displays the legend
    plt.show() # Displays the plot

def plot_pie(df):
    counts = df['species'].value_counts() # Counts the number of occurrences of each penguin species
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%') # Plots a pie chart of penguin species distribution
    plt.title('Distribution of Penguin Species') # Sets the title of the chart
    plt.legend(counts.index, loc='lower right') # Displays the legend
    plt.show() # Displays the plot

def plot_scatter(df):
    plt.scatter(df['bill_length_mm'], df['bill_depth_mm'], label='Penguin') # Plots a scatter plot of bill length against bill depth
    plt.title('Bill Length vs. Bill Depth') # Sets the title of the chart
    plt.xlabel('Bill Length (mm)') # Sets the label for the x-axis
    plt.ylabel('Bill Depth (mm)') # Sets the label for the y-axis
    plt.legend() # Displays the legend
    plt.show() # Displays the plot

# Reading online data
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv'
df = pd.read_csv(url)

# Calling functions
plot_line(df)
plot_pie(df)
plot_scatter(df)
