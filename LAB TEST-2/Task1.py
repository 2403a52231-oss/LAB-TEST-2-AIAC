"""
Discount Calculator Program

This program provides functionality to calculate discounted prices based on user input.
It includes input validation and error handling to ensure robust operation.

Features:
- Interactive price and discount input from user
- Input validation for price (non-negative) and discount (0-100%)
- Error handling for invalid input types
- Clear user feedback and error messages
- Modular design with separate calculation and input functions

Author: [Your Name]
Date: [Current Date]
Version: 1.0

Usage:
    Run the script directly: python TASK1.py
    Or import functions: from TASK1 import apply_discount
"""

def apply_discount(price, discount):
    """
    Calculate the final price after applying a discount percentage.
    
    Args:
        price (float): The original price of the item (must be non-negative)
        discount (float): The discount percentage to apply (0-100)
    
    Returns:
        float: The final price after applying the discount
        
    Formula:
        final_price = price * (1 - discount / 100)
        
    Example:
        >>> apply_discount(100, 10)
        90.0
        >>> apply_discount(50, 25)
        37.5
    """
    return price * (1 - discount / 100)

def get_discounted_price_from_user():
    """
    Interactive function that prompts the user for price and discount, then calculates and displays the final price.
    
    This function:
    1. Prompts user to enter a price (validates it's non-negative)
    2. Prompts user to enter a discount percentage (validates it's between 0-100)
    3. Calculates the discounted price using apply_discount()
    4. Displays the result to the user
    
    Input Validation:
        - Price must be a valid number and non-negative
        - Discount must be a valid number between 0 and 100 (inclusive)
        - Handles ValueError for non-numeric input
    
    User Experience:
        - Provides clear error messages for invalid input
        - Continues prompting until valid input is received
        - Shows the final calculated price with discount percentage
    
    Example Usage:
        When run, the function will prompt:
        Enter the price (must be non-negative): 100
        Enter the discount percentage (0-100): 10
        Final price after 10.0% discount: 90.0
    """
    while True:
        try:
            # Get price input from user with validation
            price = float(input("Enter the price (must be non-negative): "))
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            
            # Get discount input from user with validation
            discount = float(input("Enter the discount percentage (0-100): "))
            if discount < 0 or discount > 100:
                print("Discount must be between 0 and 100. Please try again.")
                continue
            
            # If both inputs are valid, break out of the loop
            break
            
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter numeric values.")
    
    # Calculate the discounted price using the helper function
    discounted_price = apply_discount(price, discount)
    
    # Display the result to the user
    print(f"Final price after {discount}% discount: {discounted_price}")

# Example usage and main execution
if __name__ == "__main__":
    """
    Main execution block that runs when the script is executed directly.
    
    This ensures the interactive discount calculator only runs when the script
    is run directly (not when imported as a module).
    """
    print("Starting the discount calculator...")
    get_discounted_price_from_user()