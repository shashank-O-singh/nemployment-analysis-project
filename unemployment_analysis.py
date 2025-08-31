# Import the necessary tools for our data work.
# pandas is for handling our data tables (like a spreadsheet).
# matplotlib and seaborn are for creating our charts.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_national_unemployment():
    """
    First, we'll look at the big picture: the national unemployment rate for 2020.
    This will help us see the overall impact of the lockdown.
    """
    print("--- Starting Analysis 1: The Big Picture (National Unemployment) ---")

    # Step 1: Load the national data
    # We're reading the first CSV file into a data table called 'df'.
    df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')

    # Step 2: Clean up the column names
    # The original names are a bit messy, so we'll simplify them.
    df.columns = ['state', 'date', 'frequency', 'unemployment_rate_percent', 'estimated_employed', 'labour_participation_rate_percent', 'region', 'longitude', 'latitude']

    # Step 3: Make sure dates are treated as dates
    # This helps Python understand how to plot the data over time.
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    # Step 4: Calculate the average unemployment rate for each month
    monthly_avg_unemployment = df.groupby('date')['unemployment_rate_percent'].mean().reset_index()

    # Step 5: Create and save the chart
    print("Creating the first chart...")
    plt.figure(figsize=(12, 7))
    sns.set_style("whitegrid")
    plt.title("Impact of Covid-19 on India's Unemployment Rate (2020)", fontsize=16)
    sns.lineplot(x='date', y='unemployment_rate_percent', data=monthly_avg_unemployment, marker='o')
    plt.xlabel("Month")
    plt.ylabel("Average Unemployment Rate (%)")
    plt.savefig('unemployment_rate_over_time.png')
    print("Success! Chart saved as 'unemployment_rate_over_time.png'")
    plt.close()


def analyze_rural_vs_urban_unemployment():
    """
    Now, let's dive deeper and compare the story in rural and urban areas.
    This uses the second, more detailed dataset.
    """
    print("\n--- Starting Analysis 2: Comparing Rural vs. Urban Areas ---")

    # Step 1: Load the rural/urban dataset
    df_rural_urban = pd.read_csv('Unemployment in India.csv')

    # Step 2: Clean up the column names and remove any empty rows
    df_rural_urban.columns = ['state', 'date', 'frequency', 'unemployment_rate_percent', 'estimated_employed', 'labour_participation_rate_percent', 'area']
    df_rural_urban.dropna(inplace=True) # inplace=True modifies the table directly

    # Step 3: Make sure the dates are understood correctly
    df_rural_urban['date'] = pd.to_datetime(df_rural_urban['date'], dayfirst=True)

    # Step 4: Calculate the average rate, but this time separated by 'area'
    avg_unemployment_by_area = df_rural_urban.groupby(['date', 'area'])['unemployment_rate_percent'].mean().reset_index()

    # Step 5: Create and save the comparison chart
    print("Creating the second chart...")
    plt.figure(figsize=(14, 8))
    sns.set_style("whitegrid")
    plt.title('Rural vs. Urban Unemployment Rate in India (2019-2020)', fontsize=16)
    # The 'hue' parameter is the magic that creates separate lines for each 'area'.
    sns.lineplot(data=avg_unemployment_by_area, x='date', y='unemployment_rate_percent', hue='area', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Average Unemployment Rate (%)')
    plt.savefig('rural_vs_urban_unemployment.png')
    print("Success! Chart saved as 'rural_vs_urban_unemployment.png'")
    plt.close()


# This is the main part of our script that runs everything.
if __name__ == "__main__":
    analyze_national_unemployment()
    analyze_rural_vs_urban_unemployment()
    print("\nProject complete! Both analyses have been run and charts have been saved.")
