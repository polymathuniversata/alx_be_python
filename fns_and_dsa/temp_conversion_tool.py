#!/usr/bin/python3
"""
Temperature Conversion Tool

This script demonstrates the use of global variables in Python by implementing
a simple temperature conversion utility between Celsius and Fahrenheit.

The script defines two global variables to store the conversion factors:
- FAHRENHEIT_TO_CELSIUS_FACTOR (5/9): Used when converting from Fahrenheit to Celsius
- CELSIUS_TO_FAHRENHEIT_FACTOR (9/5): Used when converting from Celsius to Fahrenheit

These global variables are accessible within the conversion functions without needing
to be passed as parameters, demonstrating the concept of variable scope in Python.

The script provides a simple command-line interface for users to convert temperatures
between the two scales.

Requirements completed:
1. Define Global Conversion Factors:
   - FAHRENHEIT_TO_CELSIUS_FACTOR (5/9)
   - CELSIUS_TO_FAHRENHEIT_FACTOR (9/5)

2. Implement Conversion Functions:
   - convert_to_celsius(fahrenheit)
   - convert_to_fahrenheit(celsius)

3. User Interaction:
   - Prompt for temperature and unit
   - Call the appropriate conversion function
   - Display the converted temperature
   - Handle invalid input with error message
"""

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    # Use the global conversion factor
    # The formula is (F - 32) * (5/9)
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    # Use the global conversion factor
    # The formula is (C * 9/5) + 32
    return (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32

def main():
    """
    Main function to handle user interaction for temperature conversion
    """
    try:
        # Prompt the user for a temperature
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Ask for the unit (Celsius or Fahrenheit)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform the conversion based on the unit provided
        if unit == 'C':
            # Convert from Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            # Convert from Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            # Handle invalid unit input
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle invalid temperature input with the exact required message
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    # Execute the main function only when the script is run directly,
    # not when imported as a module in another script
    main()