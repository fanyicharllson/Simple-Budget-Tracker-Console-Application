import json
import os

# Function to get user data and save it to a JSON file
def save_user_data():
    # Collecting user data
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    # Creating a dictionary to store the data
    user_data = {
        "name": name,
        "age": age,
        "city": city
    }

    # Saving the data to a JSON file
    with open('user_data.json', 'a') as file:
        json.dump(user_data, file, indent=4)
    print("Data saved successfully.")

# Function to load and display user data from the JSON file
def load_user_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
            print("User Data:", user_data)
            
    else:
        print("No data found.")
        

        
# Function to edit user data
def edit_user_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        
        # Example: Changing the city
        new_city = input(f"Current city is {user_data['city']}. Enter new city: ")
        user_data['city'] = new_city
        
        with open('user_data.json', 'w') as file:
            json.dump(user_data, file, indent=4)
        print("Data updated successfully.")
    else:
        print("No data found.")

# Function to delete the JSON file
def delete_user_data():
    if os.path.exists('user_data.json'):
        os.remove('user_data.json')
        print("Data deleted successfully.")
    else:
        print("No data found to delete.")

# Main function to interact with the user
def main():
    while True:
        print("\nOptions:")
        print("1. Save User Data")
        print("2. Load User Data")
        print("3. Edit User Data")
        print("4. Delete User Data")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            save_user_data()
        elif choice == '2':
            load_user_data()
        elif choice == '3':
            edit_user_data()
        elif choice == '4':
            delete_user_data()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
