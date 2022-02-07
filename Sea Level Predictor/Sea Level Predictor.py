import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # to use np.arange()
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (10,5))
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    linr = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    x_extended = np.arange(df["Year"].min(),2051) # extend to 2050

    plt.plot(x_extended, (linr.slope*x_extended)+linr.intercept, c = "g") #linear regression formula (slope*x)+intercept

    # Create second line of best fit
    df2k = df[df["Year"]>= 2000]
    linr2k = linregress(df2k["Year"],df2k["CSIRO Adjusted Sea Level"])
    x_extended2k=np.arange(2000,2051)

    plt.plot(x_extended2k, (linr2k.slope*x_extended2k)+linr2k.intercept, c = "red")


    # Add labels and title
    plt.title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
