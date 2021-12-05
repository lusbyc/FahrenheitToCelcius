print("Exercise 1: Fahrenheit to Celcius")
#Two separate options are shown below for weather or thermometer readings where responses are typically whole numbers or have one decimal place.

weather_fahrenheit = int(input("Please enter the outdoor temperature in Farenheit: "))
weather_celsius = int((weather_fahrenheit - 32) * (5/9))

print()
print(f"Farenheit: {weather_fahrenheit}")
print(f"Celcius: {weather_celsius}")

print()
thermometer_fahrenheit = float(input("Please enter your temperature in Farenheit: "))
thermometer_celsius = format((thermometer_fahrenheit - 32) * (5/9),".1f")

print()
print(f"Farenheit: {thermometer_fahrenheit}")
print(f"Celcius: {thermometer_celsius}")
