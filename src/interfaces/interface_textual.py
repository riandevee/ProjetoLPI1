from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import converte_str_para_data
from entidades.obra import Obra, inserir_obra, get_obras
from entidades.equipamento import Equipamento, inserir_equipamento, get_equipamentos, Betoneira, Furadeira
from entidades.empreiteiro import Empreiteiro, inserir_empreiteiro, get_empreiteiros
from entidades.contrato import Contrato, filtrar_contrato, get_contratos, criar_contrato, inserir_contrato


def loop_opções_execução():
    sair_loop = False
    cabeçalho_empreiteiro = '\nEmpreiteiro : nome - telefone - email - endereço '
    cabeçalho_equipamento = '\nEquipamento : nome - valor - peso - Betoneira [tipo - voltagem - capacidade] | Furadeira [perfuração - aplicação] - disponível'
    cabeçalho_obra = '\nObra : id - descrição - execução - data'
    cabeçalho_obra_equipamentos = ('\nObra : id - descrição - execução - datas'
    + '\n - Equipamento : nome - tipo - valor - peso - Betoneira [voltagem - capacidade] | Furadeira [perfuração - aplicação]'
    + ' -  disponível')
    cabeçalho_contrato = '\nContrato : id da obra - nome do empreiteiro - data'
    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: Imprimir Todos / <ENTER>: Parar]', retornar=True)
        if operação == None: break
        elif operação in ('C', 'I'):
            if operação == 'I':
                opção_conteúdo = ler_str('E: Empreiteiro / Eq: Equipamento / O: Obra / C: Contrato / EO: Equipamentos nas Obra'
                + '/ <ENTER>: retornar]', retornar=True)
            else:opção_conteúdo = ler_str('E: Empreiteiro / Eq: Equipamento / O: Obra / C: Contrato / <ENTER>: retornar]', retornar=True)
            if opção_conteúdo == None: pass
            elif opção_conteúdo == 'E':
                if operação == 'C':loop_leitura_empreiteiros()
                imprimir_objetos(cabeçalho_empreiteiro,get_empreiteiros().values())
            elif opção_conteúdo == 'Eq':
                if operação == 'C':loop_leitura_equipamentos()
                imprimir_objetos(cabeçalho_equipamento,get_equipamentos().values())
            elif opção_conteúdo == 'O':
                if operação == 'C':loop_leitura_obras()
                imprimir_objetos(cabeçalho_obra, get_obras().values())
            elif opção_conteúdo == 'C':
                if operação == 'C':loop_leitura_contratos()
                imprimir_objetos(cabeçalho_contrato,get_contratos())
            elif operação == 'I' and opção_conteúdo == 'EO':
                imprimir_obra_equipamentos(cabeçalho_obra_equipamentos)
        elif operação == 'S': loop_seleção_contratos()
        elif operação == 'T':
            imprimir_objetos(cabeçalho_empreiteiro,get_empreiteiros().values())
            imprimir_objetos(cabeçalho_equipamento,get_equipamentos().values())
            imprimir_objetos(cabeçalho_obra, get_obras().values())
            imprimir_obra_equipamentos(cabeçalho_obra_equipamentos)
            imprimir_objetos(cabeçalho_contrato, get_contratos())
def imprimir_obra_equipamentos(cabeçalho_obra_equipamentos):
    print(cabeçalho_obra_equipamentos)
    for índice, obra in enumerate(get_obras().values()):
        imprimir_objeto(índice=índice, objeto_str=str(obra))
        imprimir_objetos_internos(obra.equipamentos.values())

def loop_leitura_empreiteiros():
    sair_loop = False
    print('--- Leitura de Dados dos Empreiteiros ---')
    while not sair_loop:
        empreiteiro = ler_empreiteiro()
        if empreiteiro is not None: inserir_empreiteiro((empreiteiro))
        else:print('-ERRO: na leitura do empreiteiro')
        sair_loop = ler_sair_loop('cadastro de empreiteiros')

def loop_leitura_equipamentos():
    sair_loop = False
    print('--- Leitura de Dados dos Equipamentos ---')
    while not sair_loop:
        equipamento = ler_equipamento()
        if equipamento is not None:
            inserir_equipamento(equipamento)
        else: print('- ERRO: na leitura do equipamento')
        sair_loop = ler_sair_loop('cadastro de equipamentos')

