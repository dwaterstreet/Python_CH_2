def age_finder(age):
    return (2020-int(x))

"""must identify the variable as an integer otherwise it will
compile it as a str and you can't subtract a letter from a number, dummy"""

x = input ("enter the year you were born: ")

print ("your age is: ", age_finder(x))
