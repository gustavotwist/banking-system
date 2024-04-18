import textwrap


def menu():
    menu = """\n
    ----------------- MENU -------------------
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nc]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def