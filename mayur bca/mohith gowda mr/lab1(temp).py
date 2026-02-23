def temperature_converter():
    print("Temperature Converter")
    choice = input("Enter choice (C/F): ")

    if choice.upper() == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice.upper() == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Invalid choice")

temperature_converter()
