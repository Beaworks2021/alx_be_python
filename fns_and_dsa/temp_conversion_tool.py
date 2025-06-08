# temp_conversion_tool.py
# Temperature conversion tool demonstrating global variable scope

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
    float: Temperature converted to Celsius
    """
    # Use global conversion factor to convert F to C
    # Formula: (F - 32) * (5/9)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    float: Temperature converted to Fahrenheit
    """
    # Use global conversion factor to convert C to F
    # Formula: (C * 9/5) + 32
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature_input():
    """
    Get temperature input from user with validation.
    
    Returns:
    float: Valid temperature value
    
    Raises:
    ValueError: If user enters invalid numeric input
    """
    while True:
        try:
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            return temperature
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """
    Get temperature unit input from user with validation.
    
    Returns:
    str: Valid unit ('C' or 'F')
    """
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    print("=== Temperature Conversion Tool ===")
    print("Convert between Celsius and Fahrenheit")
    print(f"Using conversion factors:")
    print(f"Fahrenheit to Celsius factor: {FAHRENHEIT_TO_CELSIUS_FACTOR}")
    print(f"Celsius to Fahrenheit factor: {CELSIUS_TO_FAHRENHEIT_FACTOR}")
    print("-" * 40)
    
    try:
        # Get temperature input from user
        temperature = get_temperature_input()
        
        # Get unit input from user
        unit = get_unit_input()
        
        # Perform conversion based on input unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Ask if user wants to perform another conversion
    while True:
        another = input("\nWould you like to convert another temperature? (y/n): ").strip().lower()
        if another in ['y', 'yes']:
            print("-" * 40)
            main()  # Recursive call for another conversion
            break
        elif another in ['n', 'no']:
            print("Thank you for using the Temperature Conversion Tool!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()