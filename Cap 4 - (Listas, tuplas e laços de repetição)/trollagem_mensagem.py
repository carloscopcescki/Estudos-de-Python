import pyautogui as py
import random
import time

time.sleep(5)

msg = ['Teste', 'Teste2', 'Teste3', 'Teste4']

for i in range (50):
    mensagem = random.choice(msg)
    py.write(mensagem)
    py.press("Enter")
    