#Task2: Temperature Conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("======================")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1/2): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        converted_temp = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {converted_temp}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        converted_temp = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {converted_temp}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
