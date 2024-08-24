import json

# Sample JSON data (for demonstration purposes)
data = '''
{
  "users": [
    {
      "user_id": "1",
      "username": "john_doe",
      "password": "hashed_password_1",
      "transactions": [
        {"description": "Groceries", "amount": 100, "date": "2024-08-12", "category": "Food"}
      ]
    },
    {
      "user_id": "2",
      "username": "jane_smith",
      "password": "hashed_password_2",
      "transactions": [
        {"description": "Rent", "amount": 800, "date": "2024-08-01", "category": "Housing"},
        {"description": "Utilities", "amount": 150, "date": "2024-08-10", "category": "Housing"}
      ]
    },
    {
      "user_id": "3",
      "username": "alex_jones",
      "password": "hashed_password_3",
      "transactions": []
    },
    {
      "user_id": "4",
      "username": "chris_evans",
      "password": "hashed_password_4",
      "transactions": []
    }
  ]
}
'''

# Load JSON data into a Python dictionary
budget_data = json.loads(data)

# Function to display user's transactions and allow modification
def modify_transaction_date(username):
    # Find the user by username
    for user in budget_data['users']:
        if user['username'] == username:
            transactions = user['transactions']
            if not transactions:
                print(f"No transactions found for {username}.")
                return
            
            # Display available transactions
            print(f"Transactions for {username}:")
            for i, transaction in enumerate(transactions):
                print(f"{i + 1}. Description: {transaction['description']}, Date: {transaction['date']}, Amount: {transaction['amount']}, Category: {transaction['category']}")
            
            # Ask user to select a transaction by index
            try:
                choice = int(input(f"Select a transaction to modify (1-{len(transactions)}): "))
                if 1 <= choice <= len(transactions):
                    selected_transaction = transactions[choice - 1]
                    # Ask for new date
                    new_date = input("Enter the new date (YYYY-MM-DD): ")
                    # Update the date
                    selected_transaction['date'] = new_date
                    print("Transaction date updated successfully.")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            
            return

    print(f"User {username} not found.")

# Example: Modify a transaction date for "jane_smith"
username_to_find = "jane_smith"
modify_transaction_date(username_to_find)

# Output the updated JSON data (for demonstration)
print(json.dumps(budget_data, indent=2))
