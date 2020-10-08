def weight_convert(metric):
    return ((0.453592)* int(pounds))

pounds = input ("enter your weight to see if you can ride this ride: ")

print ("congrats, your lighter in kg: ", weight_convert(pounds), " kgs")

