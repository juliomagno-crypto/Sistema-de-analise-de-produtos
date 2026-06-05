Sistema de Cadastro, Análise e Busca de Produtos
Este é um script simples em Python que simula um sistema de gerenciamento de produtos. O programa permite cadastrar 5 produtos com seus respectivos preços, realiza validações de entrada, calcula estatísticas básicas (total, produto mais caro e mais barato) e oferece uma ferramenta de busca em tempo real.

🚀 Funcionalidades
Cadastro Validado: Permite o cadastro de 5 produtos, garantindo que o usuário digite apenas valores numéricos positivos para os preços.

Análise de Dados: Identifica automaticamente o produto de maior valor, o de menor valor e calcula o custo total dos produtos cadastrados.

Sistema de Busca: Permite pesquisar o preço de qualquer produto cadastrado pelo nome, funcionando em um loop contínuo até que o usuário decida sair.

🛠️ Como o Código Funciona
O programa está dividido em três etapas principais:

1. Funções de Análise (produto_mais_caro e produto_mais_barato)
produto_mais_caro(prod): Percorre o dicionário de produtos. Utiliza uma lógica de comparação começando em -1.0 para encontrar e retornar o nome e o preço do item mais caro.

produto_mais_barato(prod): Semelhante à função anterior, mas inicia a comparação com float("inf") (infinito positivo) para garantir que qualquer preço cadastrado seja menor que o valor inicial, retornando o item mais barato.

2. Cadastro e Validação
O programa utiliza um loop for para repetir o cadastro 5 vezes. Dentro dele, há um loop while True combinado com try/except que trata dois possíveis erros de digitação:

Caso o usuário digite letras ou símbolos inválidos (ValueError).

Caso o usuário digite um preço negativo.

3. Exibição e Busca
Após o cadastro, o script exibe um resumo com o total gasto e os extremos de preço. Em seguida, entra no Sistema de Busca, onde o usuário pode digitar o nome de um produto para saber seu preço instantaneamente (usando o operador in para verificar a existência da chave no dicionário). O loop de busca é encerrado ao digitar "sair".
