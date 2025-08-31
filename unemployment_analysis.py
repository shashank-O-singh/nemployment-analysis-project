# Import necessary libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Data Loading and Preparation ---

# Load the dataset from the CSV file
# This file contains unemployment data for Indian states up to November 2020.
df = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')

# Clean up the column names to make them easier to work with.
# The original names have leading spaces and special characters.
df.columns = ['state', 'date', 'frequency', 'unemployment_rate_percent', 'estimated_employed', 'labour_participation_rate_percent', 'region', 'longitude', 'latitude']

# Convert the 'date' column to a proper datetime format.
# This is essential for performing time-series analysis.
df['date'] = pd.to_datetime(df['date'], dayfirst=True)


# --- Step 2: Data Analysis ---

# To see the overall trend, we'll calculate the average unemployment rate
# across all states for each month.
monthly_avg_unemployment = df.groupby('date')['unemployment_rate_percent'].mean().reset_index()

# For context, let's calculate the average unemployment rate before the lockdown
# (January and February 2020) to serve as a baseline.
pre_lockdown_avg = monthly_avg_unemployment[monthly_avg_unemployment['date'] < '2020-03-01']['unemployment_rate_percent'].mean()


# --- Step 3: Data Visualization ---

# Set a visually appealing style for the plot
sns.set_style("whitegrid")
plt.figure(figsize=(12, 7))

# Create the main line plot showing the unemployment trend over time
ax = sns.lineplot(x='date', y='unemployment_rate_percent', data=monthly_avg_unemployment, marker='o', label='Monthly Average Rate')

# Add the pre-lockdown average as a dashed line for comparison
ax.axhline(y=pre_lockdown_avg, color='red', linestyle='--', label=f'Pre-Lockdown Average ({pre_lockdown_avg:.2f}%)')

# Highlight the peak unemployment rate during the lockdown
peak_date = monthly_avg_unemployment.loc[monthly_avg_unemployment['unemployment_rate_percent'].idxmax()]['date']
peak_value = monthly_avg_unemployment['unemployment_rate_percent'].max()
ax.annotate('Lockdown Peak',
            xy=(peak_date, peak_value),
            xytext=(peak_date, peak_value + 2), # Position the text slightly above the peak
            arrowprops=dict(facecolor='black', shrink=0.05),
            ha='center') # Horizontal alignment

# Add clear titles and labels to the plot to explain what it shows
plt.title("Impact of Covid-19 on India's Unemployment Rate (2020)", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Unemployment Rate (%)", fontsize=12)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend to explain the lines
plt.legend()

# Ensure the plot layout is clean and nothing is cut off
plt.tight_layout()

# Save the final plot as an image file
plt.savefig('unemployment_rate_over_time.png')

print("Analysis complete. The plot has been saved as 'unemployment_rate_over_time.png'")