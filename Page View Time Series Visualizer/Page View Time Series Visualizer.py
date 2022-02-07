import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col= "date")

# Clean data
botclean = df["value"].quantile(0.025)
topclean = df["value"].quantile(0.975)

df = df[(df["value"] <= topclean) & (df["value"] >= botclean)]

def draw_line_plot():

    # Draw line plot
    fig = plt.figure()
    fig, ax = plt.subplots(figsize=(20,8))
    plt.plot(df, color = "red")

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    ax.set_title('ConciseFormatter', loc='left', fontsize='medium')
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    plt.ylabel("Page Views")

  # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

df1 = df.copy()
df1.reset_index(inplace=True)
df1["date"] = pd.to_datetime(df1['date'], format='%Y-%m-%d') #fix replit bug in .dt
df1['Month'] = df1['date'].dt.month
df1["Year"] = df1['date'].dt.year

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df1.pivot_table(values = "value",columns="Month",index="Year",aggfunc='mean')
    # Draw bar plot
    fig = df_bar.plot.bar(legend=True, figsize = (10,5), ylabel="Average Page Views", xlabel="Years").figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xticks(fontsize = 10)
    plt.yticks(fontsize = 10)
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box.date, format='%Y-%m-%d') #fix bug
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, sharex=False, figsize=(16,5))
    ax[0] = sns.boxplot(x=df_box["year"],y=df_box["value"],ax = ax[0])
    ax[1] = sns.boxplot(x=df_box["month"],y=df_box["value"],ax = ax[1])
    
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
