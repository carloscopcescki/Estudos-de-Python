class User:
    def __init__(self, first_name, last_name, age, occupation) -> None:
        self.name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        
    def describe_user(self):
        print(f"O usuário se chama {self.name} {self.last_name}, trabalha de {self.occupation} e possui {self.age} anos")
        
    def greet_user(self):
        print(f"Seja bem vindo {self.name} {self.last_name}\n")
        
first_employee = User('Carlos', 'Daniel', 22, 'Operador de Produção')
first_employee.describe_user()
first_employee.greet_user()
        
second_employee = User('Anderson', 'Souza', 22, 'Telemarketing')
second_employee.describe_user()
second_employee.greet_user()
        
third_employee = User('Gabriel', 'Rodrigues', 22, 'Arquiteto')
third_employee.describe_user()
third_employee.greet_user()
        