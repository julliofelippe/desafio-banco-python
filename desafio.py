def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()

    usuario_existente = any(u["cpf"] == cpf for u in usuarios)

    if usuario_existente:
        print("Operação falhou! Já existe um usuário com esse CPF.")
        return usuarios

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro - número - bairro - cidade/sigla do estado): ").strip()

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")
    return usuarios


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()

    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario:
        print(f"Conta criada com sucesso para {usuario['nome']}!")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
    else:
        print("Usuário não encontrado! Operação falhou.")
        return None
    

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=========== CONTAS CADASTRADAS ===========")
    for conta in contas:
        linha = f"""
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
        print(linha)
    print("==========================================")


def sair():
    print("Saindo do sistema... Obrigado por utilizar nosso banco!")
    exit()


def main():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            usuarios = criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao =="l":
            listar_contas(contas)

        elif opcao == "q":
            sair()

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
