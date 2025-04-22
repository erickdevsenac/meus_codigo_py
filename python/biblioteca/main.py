class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def get_endereco(self):
        return self.endereco

    def get_telefone(self):
        return self.telefone

    def atualizar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

class Funcionario(Pessoa):
    def __init__(self, nome, endereco, telefone, matricula, cargo, salario):
        super().__init__(nome, endereco, telefone) # Chama o construtor da classe Pessoa
        self.matricula = matricula
        self.cargo = cargo
        self.salario = salario

    def get_matricula(self):
        return self.matricula

    def get_salario(self):
        return self.salario

    def registrar_emprestimo(self, aluno, livro):
        if livro.is_disponivel():
            livro.marcar_indisponivel()
            print(f"Empréstimo registrado para o aluno {aluno.nome} do livro '{livro.get_titulo()}'.")
        else:
            print(f"Livro '{livro.get_titulo()}' não está disponível para empréstimo.")

    def registrar_devolucao(self, aluno, livro):
        livro.marcar_disponivel()
        print(f"Devolução registrada do livro '{livro.get_titulo()}' pelo aluno {aluno.nome}.")


class Aluno(Pessoa):
    def __init__(self, nome, endereco, telefone, numero_aluno, curso):
        super().__init__(nome, endereco, telefone) # Chama o construtor da classe Pessoa
        self.numero_aluno = numero_aluno
        self.curso = curso

    def get_numero_aluno(self):
        return self.numero_aluno

    def solicitar_emprestimo(self, livro):
        if livro.is_disponivel():
            print(f"Aluno {self.nome} solicitou empréstimo do livro '{livro.get_titulo()}'. Aguardando aprovação do funcionário.")
        else:
            print(f"Livro '{livro.get_titulo()}' não está disponível para empréstimo.")

    def renovar_emprestimo(self, livro):
        print(f"Empréstimo do livro '{livro.get_titulo()}' renovado para o aluno {self.nome}.")


class Livro:
    def __init__(self, titulo, autor, isbn, ano_publicacao, editora, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.editora = editora
        self.numero_paginas = numero_paginas
        self.disponivel = True # Livro começa disponível por padrão

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def get_editora(self):
        return self.editora

    def get_numero_paginas(self):
        return self.numero_paginas

    def is_disponivel(self):
        return self.disponivel

    def marcar_indisponivel(self):
        self.disponivel = False

    def marcar_disponivel(self):
        self.disponivel = True

class Biblioteca:
    def __init__(self, nome_biblioteca, endereco_biblioteca):
        self.nome_biblioteca = nome_biblioteca
        self.endereco_biblioteca = endereco_biblioteca
        self.acervo_livros = [] # Lista para armazenar objetos Livro
        self.usuarios = [] # Lista para armazenar objetos Pessoa (Aluno ou Funcionario)


    def adicionar_livro(self, livro):
        self.acervo_livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' adicionado ao acervo da biblioteca {self.nome_biblioteca}.")

    def remover_livro(self, isbn):
        for livro in self.acervo_livros:
            if livro.get_isbn() == isbn:
                self.acervo_livros.remove(livro)
                print(f"Livro com ISBN {isbn} removido do acervo da biblioteca {self.nome_biblioteca}.")
                return
        print(f"Livro com ISBN {isbn} não encontrado no acervo.")

    def buscar_livro_por_titulo(self, titulo):
        livros_encontrados = []
        for livro in self.acervo_livros:
            if titulo.lower() in livro.get_titulo().lower(): # Busca insensível a maiúsculas e minúsculas
                livros_encontrados.append(livro)
        return livros_encontrados

    def emprestar_livro(self, aluno, livro):
        funcionario = Funcionario("Funcionario Padrão", "Endereço Funcionario", "Telefone Funcionario", "FP123", "Bibliotecário", 2500.00) # Simplificando, usando um funcionário padrão
        funcionario.registrar_emprestimo(aluno, livro) # Delega a ação para o funcionário

    def devolver_livro(self, aluno, livro):
        funcionario = Funcionario("Funcionario Padrão", "Endereço Funcionario", "Telefone Funcionario", "FP123", "Bibliotecário", 2500.00) # Simplificando, usando um funcionário padrão
        funcionario.registrar_devolucao(aluno, livro) # Delega a ação para o funcionário

    def adicionar_usuario(self, pessoa):
        self.usuarios.append(pessoa)
        print(f"Usuário {pessoa.nome} adicionado à biblioteca {self.nome_biblioteca}.")

    def remover_usuario(self, numero_identificacao):
        for usuario in self.usuarios:
            if isinstance(usuario, Aluno) and usuario.get_numero_aluno() == numero_identificacao:
                self.usuarios.remove(usuario)
                print(f"Aluno com número de aluno {numero_identificacao} removido da biblioteca {self.nome_biblioteca}.")
                return
            elif isinstance(usuario, Funcionario) and usuario.get_matricula() == numero_identificacao:
                self.usuarios.remove(usuario)
                print(f"Funcionário com matrícula {numero_identificacao} removido da biblioteca {self.nome_biblioteca}.")
                return
        print(f"Usuário com identificação {numero_identificacao} não encontrado na biblioteca.")


if __name__ == "__main__":
    biblioteca_central = Biblioteca("Biblioteca Central", "Rua Principal, 123")

    livro1 = Livro("Dom Casmurro", "Machado de Assis", "978-8532516576", 1899, "Editora XYZ", 250)
    livro2 = Livro("O Cortiço", "Aluísio Azevedo", "978-8572327050", 1890, "Editora ABC", 300)

    biblioteca_central.adicionar_livro(livro1)
    biblioteca_central.adicionar_livro(livro2)

    aluno1 = Aluno("Ana Silva", "Rua das Flores, 456", "11-9999-8888", "20231001", "Engenharia")
    funcionario1 = Funcionario("Carlos Souza", "Av. Brasil, 789", "11-8888-7777", "FC2001", "Bibliotecário", 3000.00)

    biblioteca_central.adicionar_usuario(aluno1)
    biblioteca_central.adicionar_usuario(funcionario1)

    print("\n--- Busca por livro ---")
    livros_dom_casmurro = biblioteca_central.buscar_livro_por_titulo("Dom Casmurro")
    for livro in livros_dom_casmurro:
        print(f"Livro encontrado: {livro.get_titulo()} por {livro.get_autor()}")

    print("\n--- Empréstimo de livro ---")
    biblioteca_central.emprestar_livro(aluno1, livro1) # Aluno Ana Silva tenta emprestar Dom Casmurro

    # print("\n--- Devolução de livro ---")
    # biblioteca_central.devolver_livro(aluno1, livro1)  # Aluno Ana Silva devolve Dom Casmurro

    print("\n--- Tentativa de empréstimo do mesmo livro novamente ---")
    biblioteca_central.emprestar_livro(aluno1, livro1) # Aluno Ana Silva tenta emprestar Dom Casmurro novamente