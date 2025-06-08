
"""
Explore Datetime Module

This script demonstrates the usage of Python's datetime module for:
1. Displaying the current date and time
2. Calculating future dates by adding a specified number of days

The script showcases how to work with dates, format them for display,
and perform date arithmetic using timedelta.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets and displays the current date and time.
    
    Returns:
        datetime: The current date and time object
    """
    # Get the current date and time
    current_date = datetime.now()
    # Print the current date and time in a formatted string
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(days, current_date):
    """
    Calculates a future date by adding a specified number of days to a given date.
    
    Args:
        days (int): Number of days to add to the current date
        current_date (datetime): The starting date for calculation
        
    Returns:
        datetime: The calculated future date
    """
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days)
    # Print the future date in a formatted string
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date

def main():
    """
    Main function that orchestrates the program flow.
    
    This function:
    1. Displays the current date and time by calling display_current_datetime()
    2. Prompts the user for a number of days to add
    3. Calculates and displays the future date by calling calculate_future_date()
    4. Handles any input validation errors
    """
    # Part 1: Display the current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    try:
        # Get the number of days from the user
        days = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(days, current_date)
    except ValueError:
        # Handle invalid input (non-integer)
        print("Error: Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Execute the main function when the script is run directly
    main()