def conversion (temp, unit):
    if unit == 'C':
        return f"{(temp * 9/5) + 32}°F"
    elif unit == 'F':
        return f"{(temp - 32) * 5/9}°C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

def main():
        temp = float(input("Enter the temperature:"))
        unit = input("Enter the unit: ")
        result = conversion(temp, unit.upper())
        print(f"The temperature is : {result}")
if __name__ == "__main__":
    main()
