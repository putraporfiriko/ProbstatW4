import pandas as pd
from scipy.stats import poisson

# Load the data
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Step 1: Calculate the average number of people that got the flu
# Flu based on age range 30 <= x <= 50
flu_cases = data[(data['Age'] >= 30) & (data['Age'] <= 50)]
total_people = len(data)
flu_case_count = len(flu_cases)

# Average number of people that got the flu
average_flu_cases = flu_case_count / total_people

# Step 2: Probability that exactly 3 people got the flu (Poisson distribution)
k = 3  # number of people getting the flu
# Using the average number of flu cases (lambda) as the rate parameter for the Poisson distribution
prob_3_flu_cases = poisson.pmf(k, average_flu_cases)

# Step 3: Mean and standard deviation for the Poisson distribution
# Mean for Poisson is the average (lambda)
mean = average_flu_cases

# Standard deviation for Poisson is sqrt(lambda)
std_dev = mean ** 0.5

# Output results
results = {
    "Average flu cases": average_flu_cases,
    "Probability of 3 flu cases": prob_3_flu_cases,
    "Mean": mean,
    "Standard Deviation": std_dev
}

for data in results:
    print(data, ":", results[data])
