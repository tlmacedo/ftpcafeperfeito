from enum import IntEnum


class SituacaoNoSistema(IntEnum):
    ATIVO = 1
    DESATIVADO = 2
    NEGOCIACAO = 3
    DESCONTINUADO = 4
    INCONSISTENTE = 5
    TERCEIROS = 6
    BAIXADA = 7


class TelefoneTipo(IntEnum):
    FIXO = 1
    CELULAR = 2
    FIXO_CELULAR = 3


class EmpresaTipo(IntEnum):
    FISICA = 1
    JURIDICA = 2


class EmpresaIsentoIE(IntEnum):
    NISENTO = 0
    ISENTO = 1
