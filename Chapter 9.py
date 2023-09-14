def good():
    return ['Harry', 'Ron', 'Hermione']
good_list = good()
print(good_list)
# 9.2 Define a generator function called get_odds() and return the odd num from range
def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

# Use a for loop to find and print the third value returned
count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print("The third odd number is:", odd)
        break
