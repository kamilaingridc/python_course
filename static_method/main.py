from random import randint


class Pessoa:
    # atributo de clase, está acessível na classe Pessoa
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

    @staticmethod  # não recebe classe e nem instância (não utiliza self ou cls)
    def gera_id():
        rand = randint(10000, 19999)
        return rand


pessoa1 = Pessoa('Luiz', 32)
pessoa1.get_ano_nascimento()

print(Pessoa.gera_id())
