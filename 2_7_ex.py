def temp_convert(hotcold):
    return ((int(temp)-32)*(5/9))

temp = input ("temperature conversion: ")

print ("temperature in celcius is: ", temp_convert(temp), "celcius")
