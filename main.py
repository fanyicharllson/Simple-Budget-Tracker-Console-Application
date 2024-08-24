"""Importing Modules"""
import logging
import json
from Clasess.userU import User
from ConfigLog.log import setting_logging



"""setting up logging for this main file"""
setting_logging(__name__, "main.log")
logger = logging.getLogger(__name__)



def sub_main(name, id, password, income): 
   """sub main function calling the user class and passing in the inputs entered by the user"""
   
   user_object = User(name, id, password, income)
   user_object.addingUserPersonalInfo()

#  if os.path.exists("userDatabase.json"):
#       with open("userDatabase.json", "r") as file:


def signIn(signIn_password ):
   """Sign in function""" 
   with open("userDatabase.json", "r") as file:
      user_data  = json.load(file) 
  
   # Flag to check if the password was found
   password_found = False    
      
   for user in user_data["users"]:
    if user["password"] == signIn_password:
        logger.info("CORRECT PASSWORD====================")
        password_found = True
        # Calling the user class and performing further operations
        userObj = User()
        userObj.menu()
        break  # Exit the loop since the correct password was found 
   
   if not password_found:
     logger.warning("INCORRECT PASSWORD! PLEASE TRY AGAIN LATER")
     quit()        
              
      

#================================================================================
#| MAIN FUNCTION                                                                |
#================================================================================  

 
def main():
    """Main function """
    
    logger.info("BUDGET TRACKER APPLICATION STARTED......")
    print("\n")
    logger.info("WELCOME TO YOUR BUDGET TRACKER APPLICATION")
    
    while True:
    
       print("1) Sign Up")
       print("2) Sign In")
       print("3) Sign Out")
       
    
       choice = input("Enter your option from above(1-2): ")
       if choice.isdigit():
          choice = int(choice)
          
          if choice == 1:
             logger.info(" USER SIGNING UP...")
             
                  
             name = input("\nEnter your username: ")
             user_id = input("Enter your id: ")
             password = input("Enter your password: ")
             income  = input("Enter your Budget income: $ ")
             if income.isdigit():
                real_income = float(income)
             elif income.isalpha():
                logger.warning("SORRY YOUR CANNOT BE WORD OR ALPHABET, PLEASE TRY AGAIN")
                main()
             else:
                logger.error("Invalid income!")
                main()      
                
             print("\n")
             
             logger.info("CALLING SUB MAIN FUNCTION NOW IN USER.PY ........")
             
             sub_main(name, user_id, password, real_income)
             
             
             
            
          elif choice == 2:
             signIn_password = input("Enter password to sign in:  ")
             signIn(signIn_password)
         
          elif choice == 3:
              logger.info("SIGHNING OUT========____========")
              
              option = input("\n\tAre you sure you want to Sign Out? (y/n): ")
              if option == "y":
                 logger.debug("EXISTING.....")
                 exit()
              elif option == "n":
                 main()
              
              else:
                 logger.error("Invalid Option! Please choose the right option.")
                 main()
        
          else:
              logger.error("Invalid choice. Please Try again.")


if __name__ == "__main__":
   main()
                 
      