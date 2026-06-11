empreiteiros = {}

def get_empreiteiros():return empreiteiros

def inserir_empreiteiro(empreiteiro):
    nome_empreiteiro = empreiteiro.nome
    if nome_empreiteiro not in empreiteiros.keys(): empreiteiros[nome_empreiteiro] = empreiteiro
    else: print('Empreiteiro ' + nome_empreiteiro + ' já tem cadastro')

def set_empreiteiros(empreiteiro1):
    global empreiteiros
    empreiteiros = empreiteiro1

class Empreiteiro:
    def __init__(self, nome, telefone, email, endereço):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereço = endereço

    def __str__(self):
        formato = '{} {:<31} {} {:<14} {} {:<32} {} {:<31} {}'
        empreiteiro_formatado = formato.format(
            '|', self.nome,
            '|', self.telefone,
            '|', self.email,
            '|', self.endereço,
            '|'
        )
        return empreiteiro_formatado