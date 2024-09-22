import pandas as pd
from scipy.stats import binom

# Load the data
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Define parameters
n = 6  # number of people chosen for the new competition
k = 4  # number of successes

# Step 1: Calculate the probability of success based on the age range
eligible_jumpers = data[(data['Age'] >= 16) & (data['Age'] <= 25)]
total_family_members = len(data)
eligible_jumpers_count = len(eligible_jumpers)

# Probability of success (jumping 1.2 meters)
p = eligible_jumpers_count / total_family_members

# Step 2: Calculate the probability of exactly 4 successes in a binomial distribution
prob_4_success = binom.pmf(k, n, p)

# Step 3: Calculate the mean and standard deviation
mean = n * p
std_dev = (n * p * (1 - p)) ** 0.5

# Output results
results = {
    "Probability of success (p)": p,
    "Probability of 4 successes out of 6": prob_4_success,
    "Mean": mean,
    "Standard Deviation": std_dev
}

for data in results:
    print(data, ":", results[data])