def loop_leitura_obras():
    sair_loop = False
    print('--- Leitura de Dados das Obras ---')
    while not sair_loop:
        obra = ler_obra()
        if obra is not None:
            inserir_obra(obra)
            loop_leitura_chaves_obras_equipamento(obra)
        else: print('- ERRO: na leitura do obra')
        sair_loop = ler_sair_loop('cadastro de obra')

def loop_leitura_chaves_obras_equipamento(obra):
    print('--- Leitura dos Índices das Chaves dos Equipamentos:' + obra.id + ' ---')
    imprimir_objetos('--- Lista de índice dos equipamento', get_equipamentos().keys())
    sequência_numeros = ler_str('Informar lista de índice dos equipamentos')
    lista_índice_chaves = sequência_numeros.split(',')
    chave_equipamentos = []
    lista_chaves = list(get_equipamentos().keys())
    for índice_str in lista_índice_chaves:
        índice = int(índice_str)
        chave_equipamentos.append(lista_chaves[índice -1])
    obra.inserir_equipamentos(chave_equipamentos)

def loop_leitura_contratos():
    sair_loop = False
    print('--- Leitura de Dados dos Contratos ---')
    while not sair_loop:
        contrato = ler_contrato()
        if contrato is not None: inserir_contrato(contrato)
        else: print(' - ERRO: na leitura do contrato')
        sair_loop = ler_sair_loop('cadastro de contrato')

def loop_seleção_contratos():
    sair_loop = False
    print('--- Seleção de Contratos ---')
    while not sair_loop:
        filtros, contratos_selecionados = selecionar_contrato()
        if filtros is not None: cabeçalho = ('Contrato : id da obra - nome do empreiteiro - data'
                                             + '\n - Equipamento : nome - tipo - valor - peso - Betoneira [voltagem - capacidade] | Furadeira [perfuração - aplicação]'
                                             + '\n - disponível')
        imprimir_objetos_associação_filtros(cabeçalho, contratos_selecionados, filtros)
        sair_loop = ler_sair_loop('seleçao de contratos')

def ler_sair_loop(loop):
    try:
        sair = input('--sair do loop de ' + loop + ' [S]: ')
        if sair == 'S': return True
    except IOError: pass
    return False

def ler_empreiteiro():
    nome = ler_str('nome do empreiteiro')
    if nome is None: return None
    telefone = ler_str('telefone do empreiteiro')
    if telefone is None: return None
    email = ler_str('email do empreiteiro')
    if email is None: return None
    endereço = ler_str('endereço do empreiteiro')
    if endereço is None: return None
    return Empreiteiro(nome,telefone,email, endereço)

def ler_obra():
    id = ler_str('id da obra')
    if id is None: return None
    descrição = ler_str('descrição da obra')
    if descrição is None: return None
    datas = ler_data('datas da obra')
    if datas is None: return None
    execução = ler_str('execução da obra')
    if execução is None: return None
    return Obra(id, descrição, datas, execução)

def ler_equipamento():
    nome = ler_str('nome do equipamento')
    if nome == None: return None
    valor = ler_float_positivo('valor do equipamento')
    if valor == None: return None
    peso = ler_int_positivo('peso dos equipamento')
    if peso == None: return None
    disponível = ler_bool('disponível do equipamento')
    if disponível == None: return None
    família_equipamento = ler_str('família do equipamento [B=Betoneira / F=Furadeira')
    if família_equipamento == 'B':
        capacidade = ler_int_positivo('capacidade da Betoneira')
        if capacidade == None: return None
        voltagem = ler_str('Voltagem do Betoneira')
        if voltagem == None: return None
        tipo_betoneira = ler_tipo_betoneira()
        if tipo_betoneira == None: return None
        return Betoneira(nome,valor,peso,disponível,capacidade,voltagem,tipo_betoneira)
    if família_equipamento == 'F':
        perfuração = ler_perfuração_furadeira('perfuração da Furadeira')
        if perfuração == None: return None
        aplicação = ler_str('Aplicação da Furadeira')
        if aplicação == None: return None
        return Furadeira(nome, valor, peso, disponível, perfuração, aplicação)
    else: return None

def ler_contrato():
    data = ler_data('data do contrato')
    if data is None: return None
    id_obra = ler_str('id da obra')
    if id_obra is None: return None
    nome_empreiteiro = ler_str('nome do empreiteiro')
    if nome_empreiteiro is None: return None
    return criar_contrato(data, id_obra, nome_empreiteiro)

