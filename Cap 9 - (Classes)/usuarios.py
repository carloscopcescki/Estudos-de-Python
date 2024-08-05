class User:
    def __init__(self, first_name, last_name, age, occupation) -> None:
        self.name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"O usuário se chama {self.name} {self.last_name}, trabalha de {self.occupation} e possui {self.age} anos")
        
    def greet_user(self):
        print(f"Seja bem vindo {self.name} {self.last_name}\n")
        print(f"Você logou {self.login_attempts} vezes hoje.")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
first_employee = User('Carlos', 'Daniel', 22, 'Operador de Produção')
first_employee.describe_user()
first_employee.increment_login_attempts()
first_employee.increment_login_attempts()
first_employee.increment_login_attempts()
first_employee.reset_login_attempts()
first_employee.greet_user()