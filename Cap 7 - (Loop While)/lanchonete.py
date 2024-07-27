sandwich_orders = ['x-bancon', 'pastrami', 'misto quente', 'pastrami', 'x-burguer', 'pão de batata', 'pão de queijo', 'pastrami']
finished_orders = []

print("A lanchonete está sem pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sanduiche = sandwich_orders.pop()
    
    print(f"Preparando {sanduiche.title()}")
    finished_orders.append(sanduiche)

print("\nSanduiches preparados:") 
for finished_order in finished_orders:
    print(finished_order.title())