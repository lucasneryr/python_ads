linha = "=" * 20

produtos = [
    {
        "nome": "Notebook",
        "preco": 2500.00,
        "quantidade": 10
    },
    {
        "nome": "Smartphone",
        "preco": 1500.00,
        "quantidade": 20
    },
    {
        "nome": "Tablet",
        "preco": 800.00,
        "quantidade": 15
    }
]

while True:
    print(f"\n{linha} MENU DE NAVEGAÇÃO {linha}\n"
        "1 - Visualizar Estoque Atual\n"
        "2 - Registrar Entrada de Produto\n"
        "3 - Registrar Saída de Produto\n"
        "4 - Sair do Sistema\n"
        f"{linha*2}\n")
    escolha_menu = input("Selecione uma opção: ")

    if (escolha_menu == "1"):
        print(f"{linha}ESTOQUE{linha}\n")
        for p in range(len(produtos)):
            produto = produtos[p] #esta variavel serve para evitar a repetição de produtos[p] na linha abaixo
            print(f"{p+1}. Nome: {produto['nome']} | Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
    elif (escolha_menu == "2"):
        print(f"\n{linha}ADICIONAR PRODUTO{linha}")
        print("Produtos: ", [produto['nome'] for produto in produtos])
        while True:
            encontrado = False #caso o produto seja encontrado, este valor mudará para verdadeiro para que o loop possa ser encerrado
            nome_produto = input("\nNome do produto: ")
            for produto in produtos:
                if nome_produto == produto['nome']:
                    quantidade_inserida = int(input("\nQuantidade: "))
                    produto['quantidade'] += quantidade_inserida
                    print("PRODUTO ADICIONADO!")
                    encontrado = True
                    break
                else:
                    print("Produto não encontrado!")
            if encontrado:
                break
    elif (escolha_menu == "3"):
        print(f"{linha}SAÍDA DE PRODUTO{linha}\n")
        print("Produtos: ", [produto['nome'] for produto in produtos]) 
        retirado = False
        produto_retirado = input("\nProduto a ser retirado: ")
        for produto in produtos:
            if produto_retirado == produto['nome']:
                quantidade_retirada = int(input("\nQuantidade a ser retirada: "))
                if quantidade_retirada <= produto['quantidade']: #verifica se o produto tem quantidade suficiente para atender à demanda
                    produto['quantidade'] -= quantidade_retirada
                    retirado = True 
                    break
                else:
                    print("Estoque insuficiente")
            else:
                print("Produto não encontrado.")
            if retirado:
                break
    elif (escolha_menu == "4"):
        print(f"Saindo do sistema...\n")
        break    
    else:
        print("Opção inválida...")
