class CellPhone:
    #intialize variables
    def __init__(self, manu, modelnum, price):
        self.__manufacturer = manu
        self.__model_number = modelnum
        self.__retail_price = price
    def __set_manufact__(self, manu):
        #accepts argument for manufacturere
            self.__manufacturer = manu
        
    def __set_model__(self, model):
        #accepts arguemnt for model nunber
            self.__modelnum = model
        
    def __set_retail_price(self, price):
        #accepts arguemnt for retail price
            self.__retialprice = price
        
    def __get_manufact(self):
        #returns manufacturer
            return self.__manufacturer
    
    def __get_model(self):
        #returns model number
            return self.__modelnum
    
    def __get_retail_price(self):
        #returns retail price
            return self.__retialprice
        
        
        
        
        
        