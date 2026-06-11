equipamentos = {}

def get_equipamentos(): return equipamentos

def inserir_equipamento(equipamento):
    nome_equipamento = equipamento.nome
    if nome_equipamento not in equipamentos.keys(): equipamentos[nome_equipamento] = equipamento
    else: print('Equipamento ' + nome_equipamento + ' já tem cadastro')

def set_equipamentos(equipamentos1):
    global equipamentos
    equipamentos = equipamentos1

class Equipamento:
    def __init__(self, nome, valor, peso, disponível):
        self.nome = nome
        self.valor = valor
        self.peso = peso
        self.disponível = disponível

    def __str__(self):
        if self.disponível: disponível_str = 'disponível |'
        else: disponível_str = ''
        formato = '{} {:<37}  {} R$ {:<8.2f} {} {:<6}kg {} {:<22}'
        equipamento_formatado = formato.format(
            '|', self.nome,
            '|', self.valor,
            '|', self.peso,
            '|', disponível_str,
        )
        return equipamento_formatado

class Betoneira(Equipamento):
    def __init__(self, nome, valor, peso, disponível, capacidade, voltagem, tipo_betoneira):
        super().__init__(nome, valor, peso, disponível)
        self.capacidade = capacidade
        self.voltagem = voltagem
        self.tipo_betoneira = tipo_betoneira if tipo_betoneira in ('hobby', 'semi-profissional', 'profissional') else 'indefinido'

    def __str__(self):
        if self.disponível: disponível_str = 'disponível'
        else: disponível_str = ''
        formato = '{} {:<37} {} R$ {:<8.2f} {} {:<6} {} {:<17} {} {:<20} {} {:<10} {} {}'
        betoneira_formatada = formato.format(
            '|', self.nome,
            '|', self.valor,
            '|', f'{self.peso}kg',
            '|', self.tipo_betoneira,
            '|', f'{self.voltagem}V',
            '|', f'{self.capacidade}L',
            '|', disponível_str,

        )
        return betoneira_formatada

class Furadeira(Equipamento):
    def __init__(self, nome, valor, peso, disponível, perfuração, aplicação):
        super().__init__(nome,  valor, peso, disponível) 
        self.perfuração = perfuração if perfuração in ('Metal', 'Madeira', 'Alvenaria') else 'indefinido'
        self.aplicação = aplicação

    def __str__(self):
        if self.disponível: disponível_str = 'disponível'
        else: disponível_str = ''
        formato = '{} {:<37} {} R$ {:<8.2f} {} {:<6} {} {:<17} {} {:<20} {} {}'
        furadeira_formatada = formato.format(
            '|', self.nome,
            '|', self.valor,
            '|', f'{self.peso}kg',
            '|', self.perfuração,
            '|', self.aplicação,
            '|', disponível_str
        )
        return furadeira_formatada