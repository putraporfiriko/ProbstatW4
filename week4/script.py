import pandas as pd
from itertools import combinations, permutations

# set xlsx path
xlsx_path = r'''data.xlsx'''
# Load the data (xlsx file)
data = pd.read_excel(xlsx_path)

#column 1 = name
#column 2 = age
#column 3 = Weight (in kg)
#column 4 = Gender
#column 5 = Height (in cm)

# Print the data
# print(data)

# make into dictionary: {index:{column_name: value, column_name: value, ...}}
data_dict = data.to_dict(orient='index')

# for each index in the dictionary, check the age value. if its >18, add to a counter. if its <18, add to another counter
over_18 = 0
under_18 = 0
for index in data_dict:
    if data_dict[index]['Age'] > 18:
        over_18 += 1
    else:
        under_18 += 1

# count the probabilities of each group
total = over_18 + under_18
prob_over_18 = over_18 / total
prob_under_18 = under_18 / total

# with itertools, find how much permutations and combination that can be made if we choose 4 unique people from the data
perms = list(permutations(data_dict, 4))
combs = list(combinations(data_dict, 4))

# question 3.
# a = members with height > 150
# b = members with gender == F
# c = members with weight > 50
# d = members with gender == M

a = {}
b = {}
c = {}
d = {}

for index in data_dict:
    if data_dict[index]['Height'] > 150:
        a[index] = data_dict[index]
    if data_dict[index]['Gender'] == 'F':
        b[index] = data_dict[index]
    if data_dict[index]['Weight'] > 50:
        c[index] = data_dict[index]
    if data_dict[index]['Gender'] == 'M':
        d[index] = data_dict[index]

# print each index of dict on a diff line (data is valid YEAH)
# print("group a")
# for index in a:
#     print(a[index])
# print("group b")
# for index in b:
#     print(b[index])
# print("group c")
# for index in c:
#     print(c[index])
# print("group d")
# for index in d:
#     print(d[index])


a_intersect_c = (a.keys() & c.keys())
a_union_c = (a.keys() | c.keys())
a_logicaldisj_b = (a.keys() ^ b.keys())
c_logicaldisj_d = (c.keys() ^ d.keys())

# count perms
perms_a_intersect_c = list(permutations(a_intersect_c, 4))
perms_a_union_c = list(permutations(a_union_c, 4))
perms_a_logicaldisj_b = list(permutations(a_logicaldisj_b, 4))
perms_c_logicaldisj_d = list(permutations(c_logicaldisj_d, 4))

# s1 = age < 20
# s2 = 20 <= age < 40
# s3 = 40 <= age < 60
# s4 = 60 <= age

s1 = {}
s2 = {}
s3 = {}
s4 = {}

for index in data_dict:
    if data_dict[index]['Age'] < 20:
        s1[index] = data_dict[index]
    elif 20 <= data_dict[index]['Age'] < 40:
        s2[index] = data_dict[index]
    elif 40 <= data_dict[index]['Age'] < 60:
        s3[index] = data_dict[index]
    elif 60 <= data_dict[index]['Age']:
        s4[index] = data_dict[index]

## data validation
# print(len(s1))
# print(len(s2))
# print(len(s3))
# print(len(s4))

# print(len(s1)+len(s2)+len(s3)+len(s4))

#perm s1, s2, s3, s4
perms_s1 = list(permutations(s1, len(s1)))
perms_s2 = list(permutations(s2, len(s2)))
perms_s3 = list(permutations(s3, len(s3)))
perms_s4 = list(permutations(s4, len(s4)))

# output stack!!!!
print('Soal 1:')
print(f'probabilitas dapat mengikuti piknik keluarga: {prob_over_18}')
print(f'probabilitas tidak dapat mengikuti piknik keluarga: {prob_under_18}')

print('\nSoal 2:')
print(f'Permutations: {len(perms)}')
print(f'Combinations: {len(combs)}')

print('\nSoal 3:')
print(f'Permutasi dari a intersect c: {len(perms_a_intersect_c)}')
print(f'Permutasi dari a union c: {len(perms_a_union_c)}')
print(f'Permutasi dari a logical disjunction b: {len(perms_a_logicaldisj_b)}')
print(f'Permutasi dari c logical disjunction d: {len(perms_c_logicaldisj_d)}')

print('\nSoal 4:')
print(len(perms_s1))
print(len(perms_s2))
print(len(perms_s3))
print(len(perms_s4))
