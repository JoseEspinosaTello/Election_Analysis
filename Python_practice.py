print("Hello World")

print(type(" "))

a = 5 + 2 * 3

b = 8 // 5 - 3
c = 8 + 22 * 2 - 4
d = 16 - 3 / 2 + 7 - 1
e = 3 ** 3 % 5
f = 5 + 9 * 3 / 2 - 4

print(a, b, c, d, e, f)

counties = ["Arapahoe","Denver","Jefferson"]

print(counties)

print(counties[0])

print(len(counties))

#3.2.10

for i in range(len(counties)):

	print(counties[i])

counties_tuple = ("Arapahoe","Denver","Jefferson")

for county in counties_tuple:
	print(county)

#iterate through a DIctionary

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:

	print(county)

for county in counties_dict.keys(): #returns keys
	print(county)

for voters in counties_dict.values(): #returns values
    print(voters)

for key, value in counties_dict.items(): #returns key and value
	print(key,value)

#Skill Drill Print each county and registered voter form the counties dictionary so that the output looks like this:

# Iterate Through a List of Dictionaries

voting_data=[{"county":"Arapahoe","registered_voters":422829},
		{"county":"Denver","registered_voters":463353},
{"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
	print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

#Get the Values from a List of Dictionaries

for county_dict in voting_data:

	for value in county_dict.values():
	
		print(value)