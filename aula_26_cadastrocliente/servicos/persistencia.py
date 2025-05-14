import json
import os

ARQUIVO_DADOS = "clientes.json"

def salvar_cliente(cliente):
    dados = []
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []

    dados.append(cliente.to_dict())

    with open(ARQUIVO_DADOS, 'w') as f:
        json.dump(dados, f, indent=4)
