import pandas as pd
from scipy.stats import binom, poisson, hypergeom

# load data
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# soal 1
eligible_jumpers = data[(data['Age'] >= 16) & (data['Age'] <= 25)]
total_family_members = len(data)
eligible_jumpers_count = len(eligible_jumpers)

p_success = eligible_jumpers_count / total_family_members

n_jumpers = 6  # total number of people chosen
k_jumpers = 4  # number of successes
prob_4_success = binom.pmf(k_jumpers, n_jumpers, p_success)

mean_jumpers = n_jumpers * p_success
std_dev_jumpers = (n_jumpers * p_success * (1 - p_success)) ** 0.5

# soal 2
flu_cases = data[(data['Age'] >= 30) & (data['Age'] <= 50)]
flu_case_count = len(flu_cases)


average_flu_cases = flu_case_count / total_family_members

k_flu = 3  # number of people getting the flu
prob_3_flu_cases = poisson.pmf(k_flu, average_flu_cases)

mean_flu = average_flu_cases
std_dev_flu = mean_flu ** 0.5

# soal 3
age_30_or_less = data[data['Age'] <= 30]

overall_members = len(age_30_or_less)
overall_male_members = len(age_30_or_less[age_30_or_less['Gender'] == 'M'])
overall_female_members = len(age_30_or_less[age_30_or_less['Gender'] == 'F'])

chosen_member = age_30_or_less.loc[age_30_or_less['Age'].idxmax()]

N = overall_members  # total members
K = overall_male_members  # total males
n_hyper = 3  # number of members chosen
x_hyper = 3  # number of males chosen

probability_all_males = hypergeom.pmf(x_hyper, N, K, n_hyper)

mean_hyper = n_hyper * (K / N)
std_dev_hyper = ((n_hyper * (K / N) * (1 - K / N) * ((N - n_hyper) / (N - 1)))) ** 0.5

# output stakcscksadfkl;jfdsa;knljkjfdsakl;jkjfaksl;jfajdl;kss
print("===== SOAL 1 =====")
print(f"successful 1.2m jumpers probability: {prob_4_success}")
print(f"successful 1.2m jump mean: {mean_jumpers}")
print(f"std dev: {std_dev_jumpers}")

print("\n===== SOAL 2 =====")
print(f"flu cases mean in a month: {average_flu_cases}")
print(f"probability for 3 flu cases: {prob_3_flu_cases}")
print(f"flu cases mean: {mean_flu}")
print(f"flu cases std dev: {std_dev_flu}")

print("\n===== SOAL 3 =====")
# debug stuff
# print(f"Jumlah total anggota (umur <= 30): {overall_members}")
# print(f"Jumlah total laki-laki (umur <= 30): {overall_male_members}")
# print(f"Jumlah total perempuan (umur <= 30): {overall_female_members}")
# print(f"Anggota dengan umur tertinggi (<= 30): {chosen_member['Name']}")
print(f"probabilty to choose all males to go to jakarta: {probability_all_males}")
print(f"hypergeometric mean: {mean_hyper}")
print(f"std deviation: {std_dev_hyper}")
