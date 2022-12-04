#!/usr/bin/python3.10

temperature = 5

if temperature > 30:
    print("It's hot day")
    print("Drink more water")

elif temperature >20: #Temperature (20, 30]
    print("It's nice day")

elif temperature > 10:
    print("It's a bit cold")

else:
    print("It's cold")
print("Done")
