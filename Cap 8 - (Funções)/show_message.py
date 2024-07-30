message_list = ['Hello! Carlos', 'What you doing?', 'How are you?', 'Where do you go on the next vacation?']
new_list = []

def show_messages(message_list, new_list):
    while message_list:
        item = message_list.pop()
        new_list.append(item)
        print(item)
        
def sent_messages(new_list):
    for msg in new_list:
        print(f"Send: {msg.title()}")
        
print(f"Mensagens carregadas:\n")
show_messages(message_list, new_list)
print(f"\nMensagens enviadas:\n")
sent_messages(new_list[:])