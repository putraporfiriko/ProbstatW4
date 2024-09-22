import pandas as pd
from scipy.stats import hypergeom

# Load the data
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Step 1: Filter members with age <= 30
age_30_or_less = data[data['Age'] <= 30]

# Count overall members, male members, and female members from the filtered data
overall_members = len(age_30_or_less)
overall_male_members = len(age_30_or_less[age_30_or_less['Gender'] == 'M'])
overall_female_members = len(age_30_or_less[age_30_or_less['Gender'] == 'F'])

# Step 2: Find the member with the highest age (within the age <= 30 sample)
chosen_member = age_30_or_less.loc[age_30_or_less['Age'].idxmax()]

# Step 3: Use hypergeometric distribution to calculate the probability
# Parameters for Hypergeometric distribution:
# N = total number of members in the sample (age <= 30)
# K = total number of male members in the sample (age <= 30)
# n = number of members to choose (3)
# x = number of male members we want (3)

N = overall_members  # total members
K = overall_male_members  # total males
n = 3  # number of members chosen
x = 3  # number of males chosen

# Hypergeometric probability for choosing 3 males
probability_all_males = hypergeom.pmf(x, N, K, n)

# Step 4: Mean and standard deviation for Hypergeometric distribution
# Mean = n * (K / N)
mean = n * (K / N)

# Standard deviation = sqrt(n * (K/N) * (1 - K/N) * ((N - n) / (N - 1)))
std_dev = ((n * (K / N) * (1 - K / N) * ((N - n) / (N - 1)))) ** 0.5

# Output results
results = {
    "Overall members (age <= 30)": overall_members,
    "Overall male members (age <= 30)": overall_male_members,
    "Overall female members (age <= 30)": overall_female_members,
    "Member with highest age (<= 30)": chosen_member['Name'],
    "Probability of choosing 3 males": probability_all_males,
    "Mean": mean,
    "Standard Deviation": std_dev
}

for data in results:
    print(data, ":", results[data])
