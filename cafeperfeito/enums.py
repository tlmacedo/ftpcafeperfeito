# from enum import IntEnum
from cafeperfeito.utils import ChoiceEnum


class UNIDADE_COMERCIAL(ChoiceEnum):
    UNIDADE = 1
    PACOTE = 2
    PESO = 3
    FARDO = 4
    CAIXA = 5
    VIDRO = 6
    DUZIA = 7
    LATA = 8


class SITUACAO_NO_SISTEMA(ChoiceEnum):
    ATIVO = 1
    DESATIVADO = 2
    NEGOCIACAO = 3
    DESCONTINUADO = 4
    INCONSISTENTE = 5
    TERCEIROS = 6
    BAIXADA = 7


class TELEFONE_TIPO(ChoiceEnum):
    FIXO = 1
    CELULAR = 2
    FIXO_CELULAR = 3


class EMPRESA_TIPO(ChoiceEnum):
    FISICA = 1
    JURIDICA = 2


class EMPRESA_ISENTO_IE(ChoiceEnum):
    NISENTO = 0
    ISENTO = 1
