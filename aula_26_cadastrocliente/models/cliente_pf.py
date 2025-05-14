class ClientePF:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf














# from .cliente import Cliente

# class ClientePessoaFisica(Cliente):
#     def __init__(self, nome, email, cpf):
#         super().__init__(nome, email)
#         self.cpf = cpf

#     def to_dict(self):
#         data = super().to_dict()
#         data.update({
#             "tipo": "Pessoa Física",
#             "cpf": self.cpf
#         })
#         return data
