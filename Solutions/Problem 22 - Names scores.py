"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import pandas as pd
import requests
import string

# fetch data
data = requests.get('https://projecteuler.net/project/resources/p022_names.txt')
data = data.text

data = data.split(',')
data = [x.replace('"', '') for x in data]

# construct dataframe containing names data
df = pd.DataFrame(data, columns=['NAMES'])
df = df.sort_values(by='NAMES')
df = df.reset_index(drop=True)

# make sure COLIN is in the right place (1 indexing...)
df['PLACE'] = df.index + 1

# create dict to keep track of alphabetical score
alpha = dict([(j, i + 1,) for i, j in enumerate(list(string.ascii_uppercase))])


def return_alphabetical_value(name):
    alpha_value = int()

    for s in name:
        alpha_value += alpha[s]

    return alpha_value


df['alpha_score'] = df['NAMES'].apply(lambda x: return_alphabetical_value(x))
df['score'] = df['PLACE'] * df['alpha_score']

print(f'Total name score is: {df["score"].sum()}')
