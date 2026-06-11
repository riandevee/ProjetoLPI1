from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from entidades.empreiteiro import get_empreiteiros, set_empreiteiros
from entidades.equipamento import get_equipamentos, set_equipamentos
from entidades.obra import get_obras, set_obras
from entidades.contrato import get_contratos, set_contratos
from interfaces.interface_textual import loop_opções_execução

nome_arquivo = 'conjuntos_globais'
def salvar_aplicação():
    contrato_equipamentos = []
    contrato_equipamentos.append(get_empreiteiros())
    contrato_equipamentos.append(get_equipamentos())
    contrato_equipamentos.append(get_obras())
    contrato_equipamentos.append(get_contratos())
    salvar_arquivo(nome_arquivo, objetos=contrato_equipamentos)

def recuperar_aplicação():
    contrato_equipamentos = carregar_arquivo(nome_arquivo)
    if contrato_equipamentos is not None:
        set_empreiteiros(contrato_equipamentos[0])
        set_equipamentos(contrato_equipamentos[1])
        set_obras(contrato_equipamentos[2])
        set_contratos(contrato_equipamentos[3])

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()

