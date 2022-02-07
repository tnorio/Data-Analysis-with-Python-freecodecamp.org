import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df["education"] == "Bachelors"]) / len(df)) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    studied = df[(df["education"] == "Masters")| (df["education"] == "Doctorate")| (df["education"] == "Bachelors")]
    not_studied = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    # percentage with salary >50K
    studied_rich = studied[studied["salary"] == ">50K"]
    no_studied_rich = not_studied[not_studied["salary"] == ">50K"]

    higher_education_rich = round((len(studied_rich) / len(studied))*100,1)
    lower_education_rich = round((len(no_studied_rich) / len(not_studied))*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    min_hour_rich = df[(df["hours-per-week"]== min_work_hours) & (df["salary"] == ">50K")]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[ df["hours-per-week"] == min_work_hours])

    rich_percentage = round((len(min_hour_rich) / num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    rich = df[df["salary"] == ">50K"]
    rich = rich.loc[:,["native-country", "salary"]].value_counts().sort_index()

    countries = df.groupby(["native-country"]).count().sort_index()

    richest_countries = rich/countries["salary"]

    highest_earning_country = (richest_countries).idxmax()[0]

    richest_countries = richest_countries.reset_index()


    highest_earning_country_percentage = round(richest_countries[richest_countries["native-country"] == highest_earning_country][0].sum()*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_in_50k = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
    top_IN_occupation = df_in_50k["occupation"].value_counts().index[0]
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }