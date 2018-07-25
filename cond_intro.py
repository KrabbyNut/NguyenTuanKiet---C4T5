yob = int(input("Your year of birth ? "))
age = 2018 - yob

print(age)

if age < 10:
    print("Baby is not allowed")
elif age < 18:
    print("Teenager")
else:
    print("Your're Welcome")