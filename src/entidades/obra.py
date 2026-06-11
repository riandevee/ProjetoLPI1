from entidades.equipamento import get_equipamentos

obras = {}

def get_obras():return obras

def inserir_obra(obra):
    id_obra = obra.id
    if id_obra not in obras.keys():obras[id_obra] = obra
    else:print('Obra ' + id_obra + ' já tem cadastro')

def set_obras(obras1):
    global obras
    obras = obras1

class Obra:
    def __init__(self, id, descrição, datas, execução):
        self.id = id
        self.descrição =  descrição
        self.datas = datas
        self.execução = execução
        self.equipamentos = {}


    def __str__(self):
        formato = "{} {:<4} {} {:<31} {} {:<11} {} {:<9} {}"
        obra_formatado = formato.format(
            '|', self.id,
            '|', self.descrição,
            '|', self.execução,
            '|', str(self.datas),
            '|'
        )
        return obra_formatado

    def inserir_equipamentos(self, chaves_equipamentos):
        for chave in chaves_equipamentos:
            if chave not in self.equipamentos: self.equipamentos[chave] = get_equipamentos()[chave]
            else:print('Equipamento ' + chave + ' já tem cadastro na Obra')
