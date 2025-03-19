import random

senha = ""

caracteres = "0123456789abcdefghijklmnopqrstuvwxyz,'`´^~!?@#$%¬&()_-+=/*{[]}<>."

for digito in range(8):
    aleatorio = random.choice(caracteres)
    senha += aleatorio

print("-" * 20)
print(senha)
print("-" * 20)
