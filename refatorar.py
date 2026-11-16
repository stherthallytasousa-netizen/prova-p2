class ItemCompra:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def tem_desconto(self) -> bool:
        return self.preco > 50.0

    def calcular_preco_final(self) -> float:
        if self.tem_desconto():
            return self.preco * 0.9
        return self.preco

class CarrinhoCompras:
    def __init__(self):
        self.itens: list[ItemCompra] = []

    def adicionar_item(self, item: ItemCompra) -> None:
        self.itens.append(item)

    def contar_itens_com_desconto(self) -> int:
        return sum(1 for item in self.itens if item.tem_desconto())

    def calcular_total(self) -> float:
        return sum(item.calcular_preco_final() for item in self.itens)

    def exibir_resumo(self) -> None:
        print("\n--- RESUMO DA COMPRA ---")
        for item in self.itens:
            preco_final = item.calcular_preco_final()
            if item.tem_desconto():
                print(f"- {item.nome}: R$ {preco_final:.2f} (10% de desconto aplicado)")
            else:
                print(f"- {item.nome}: R$ {preco_final:.2f}")
        print(f"\nItens com desconto: {self.contar_itens_com_desconto()}")
        print(f"Valor total da compra: R$ {self.calcular_total():.2f}")

if __name__ == "__main__":
    carrinho = CarrinhoCompras()

    while True:
        nome_item = input("Digite o nome da compra/produto (ou 'sair' para finalizar): ")
        if nome_item.lower() == "sair":
            break

        preco_item = float(input(f"Digite o preço de '{nome_item}': R$ "))
        novo_item = ItemCompra(nome_item, preco_item)
        carrinho.adicionar_item(novo_item)

    carrinho.exibir_resumo()