class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {
            "tipo": "Cliente",
            "nome": self.nome,
            "email": self.email
        }
