class Pessoa:
    # atributo de classe, está acessível na classe Pessoa
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano(cls, nome, ano):
        idade = cls.ano_atual - ano
        return cls(nome, idade)


pessoa1 = Pessoa('Luiz', 32)
pessoa1.get_ano_nascimento()
