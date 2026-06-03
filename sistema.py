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


# Cadastro de produtos
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

# Exibição de resultados
total = calcular_total(produtos)
caro, p_caro = produto_mais_caro(produtos)
barato, p_barato = produto_mais_barato(produtos)

print("\n--- RESULTADOS DOS PRODUTOS CADASTRADOS ---")
print(f"Total: R$ {total:.2f}")
print(f"Mais Caro: {caro} (R$ {p_caro:.2f})")
print(f"Mais Barato: {barato} (R$ {p_barato:.2f})")

# Sistema de busca
print("\nSistema de busca")
while True:
    busca = input("Digite o nome do produto para buscar (ou 'sair'): ")
    
    # 1. Verifica primeiro se o usuário quer sair
    if busca.lower() == "sair":
        print("Saindo do sistema de busca. Até logo!")
        break

    # 2. Faz a busca no dicionário usando o operador 'in' ou .get()
    if busca in produtos:
        preco_encontrado = produtos[busca]
        print(f"Produto encontrado! Preço de {busca}: R$ {preco_encontrado:.2f}\n")
    else:
        print("Produto não encontrado.\n")
