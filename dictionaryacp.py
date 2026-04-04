test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print("The original dictionary : " + str(test_dict))

user  = int(input("Write the number of frequency in the above dictionary"))

count = 0
for key in test_dict:
    if test_dict[key] == user:
        count += 1


print("Frequency of your enntered number is is :" + str(count))