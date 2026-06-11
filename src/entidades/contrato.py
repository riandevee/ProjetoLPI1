from entidades.obra import get_obras
from entidades.equipamento import Betoneira, Furadeira
from entidades.empreiteiro import get_empreiteiros

contratos = []

def get_contratos():return contratos

def inserir_contrato(contrato):
    if contrato not in contratos: contratos.append(contrato)
    else: print('Contrato já tem cadastro --- ' + str(contrato))

def set_contratos(contratos1):
    global contratos
    contratos = contratos1

def filtrar_contrato(data_mínima_contrato=None, prefixo_nome_empreiteiro=None,método_de_execução_obra=None, peso_máximo_equipamento=None, capacidade_mínima_betoneira=None, perfuração_furadeira=None):
    contratos_selecionados = []
    for contrato in contratos:
        if data_mínima_contrato is not None and contrato.data < data_mínima_contrato: continue
        excluir_contrato = False
        for equipamento in contrato.obra.equipamentos.values():
            if peso_máximo_equipamento is not None and equipamento.peso > peso_máximo_equipamento:
                excluir_contrato = True
                break
            if isinstance(equipamento, Betoneira):
                if capacidade_mínima_betoneira is not None and equipamento.capacidade < capacidade_mínima_betoneira:
                    excluir_contrato = True
                    break
            elif isinstance(equipamento, Furadeira):
                if perfuração_furadeira is not None and equipamento.perfuração != perfuração_furadeira:
                    excluir_contrato = True
                    break
        if excluir_contrato: continue
        if prefixo_nome_empreiteiro is not None and not contrato.empreiteiro.nome.startswith(prefixo_nome_empreiteiro): continue
        if método_de_execução_obra is not None and contrato.obra.execução != método_de_execução_obra: continue
        contratos_selecionados.append(contrato)
    return contratos_selecionados

def criar_contrato(data, id_obra, nome_empreiteiro):
    obra = get_obras().get(id_obra)
    if obra is None:
        print('Obra ' + id_obra + ' não cadastrada')
        return
    empreiteiro = get_empreiteiros().get(nome_empreiteiro)
    if empreiteiro is None:
        print('Empreiteiro ' + nome_empreiteiro + ' não cadastrado na Obra ' + id_obra)
        return
    contrato = Contrato(data,obra, empreiteiro)
    inserir_contrato(contrato)


class Contrato:
    def __init__(self,data, obra, empreiteiro):
        self.data = data
        self.obra = obra
        self.empreiteiro = empreiteiro

    def __str__(self,):
        formato = '{} {:<2} {} {:<31} {} {:<10} {}'
        contrato_formatado = formato.format(
            '|', self.obra.id,
            '|', self.empreiteiro.nome,
            '|', str(self.data),
            '|')
        return contrato_formatado

    def str_atributos_equipamento(self):
        atributos_equipamento_str = ''
        for índice, equipamento in enumerate(self.obra.equipamentos.values()):
            if(índice>0): atributos_equipamento_str += ' -- '
            atributos_equipamento_str += f'{equipamento.peso}kg' + ' - '
            if isinstance(equipamento, Betoneira): atributos_equipamento_str += str(equipamento.capacidade) + 'L'
            elif isinstance(equipamento, Furadeira): atributos_equipamento_str += str(equipamento.perfuração)
        return atributos_equipamento_str

    def str_filtro(self):
        formato = '{:<34} {} {:<11} {}'
        filtro_formatado = formato.format(self.str_atributos_equipamento(), '|', self.obra.execução, '|')
        return self.__str__() + filtro_formatado
