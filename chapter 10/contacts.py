#program 10-18
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return f'Your name is {self.name} your phone is {self.phone} and your email is {self.email}.'
        
    def set_name(self, name):
        self.name = name
        return f'Name updated to {self.name}'
    
    def set_phone(self, phone):
        self.phone = phone
        return f'Phone updated to {self.phone}'
    
    def set_email(self, email):
        self.email = email
        return f'Email updated to {self.email}'
    
    def get_name(self):
        return f'Name: {self.name}'
    
    def get_phone(self):
        return f'Phone: {self.phone}'
    
    def get_email(self):
        return f'Email: {self.email}'
    