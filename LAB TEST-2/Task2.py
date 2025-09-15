"""
Simple Login System
"""

def login():
    """
    Interactive login function that prompts user for credentials and validates them.
    
    This function provides a simple login system that:
    1. Displays a predefined list of allowed users and their passwords
    2. Prompts the user to enter their username and password
    3. Validates the credentials against the allowed users dictionary
    4. Provides feedback on login success or failure
    
    Features:
        - Simple username/password authentication
        - Interactive user input prompts
        - Clear success/failure messages
        - Predefined user database for testing
    
    User Database:
        - alice: password123
        - bob: qwerty
        - charlie: letmein
    
    Returns:
        None: This function only prints messages and doesn't return values
    
    Example Usage:
        When called, the function will prompt:
        Enter your username: alice
        Enter your password: password123
        Login successful! Welcome, alice
        
    Security Note:
        This is a basic implementation for demonstration purposes.
        In production, passwords should be hashed and stored securely.
    """
    # Define allowed users and their passwords
    allowed_users = {
            "alice": "password123",
            "bob": "qwerty",
            "charlie": "letmein"
        }
    
    # Get username input from user
    username = input("Enter your username: ")
    
    # Get password input from user
    password = input("Enter your password: ")
    
    # Validate credentials and provide feedback
    if username in allowed_users and allowed_users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed! Invalid username or password.")

# Call the login function to run the program
if __name__ == "__main__":
    login()
            
