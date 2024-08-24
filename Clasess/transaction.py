
class Transaction:
    def  __init__(self, description, ammount, date, catergory): 
        self._description = description
        self._ammount = ammount
        self._date = date
        self._catergory = catergory
        
        self.transactions = {
            "description": self._description,
            "amount": self._ammount,
            "date": self._date,
            "category": self._catergory
            
        } 
        
        
           
        