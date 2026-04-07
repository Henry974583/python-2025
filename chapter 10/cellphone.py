class CellPhone:
    #intialize variables
    def __init__(self, manufact, model, price):
        self.manufact = manufact
        self.model = model
        self.price = price
        
    def __str__(self):
        return f"your phone is a {self.manufact} model {self.model} that retails for {self.price}"
        
    def __set_manufact__(self, manu):
        #accepts argument for manufacturere
            self.manufact = manufact
            return f'manufactuer updated to {self.manufact}.'
    def __set_model__(self, model):
        #accepts arguemnt for model nunber
            self.model = model
            return f'model updated to {self.model}'
            
    def __set_retail_price(self, price):
        #accepts arguemnt for retail price
            self.price = price
            return f'price updated to ${self.price}'
    def __get_manufact(self):
        #returns manufacturer
            return f'Phone manufacturer: {self.manufact}'
    
    def __get_model(self):
        #returns model number
            return f'Model number: {self.model}'
    
    def __get_retail_price(self):
        #returns retail price
            return f'retail price: {self.price}'
        
        
        
        
        
        