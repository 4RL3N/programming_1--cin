num_listas = 3
tamanho_listas = 5

listas = {}

i = 0
while i < num_listas:
    nome_lista = f"lista_{i}"
    nova_lista = [0] * tamanho_listas
    listas[nome_lista] = nova_lista
    i += 1

print(listas)