def selecionar_contrato():
    filtros = '\nFiltros -- '
    data_mínima_contrato = ler_data('data mínima do contrato ',filtro=True)
    if data_mínima_contrato is not None: filtros += 'data mínima do contrato: ' + str(data_mínima_contrato)
    prefixo_nome_empreiteiro = ler_prefixo_nome_empreiteiro(filtro=True)
    if prefixo_nome_empreiteiro is not None: filtros += '- prefixo do nome empreiteiro: ' + str(prefixo_nome_empreiteiro)
    método_de_execução_obra = ler_obra_execução('metodo de execução obra ', filtro=True)
    if método_de_execução_obra is not None: filtros += ' - ' + método_de_execução_obra
    peso_máximo_equipamento = ler_int_positivo('peso do equipamento ', filtro=True)
    if  peso_máximo_equipamento is not None: filtros += ('- peso máximo dos equipamentos: ' + str(peso_máximo_equipamento))
    capacidade_mínima_betoneira = ler_int_positivo('capacidade da betoneira ', filtro=True)
    if capacidade_mínima_betoneira is not None: filtros += ' - capacidade mínima da betoneira: ' + str(capacidade_mínima_betoneira)
    perfuração_furadeira = ler_perfuração_furadeira('perfuração da furadeira ', filtro=True)
    if perfuração_furadeira is not None: filtros += '\n- perfuração da furadeira ' + str(perfuração_furadeira)
    contratos_selecionados = filtrar_contrato(data_mínima_contrato, prefixo_nome_empreiteiro, método_de_execução_obra, peso_máximo_equipamento, capacidade_mínima_betoneira, perfuração_furadeira)

    return filtros, contratos_selecionados

def ler_str(dado, filtro=False, retornar=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and (filtro or retornar): return None
        if len(string) > 0: return string
    except IOError: pass
    print('Erro na leitura do dado: ' + dado)
    return None

def ler_int_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: return None
        int_positivo = int(string)
        if int_positivo > 0: return int_positivo
    except ValueError:pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None

def ler_float_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: return None
        float_positivo = float(string)
        if float_positivo > 0.0: return float_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do flutuante positivo: ' + dado)
    return None

def ler_bool(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [S/N]: ')
        if len(string) == 0 and filtro: return None
        if string == 'S': return True
        elif string == 'N': return False
    except ValueError: pass
    print('Erro na leitura do booleano: ' + dado)
    return None

def ler_data(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [dd/mm/aaaa]: ')
        if len(string) == 0 and filtro: return None
        data = converte_str_para_data(string)
        if data is not None: return data
    except IOError: pass
    print('Erro na leitura da data: ' + dado)
    return None

def ler_prefixo_nome_empreiteiro(filtro=False):
    try:
        string = input(' - prefixo empreiteiro [C=Construções / S=Serviço]: ')
        if len(string) == 0 and filtro: return None
        if string == 'C': return 'Construções'
        if string == 'S': return  'Serviços'
    except ValueError: pass
    print('Erro na leitura do prefixo empreiteiro')
    return None

def ler_obra_execução(dado,filtro=False):
    try:
        string = input(' - execução da obra [H=Horizontal / V=Vertical]: ')
        if len(string) == 0 and filtro: return None
        if string == 'H': return 'Horizontal'
        if string == 'V': return 'Vertical'
    except ValueError: pass
    print('Erro na leitura da execução da obra')
    return None


def ler_tipo_betoneira(filtro=False):
    try:
        string = input(' - tipo da Betoneira [H=hobby / S=semi-profissional / P=profissional]: ')
        if len(string) == 0 and filtro: return None
        if string == 'H': return 'hobby'
        if string == 'S': return 'semi-profissional'
        if string == 'P': return 'profissional'
    except ValueError:
        pass
    print('Erro na leitura do tipo da betoneira')
    return None


def ler_perfuração_furadeira(dado,filtro=False):
    try:
        string = input(' - perfuração da Furadeira [M=Metal / Ma=Madeira / A=Alvenaria]: ')
        if len(string) == 0 and filtro: return None
        if string == 'M':  return 'Metal'
        if string == 'Ma': return 'Madeira'
        if string == 'A':  return 'Alvenaria'
    except ValueError:
        pass
    print('Erro na leitura da perfuração da furadeira')
    return None


def ler_peso_equipamento(filtro=False):
    try:
        string = input(' - peso máximo do equipamento (kg): ')
        if len(string) == 0 and filtro: return None
        peso = float(string)
        if peso > 0: return peso
    except ValueError:
        pass
    print('Erro na leitura do peso do equipamento')
    return None