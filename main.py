print("Exercise 1: Fahrenheit to Celcius")
#Two separate options are shown below for weather or thermometer readings where responses are typically whole numbers or have one decimal place.

weatherFahrenheit = int(input("Please enter the outdoor temperature in Farenheit: "))
weatherCelsius = int((weatherFahrenheit - 32) * (5/9))

print()
print(f"Farenheit: {weatherFahrenheit}")
print(f"Celcius: {weatherCelsius}")

print()
thermometerFahrenheit = float(input("Please enter your temperature in Farenheit: "))
thermometerCelsius = format((thermometerFahrenheit - 32) * (5/9),".1f")

print()
print(f"Farenheit: {thermometerFahrenheit}")
print(f"Celcius: {thermometerCelsius}")
