def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# User input
temperature = float(input("Enter temperature value: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

if unit == "C":
    converted = celsius_to_fahrenheit(temperature)
    print(f"{temperature}°C = {converted:.2f}°F")

elif unit == "F":
    converted = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°F = {converted:.2f}°C")

else:
    print("Invalid unit! Please enter C or F.")
