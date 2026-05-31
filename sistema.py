# --- 1. FUNÇÕES ---
def calcular_total(prod):
    return sum(prod.values())


def produto_mais_caro(prod):
    maior_nome, maior_preco = "", -1.0
    for nome, preco in prod.items():
        if preco > maior_preco:
            maior_nome, maior_preco = nome, preco
    return maior_nome, maior_preco


def produto_mais_barato(prod):
    menor_nome, menor_preco = "", float("inf")
    for nome, preco in prod.items():
        if preco < menor_preco:
            menor_nome, menor_preco = nome, preco
    return menor_nome, menor_preco


#Cadastro de produtos
produtos = {}

print("Cadastro de 5 produtos")
for i in range(5):
    nome = input(f"\nProduto {i+1} - Nome: ")

    while True:
        try:
            preco = float(input("Preço: "))
            if preco >= 0:
                break
            print("Erro: Preço negativo.")
        except ValueError:
            print("Erro: Digite apenas números.")

    produtos[nome] = preco

#exibicao de resultados
total = calcular_total(produtos)
caro, p_caro = produto_mais_caro(produtos)
barato, p_barato = produto_mais_barato(produtos)

print("\n--- RESULTADOS DOS PRODUTOS CADASTRADOS ---")
print(f"Total: R$ {total:.2f}")
print(f"Mais Caro: {caro} (R$ {p_caro:.2f})")
print(f"Mais Barato: {barato} (R$ {p_barato:.2f})")

#sistema de busca
print("\nSistema de busca")
while True:
    busca = input("Digite o nome do produto para buscar (ou 'sair'): ")
    if busca.lower() == "sair":
        print("Produto encontrado")
        break

    resultado = produtos.get(busca, "Produto não encontrado")

    if resultado == "Produto não encontrado":
        print(resultado)
    else:
        print(f"Preço de {busca}: R$ {resultado:.2f}\n")