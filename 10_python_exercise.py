# In this exercise we want to count the numbe of times each country won a tender in the ted-sample.csv file

# T1. Find headers/indxs for relevant vars: IDO_COUNTRY_CODE, WIN_COUNTRY_CODE
f = open('data/raw/european_comission/ted-sample.csv')

# Grab headers 
headers = f.readline().strip().split(',')

# Make sure to close the file
f.close()

for index, value in enumerate(headers):
  print(index, value)

# WIN_COUNTY_CODE at index 61

# 2. Instantiate an empty list called data
data = []

# 3. Use the context manager open() and
# 3.1 iterate through each row in ted-sample.csv and 
# 3.2 append each row to the data list using (in the loop body)     
#     data.append(list(line.split(",")))

with open('data/raw/european_comission/ted-sample.csv') as f:
  for line in f:
    data.append(list(line.split(",")))


print(data[0])
# Output should look like: data = [[row0], [row1], ..., [rowN]]
data = data[1:] # Get rid of headers; don't need them  
# or data.pop(0)

# 4. Count the number of wins by country 
# Output should look like: d = {country1: N1,
#                             ...
#                             countryN: NN,}

d = {}
for row in data:
  country = row[61] # Careful: some tenders are won by more than one county 
  countries = country.split('---') # Returns a list if winning countries 
  for winning_country in countries:
    if not winning_country in d:
      d[winning_country] = 0
    d[winning_country] += 1

print(d)

