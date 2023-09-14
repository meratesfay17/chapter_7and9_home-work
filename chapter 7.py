# define the years_list
years_list = [1998, 1999, 2000, 2001, 2002, 2003]

# find the year of your third birthday 
third_birthday_year = years_list[2]
print(f"your third birthday will be in the year of {third_birthday_year} ")

# in which year were you the oldest 
oldest_year = years_list[-1]
print(f"In this year you were the older {oldest_year}")

# 7.4 define the things
things = ["mozzarella", "cinderella", "salmonella"]
# 7.5 Capitalize the persent name and list them all
things[1] = things[1].capitalize()
print(things)
# 7.6 Make the cheesy element of things all uppercase and then print the list
things[0] = things[0].upper()
print(things)
# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
things.remove("salmonella")

# Print the updated list
print(things)

