
import logging
import json
import os
from Clasess.transaction import Transaction
from ConfigLog.log import setting_logging


"""From the configuration file log,py"""
setting_logging(__name__, "user.log")




class User:
    def __init__(self, username=None, userId=None, password=None, income=None):
        self.__username = username
        self.__userId = userId
        self.__password = password
        self.__income = income
        self.logger = logging.getLogger(__name__)
    
    @property
    def getUsername(self):
        return self.__username
    
    @property
    def getUserId(self):
        return self.__userId
    
    @property
    def getPassword(self):
        return self.__password
    
    @property
    def getIncome(self):
        return self.__income
    
    #************************************************************************************************
    
      
    #************************************************************************************************      
    
    def menu(self):
        """Menu for budget tracker, asking the user to select from the menu below"""
        print("\n")
        self.logger.info("********************************")
        self.logger.info("*********WELCOME TO MENU********")
        self.logger.info("********************************")
        print("1) Add Transaction")
        print("2) Edit Transaction")
       # print("3) Delete Transaction")
        print("3) Summary Transaction")
        print("4) Exist")
  
        while True:
          try:
            choice = int(input("Enter your choice of Transaction(1-4): "))
            if choice == 1:
                   self.logger.info("\n")  
                   self.logger.debug('WANT TO ADD TRANSACTION===============')
                   print("\n")
                   description  = input("Enter your  transaction description:  ")
                   while True:
                         ammount = input("Enter the ammount you want to use for this transaction: ")
                         if ammount.isdigit():
                              ammount = int(ammount)
                              if ammount <=0:
                                    self.logger("\n")
                                    self.logger.warning("Amount Cannot be negative or lesser than or equal to 'ZERO'===== ")
                                    continue
               
                              else:
                                 break
                   
                      
                         else:
                           raise Exception ("Invalid ammount! Please Try again.")
           
          
                   date = input("Enter your date: ")
                   catergory = input("Enter your Catergory: ")
                   print("\n")
                   self.logger.info("To add transaction you entered, please enter your password below.")
                   
                   #Userpassword = input("Enter your password: ") #Asking user to enter password
                   
                   break
               
            #editing transaction****************************************************************
            elif choice == 2:
                self.logger.info("EDITING TRANSACTION******************")
                self.logger.info("\n")
                
                self.editTransaction()  #calling editing trasaction  
                  
               
           #************************************************************************************************
            # elif choice == 3:
            #     self.logger.debug("DELETING TRANSACTION******************")
            #     self.deleteTransaction() #calling deleting trasaction function ************************************************************************************************
            
            elif choice == 3:
                self.logger.info("SUMMARY TRANSACTION ********************************")
                self.viewSummaryTransaction()
            
            elif choice == 4:
                option = input("\n\tDo you really want to exit? (y/n): ").lower()
                if option == "y":
                    self.logger.info("Exit********************************")
                    exit()
                
                elif option == "n":
                    self.menu()
                
                else:
                    logging.error("Invalid Option! Please Try again") 
                    self.menu()       
            
            
          
          except Exception as e: 
            self.logger.exception("Invalid Choice! Try Again.")
            




        self.logger.info("PASSING USER ENTERED ATTREIBUTES TO THE TRANSACTION CLASS********************************")
        transactionObject = Transaction(description, ammount, date, catergory)
        self.addTransaction(transactionObject.transactions)
            
            
            
            
            
                    
  #************************************************************************************************ 
  
  
   
  #************************************************************************************************      
    
    def addingUserPersonalInfo(self):
        
        """This function is responsible for adding user name, id, password, and income information including transaction list where all transaction will be added"""
        
        primary_info = {
            "username": self.__username,
            "userId": self.__userId,
            "password": self.__password,
            "User budget Income": self.__income,
            "transactions": []
            
        }
        
        #Loading Json Data to Python Object=======================
        if os.path.exists("userDatabase.json"):
            
            self.logger.info("JSON FILE EXIST..........")
            
            with open("userDatabase.json", "r") as file:
                user_data = json.load(file)
            
            #Appending  new sign up user======================== 
            user_data["users"].append(primary_info)
            
            
            #Updating JSON data to include the newly signUp user========================
            with open("userDatabase.json", 'w') as file:
                json.dump(user_data, file, indent=4)
            self.logger.info("SIGN UP SUCCESSFUL..........")
            
            
            
            
            self.logger.info("Asking the wether he or she want to go the menu page..........")
            
            choice_menu = input("Do you want to go the menu? (y/n): ")
            if choice_menu == "y":
                #calling user menu in the menu function
                self.menu()
            
            elif choice_menu == "n":
                self.logger.error("Thankyou for signing up")
                exit()  
            
            else:
                self.logger.error("Invalid choice")
                exit()
        
        else:
            self.logger.error("JSON FILE NOT FOUND========........==========")        
                
        
     
     
     #************************************************************************************************  
     #************************************************************************************************ 
     
    def PASSWORDS(self):
        """Password function that will be inherited by functions that calls.
        This function ensures that the password that entered by the user is valid password
        """
        if os.path.exists("userDatabase.json"):
            self.logger.info("THIS JSON FILE IS FOUND")
            with open("userDatabase.json", "r") as file:
                user_data = json.load(file)
            
            while True:
                password_found = False
                
                user_password = input("\n\t\tEnter your password: ")
                
                for password in user_data["users"]:
                    if password["password"] == user_password:
                        self.logger.info("\n")
                        self.logger.info("VALID PASSWORD")
                        password_found = True
                        
                        return user_password
                        
                
                if not password_found:
                    self.logger.warning("OOPS INVALID PASSWORD!...")
                        
                    
                       
        
        else:
            self.logger.error("THIS JSON FILE IS NOT FOUND. PLEASE COME BACK LATER!")        
        
        
              
       
     #************************************************************************************************  
     #************************************************************************************************      
       
    
    def addTransaction(self, transaction):
        """adding transation """
        
        if os.path.exists("userDatabase.json"):
            self.logger.info("THIS JSON FILE IS FOUND")
            with open("userDatabase.json", "r") as file:
                user_data = json.load(file)
            
            
            #Asking the user to enter password before adding transaction
            adding_transaction_password = input("\n\tEnter your password to add transaction: ")
            
            password_found = False
            current_user = None
            
            for user in user_data["users"]:
                if user["password"] == adding_transaction_password:
                    self.logger.info("\nValid Password=======================")
                    password_found = True
                    current_user = user
                    break
            
            if not password_found:
                self.logger.error("\nInvalid Password. Please try again.")
                quit()
            
            if user["User budget Income"]  == 0.0:
                print("\n")
                print("Sorry we coudn't add your recent transaction because your income is $0. Please go back modify your income before continuing.")
                
                #asking user if he want to add his income
                modify_income = input(f"\n\tDear {user["username"]}, do you want to add your income now? (y/n): ").lower()
                if modify_income == 'y':
                    self.update_income()
                
                elif modify_income == 'n':
                     print("Returning to menu...") 
                     self.menu()
                
                else:
                    print("Invalid choice. Try again later")
                    self.menu()
                            
                    
                    
                    
            
            current_user["transactions"].append(transaction)
            
            #Telling the user the balance income
            
            amount_found = False
            list_amount = []
            total_amount = 0 
            for transaction in user["transactions"]:
                list_amount.append(transaction["amount"])
                amount_found = True
                 
            
            if not amount_found:
                print("\nNo valid amount. Please try again.")
                print("OOps")
            
                
            print(f"List of ammount {list_amount}")
            
            for amount in range(len(list_amount)):
                total_amount += list_amount[amount]
            
            print(f"Total amount: {total_amount}") 
            
            
            balance = user["User budget Income"]  - total_amount 
            
            user["User budget Income"] = balance
            
                   
            
            with open("userDatabase.json", "w") as file:
                json.dump(user_data, file, indent= 4)
            
            self.logger.info("\n\tTransaction added successfully!")
            
            
            print("\n")
            self.logger.info(f"Dear {user["username"]}, your balance income after adding transaction is {balance}")
            self.menu()
            
        else:
            self.logger.error("THIS JSON FILE NOT IS FOUND") 
            
            
               
    #************************************************************************************************  
    #************************************************************************************************
    
    
    """Modifications of income function"""
    def update_income(self):   #Not really working as exspected(update_income function)****************************************************************==================************************************************************************************************************************************************************************************************************
        with open("userDatabase.json", "r") as file:
            user_data = json.load(file)
            
        modify_income  = float(input("\n\tEnter new income: "))
        password = input("\nEnter password to modify income: ")
        
        found_income = False
        password_found = False
        for income in user_data["users"]:
            if income["password"] == password and  income["User budget Income"] == 0.0:
                password_found = True
                found_income = True
               
                print(f"Found Name {income["User budget Income"], income["username"]}")
                real_income = income["User budget Income"] + modify_income
                break
                
        
        if not found_income  and not password_found:
            print("\n")
            self.logger.error("Invalid password/ Your account is not $0")
            self.menu()
        
        income["User budget Income"] == real_income    
        
        self.logger.info(f"{income["username"]}, you income has been modified. New income is now {income["User budget Income"] }")  
        self.menu()      
        
        
        with open("userDatabase.json", "w") as file:
            json.dump(user_data, file, indent= 4) 
                          
         
    
    
    #************************************************************************************************  
    #************************************************************************************************
         
    
    def editTransaction(self):
         """Editing particular transaction entered """
         
         if os.path.exists("userDatabase.json"):
            self.logger.info("\n") 
            self.logger.info("THIS JSON FILE IS FOUND")
            with open("userDatabase.json", "r") as file:
                user_data = json.load(file)
            
            password = self.PASSWORDS()    

            
            for user in  user_data["users"]:
                if user["password"] == password:
                    self.logger.info("Correct password")
                    
                     
                    for i, transaction in enumerate(user["transactions"]):
                       print("\n")   
                       print(f"{i + 1}. Description: {transaction['description']}, Date: {transaction['date']}, Amount: {transaction['amount']}, Category: {transaction['category']}")
                    
                    #asking the user to select the transaction type to modify
                    try:
                                       
                      modify = int(input(f"\nSelect transaction index you want to modify(1 - {len(user["transactions"])}): "))
                      if 1 <= modify <= len(user["transactions"]):
                          
                          
                         #getting transactio list
                          transactions = user["transactions"]  
                          transactions_dict = transactions[modify -1] #Accessing dictionary inside transactions(JSON FILE)
                              
                          
                          while True: 
                              modify_description = input("\nEnter the description type you want to modify(Description,Date, Amount, Category):  ").lower()
                              
                              if modify_description == "description":
                                    
                                     print(f"\nOld description is {transactions_dict['description']}")
                                     new_description = input("\nEnter the new description:  ")
                                     
                                     transactions_dict['description'] = new_description
                                     
                                     self.logger.info(f"Dear {user["username"]}, your description has been updated successfully.")
                                     self.logger.info(f"\n\t Your new description is {transactions_dict['description']}")
                                     break 
                                     
                                     
                                     
                              elif modify_description == "date":
                                      print(f"\nOld Date is {transactions_dict['date']}")
                                      new_date = input("\nEnter the new date:  ")
                                     
                                      transactions_dict['date'] = new_date
                                     
                                      self.logger.info(f"Dear {user["username"]}, your description has been updated successfully.")
                                      self.logger.info(f"\n\t Your new description is {transactions_dict['date']}")
                                      break 
                                     
                                        
                              elif modify_description == "amount":
                                      print(f"\nOld Amount is {transactions_dict['amount']}")
                                      new_amount = input("\nEnter the new amount:  ")
                                     
                                      transactions_dict['amount'] = new_amount
                                     
                                      self.logger.info(f"Dear {user["username"]}, your description has been updated successfully.")
                                      self.logger.info(f"\n\t Your new description is {transactions_dict['amount']}")
                                      break 
                                     
                                  
                              elif modify_description == "category":
                                     print(f"\nOld Category is {transactions_dict['category']}")
                                     
                                     new_category = input("\nEnter the new category:  ")
                                     
                                     transactions_dict['category'] = new_category
                                     
                                     self.logger.info(f"Dear {user["username"]}, your description has been updated successfully.")
                                     self.logger.info(f"\n\t Your new description is {transactions_dict['category']}")
                                     break 
                                      
                                     
                              else:
                                  self.logger.error(f"{user["username"]} Invalid description type! Please try again.")
                                  continue 
                              
                          with open("userDatabase.json", "w") as file:
                              json.dump(user_data, file, indent= 4) 
                          
                          self.menu() #calling back the menu********************************    
                                  
                      else:
                          print("\n")
                          self.logger.error(f"{user["username"]}, you entered wrong index! Try again please")
                          self.menu() #calling back the menu********************************
                          
                                      
                    except Exception as e:
                        self.logger.error(f"Invald input. Please try again, ERROR TYPE: {e}")
                        self.menu()  #calling menu function if password is incorresct
                    
                
    
    #************************************************************************************************  
    #************************************************************************************************      
    
    # def deleteTransaction(self, Dtransaction):
    #     """Deleting transaction"""
    #     pass
    
    
    
    #************************************************************************************************  
     #************************************************************************************************      
    
    def viewSummaryTransaction(self):
        """Viewing transaction"""
        
        self.logger.info("To view transaction summary, please enter your password below.")
        
        #userpasword =  self.PASSWORDS()
        
        if os.path.exists("userDatabase.json"):
                self.logger.info("\n") 
                self.logger.info("THIS JSON FILE IS FOUND")
                with open("userDatabase.json", "r") as file:
                      user_data = json.load(file)
                
                      
                userpasword = input("Enter your password to view your summary transaction history: ")
                
                password_found = False      
                
                for user in user_data["users"]:
                    if user["password"] == userpasword:
                        self.logger.info(f"{user["username"]}, you entered the correct password.")
                        print("\n")
                        password_found = True
                        break
                
                if  not password_found:
                    self.logger.error(f"Oops, Dear{user["username"]}, you entered the wrong password. please try again.")
                    self.viewSummaryTransaction()
               
                if user["transactions"] == []:
                    print("\n")
                    self.logger.error(f"Oops,Dear{user["username"]}, you don't have any transactions added to your account.")
                    print("Follow infomation below to add Trasaction to your account")
                    self.menu()     
                
                self.logger.info(f"{user["username"]}, BELOW ARE YOUR LIST OF SUMMARY TRANSACTION****")
                print("\n")       
                for index, transaction in enumerate(user["transactions"]):
                     print(f"{index + 1}.  Description: {transaction['description']}, \n Transaction Date: {transaction['date']},\n Transaction Amount: {transaction['amount']},\n Transaction Category: {transaction['category']}")
                     print("\n")
                
                self.menu()
                     
                    
                    
                        
       