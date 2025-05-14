cardapio = {
    'arroz': 25.50,
    'macarrão': 45,
    'churrasco': 80.90,
}

print("--- Cardápio ---")
for prato, preco in cardapio.items():
    print(f"➡️  {prato.upper()}")

while True:
    escolha = input("Escolha um prato (ou 'sair' para finalizar): ").lower().strip()
    if escolha == 'sair':
        break
    if escolha in cardapio:
        preco = cardapio[escolha]
        print(f"Você escolheu {escolha}. O preço é R${preco:.2f}")
    else:
        print("Prato inválido. Por favor, escolha um prato do cardápio.")

print("Obrigado, até a próxima 🧟‍♀️!")