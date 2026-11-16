# prova-p2

// disciplina: Paradigmas de programação // discente: Layla Pimentel de Sousa matricula: 20240005439
// disciplina: Paradigmas de programação // discente: sther thallyta sousa de souza matricula: 20240052967

// DEFINIÇÃO DAS CLASSES INICIO CLASSE ItemCompra ATRIBUTOS: nome: Caractere preco: Real

MÉTODO Construtor(nome_param: Caractere, preco_param: Real)
    nome <- nome_param
    preco <- preco_param
FIM MÉTODO

MÉTODO tem_desconto() -> Lógico
    RETORNE (preco > 50.0)
FIM MÉTODO

MÉTODO calcular_preco_final() -> Real
    SE tem_desconto() ENTÃO
        RETORNE preco * 0.9
    SENÃO
        RETORNE preco
    FIM SE
FIM MÉTODO
FIM CLASSE

CLASSE CarrinhoCompras ATRIBUTOS: itens: Lista de ItemCompra

MÉTODO Construtor()
    itens <- Lista Vazia
FIM MÉTODO

MÉTODO adicionar_item(item: ItemCompra)
    Adicione item ao final de itens
FIM MÉTODO

MÉTODO contar_itens_com_desconto() -> Inteiro
    contador <- 0
    PARA CADA item EM itens FAÇA
        SE item.tem_desconto() ENTÃO
            contador <- contador + 1
        FIM SE
    FIM PARA
    RETORNE contador
FIM MÉTODO

MÉTODO calcular_total() -> Real
    total <- 0.0
    PARA CADA item EM itens FAÇA
        total <- total + item.calcular_preco_final()
    FIM PARA
    RETORNE total
FIM MÉTODO

MÉTODO exibir_resumo()
    ESCREVA "--- RESUMO DA COMPRA ---"
    PARA CADA item EM itens FAÇA
        preco_final <- item.calcular_preco_final()
        SE item.tem_desconto() ENTÃO
            ESCREVA item.nome, ": R$ ", preco_final, " (10% de desconto aplicado)"
        SENÃO
            ESCREVA item.nome, ": R$ ", preco_final
        FIM SE
    FIM PARA

    ESCREVA "Itens com desconto: ", contar_itens_com_desconto()
    ESCREVA "Valor total da compra: R$ ", calcular_total()
FIM MÉTODO
FIM CLASSE

// ALGORITMO PRINCIPAL INÍCIO carrinho <- NOVO CarrinhoCompras() ENQUANTO Verdadeiro FAÇA ESCREVA "Digite o nome da compra (ou 'sair' para finalizar): " LEIA nome_item

    SE minúsculo(nome_item) = "sair" ENTÃO
        INTERROMPA
    FIM SE

    ESCREVA "Digite o preço de ", nome_item, ": R$ "
    LEIA preco_item
    
    novo_item <- NOVO ItemCompra(nome_item, preco_item)
    carrinho.adicionar_item(novo_item)
FIM ENQUANTO
carrinho.exibir_resumo()
FIM
