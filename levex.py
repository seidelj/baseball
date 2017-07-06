# install with: pip install python-Levenshtein
from Levenshtein import distance

# caps matter
print distance("Hello", "hello")

# spaces matter
print distance("Joe Seidel", "Joe  Seidel")

# we can safeley remedy this
print distance("Hello".lower(), "hello")

# replace takes up to 3 parameters:
# the old, new, and max number of times to replace
print distance("Joe Seidel", "Joe  Seidel".replace(" ",'', 1))


import csv


with open('draft.csv', 'rb') as f:
    creader = csv.reader(f)
    # skip headers
    #next(creader, None)
    # for later
    headers = next(creader)
    draft = []
    for row in creader:
        draft.append(row)

# we want to add a some info to this data
for row in draft:
    row.append(2016)

# we want to covert salary to an integer
for row in draft:
    value = row[7]
    value = value.replace('$','')
    # try conversion
    value = value.replace(',','')
    # try conversion
    try:
        value = int(value)
    except ValueError:
        pass
    row[7] = value
# Exercise, can we combine some lines?

# calculate the average bonus, conditional on
# having a value for bonus

bonuses = []
for row in draft:
    bonus = row[7]
    if isinstance(bonus, int):
        bonuses.append(bonus)
# Exercise, can we combine some lines?

# compute the average
sumOfBonuses = sum(bonuses)
numOfBonuses = len(bonuses)
averageBonus = float(sumOfBonuses)/numOfBonuses

print(averageBonus)
# Exercise: combine these lines

# lets create a new file to save our work
# we just realized have the headers would be useful
with open('draft_year.csv', 'w') as f:
    cwriter = csv.writer(f, csv.excel)
    cwriter.writerow(headers + ['year'])
    for row in draft:
        cwriter.writerow(row)

