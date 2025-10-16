import json
from datetime import datetime, timedelta

# Lista principal de insumos
insumos = []

# -----------------------------
# FUNÇÃO AUXILIAR: INPUT NUMÉRICO POSITIVO
# -----------------------------
def input_float_positivo(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.lower() == "voltar":
            return "voltar"
        try:
            valor = float(valor)
            if valor <= 0:
                print("⚠ Valor deve ser maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("⚠ Entrada inválida. Digite um número válido.")

# -----------------------------
# FUNÇÃO AUXILIAR: INPUT DATA
# -----------------------------
def input_data(mensagem):
    while True:
        data_str = input(mensagem).strip()
        if data_str.lower() == "voltar":
            return "voltar"
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return data_str
        except ValueError:
            print("⚠ Data inválida! Use o formato AAAA-MM-DD.")

# -----------------------------
# FUNÇÃO AUXILIAR: INPUT NÃO VAZIO
# -----------------------------
def input_nao_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.lower() == "voltar":
            return "voltar"
        if valor == "":
            print("⚠ Campo não pode ficar vazio. Digite novamente.")
        else:
            return valor

# -----------------------------
# FUNÇÃO: CONFIRMAR AÇÃO (S/N)
# -----------------------------
def confirmar_acao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta == "voltar":
            return "voltar"
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("⚠ Entrada inválida! Digite apenas 'S' ou 'N'.")

# -----------------------------
# FUNÇÃO: ADICIONAR INSUMO NOVO
# -----------------------------
def adicionar_insumo_novo():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    while True:
        nome = input_nao_vazio("Nome do insumo: ")
        if nome == "voltar":
            return
        quantidade = input_float_positivo("Quantidade inicial: ")
        if quantidade == "voltar":
            return
        unidade = input_nao_vazio("Unidade de medida (ex: kg, L, pacotes): ")
        if unidade == "voltar":
            return
        validade = input_data("Validade (AAAA-MM-DD): ")
        if validade == "voltar":
            return
        fornecedor = input_nao_vazio("Fornecedor: ")
        if fornecedor == "voltar":
            return

        print("\n--- Confirme os dados do insumo ---")
        print(f"Nome: {nome}")
        print(f"Quantidade: {quantidade} {unidade}")
        print(f"Validade: {validade}")
        print(f"Fornecedor: {fornecedor}")

        confirmar = confirmar_acao("Deseja confirmar o cadastro? (S/N): ")
        if confirmar == "voltar":
            return
        if confirmar:
            insumo = {
                "nome": nome,
                "quantidade": quantidade,
                "unidade": unidade,
                "validade": validade,
                "fornecedor": fornecedor,
                "historico": [
                    {"tipo": "entrada", "quantidade": quantidade, "data": datetime.now().strftime("%Y-%m-%d")}
                ]
            }
            insumos.append(insumo)
            print("\n✅ Insumo adicionado com sucesso!\n")
            break
        else:
            print("Você pode alterar os dados antes de confirmar.\n")

# -----------------------------
# FUNÇÃO: ADICIONAR QUANTIDADE EXISTENTE
# -----------------------------
def adicionar_quantidade_existente():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    if not insumos:
        print("⚠ Não há insumos cadastrados.\n")
        return

    while True:
        print("\n--- Insumos disponíveis ---")
        for insumo in insumos:
            print(f"- {insumo['nome']} (Qtd: {insumo['quantidade']} {insumo['unidade']})")

        nome = input_nao_vazio("\nDigite o nome do insumo para adicionar quantidade: ")
        if nome == "voltar":
            return

        encontrado = False
        for insumo in insumos:
            if insumo['nome'].lower() == nome.lower():
                encontrado = True
                quantidade = input_float_positivo("Quantidade a adicionar: ")
                if quantidade == "voltar":
                    return
                print(f"\nVocê vai adicionar {quantidade} {insumo['unidade']} ao insumo {insumo['nome']}.")
                confirmar = confirmar_acao("Deseja confirmar? (S/N): ")
                if confirmar == "voltar":
                    return
                if confirmar:
                    insumo['quantidade'] += quantidade
                    insumo['historico'].append({
                        "tipo": "entrada",
                        "quantidade": quantidade,
                        "data": datetime.now().strftime("%Y-%m-%d")
                    })
                    print(f"✅ Quantidade atualizada! Nova quantidade: {insumo['quantidade']} {insumo['unidade']}\n")
                    return
                else:
                    break
        if not encontrado:
            print("⚠ Insumo não encontrado. Tente novamente.\n")

# -----------------------------
# FUNÇÃO: REGISTRAR SAÍDA
# -----------------------------
def registrar_saida():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    if not insumos:
        print("⚠ Não há insumos cadastrados.\n")
        return

    while True:
        print("\n--- Insumos disponíveis ---")
        for insumo in insumos:
            print(f"- {insumo['nome']} (Qtd: {insumo['quantidade']} {insumo['unidade']})")

        nome = input_nao_vazio("\nDigite o nome do insumo para saída: ")
        if nome == "voltar":
            return

        encontrado = False
        for insumo in insumos:
            if insumo['nome'].lower() == nome.lower():
                encontrado = True
                quantidade = input_float_positivo("Quantidade a retirar: ")
                if quantidade == "voltar":
                    return
                if quantidade > insumo['quantidade']:
                    print(f"⚠ Quantidade insuficiente! Estoque atual: {insumo['quantidade']} {insumo['unidade']}.")
                    continue
                print(f"\nVocê vai retirar {quantidade} {insumo['unidade']} do insumo {insumo['nome']}.")
                confirmar = confirmar_acao("Deseja confirmar a saída? (S/N): ")
                if confirmar == "voltar":
                    return
                if confirmar:
                    insumo['quantidade'] -= quantidade
                    insumo['historico'].append({
                        "tipo": "saida",
                        "quantidade": quantidade,
                        "data": datetime.now().strftime("%Y-%m-%d")
                    })
                    print(f"✅ Saída registrada! Quantidade atual: {insumo['quantidade']} {insumo['unidade']}\n")
                    return
                else:
                    break
        if not encontrado:
            print("⚠ Insumo não encontrado. Tente novamente.\n")

# -----------------------------
# FUNÇÃO: EDITAR INSUMO
# -----------------------------
def editar_insumo():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    if not insumos:
        print("⚠ Não há insumos cadastrados.\n")
        return

    while True:
        print("\n--- Insumos disponíveis ---")
        for insumo in insumos:
            print(f"- {insumo['nome']}")

        nome = input_nao_vazio("\nDigite o nome do insumo que deseja editar: ")
        if nome == "voltar":
            return

        encontrado = False
        for insumo in insumos:
            if insumo['nome'].lower() == nome.lower():
                encontrado = True
                while True:
                    print(f"\n--- Dados atuais do insumo '{insumo['nome']}' ---")
                    print(f"1. Validade: {insumo['validade']}")
                    print(f"2. Fornecedor: {insumo['fornecedor']}")
                    print("0. Voltar ao menu principal")

                    opcao = input("\nEscolha o dado que deseja alterar (1-2) ou 0 para voltar: ").strip()
                    if opcao == "0":
                        return
                    elif opcao == "1":
                        nova_validade = input_data("Digite a nova validade (AAAA-MM-DD): ")
                        if nova_validade == "voltar":
                            return
                        print(f"\nValidade antiga: {insumo['validade']} -> Nova validade: {nova_validade}")
                        confirmar = confirmar_acao("Deseja confirmar a alteração? (S/N): ")
                        if confirmar == "voltar":
                            return
                        if confirmar:
                            insumo['validade'] = nova_validade
                            print(f"✅ Validade do insumo '{insumo['nome']}' atualizada com sucesso!\n")
                        else:
                            print("❌ Alteração cancelada.\n")
                            break
                    elif opcao == "2":
                        novo_fornecedor = input_nao_vazio("Digite o novo fornecedor: ")
                        if novo_fornecedor == "voltar":
                            return
                        print(f"\nFornecedor antigo: {insumo['fornecedor']} -> Novo fornecedor: {novo_fornecedor}")
                        confirmar = confirmar_acao("Deseja confirmar a alteração? (S/N): ")
                        if confirmar == "voltar":
                            return
                        if confirmar:
                            insumo['fornecedor'] = novo_fornecedor
                            print(f"✅ Fornecedor do insumo '{insumo['nome']}' atualizado com sucesso!\n")
                        else:
                            print("❌ Alteração cancelada.\n")
                            break
                    else:
                        print("⚠ Opção inválida.")
                break
        if not encontrado:
            print("⚠ Insumo não encontrado.\n")

# -----------------------------
# FUNÇÃO: PESQUISAR INSUMO
# -----------------------------
def pesquisar_insumo():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    if not insumos:
        print("⚠ Não há insumos cadastrados.\n")
        return

    while True:
        nome = input_nao_vazio("Digite o nome do insumo para pesquisa: ")
        if nome == "voltar":
            return
        encontrado = False
        for insumo in insumos:
            if insumo['nome'].lower() == nome.lower():
                encontrado = True
                print("\n--- Dados do Insumo ---")
                print(f"Nome: {insumo['nome']}")
                print(f"Quantidade: {insumo['quantidade']} {insumo['unidade']}")
                print(f"Validade: {insumo['validade']}")
                print(f"Fornecedor: {insumo['fornecedor']}\n")
                return
        if not encontrado:
            print("⚠ Insumo não encontrado.\n")

# -----------------------------
# FUNÇÃO: EXCLUIR INSUMO
# -----------------------------
def excluir_insumo():
    print("\n💡 Digite 'voltar' a qualquer momento para retornar ao menu principal.\n")
    if not insumos:
        print("⚠ Não há insumos cadastrados.\n")
        return

    while True:
        print("\n--- Insumos disponíveis ---")
        for insumo in insumos:
            print(f"- {insumo['nome']}")

        nome = input_nao_vazio("\nDigite o nome do insumo que deseja excluir: ")
        if nome == "voltar":
            return
        encontrado = False

        for insumo in insumos:
            if insumo['nome'].lower() == nome.lower():
                encontrado = True
                print("\n--- Confirme os dados do insumo a ser excluído ---")
                print(f"Nome: {insumo['nome']}")
                print(f"Quantidade: {insumo['quantidade']} {insumo['unidade']}")
                print(f"Validade: {insumo['validade']}")
                print(f"Fornecedor: {insumo['fornecedor']}")
                confirmar = confirmar_acao("Tem certeza que deseja excluir este insumo? (S/N): ")
                if confirmar == "voltar":
                    return
                if confirmar:
                    insumos.remove(insumo)
                    print(f"✅ Insumo '{nome}' removido com sucesso!\n")
                    return
                else:
                    print("❌ Exclusão cancelada.\n")
                    return
        if not encontrado:
            print("⚠ Insumo não encontrado.\n")

# -----------------------------
# FUNÇÃO: LISTAR ESTOQUE
# -----------------------------
def listar_estoque():
    if not insumos:
        print("⚠ Nenhum insumo cadastrado.\n")
        return

    print("\n--- Estoque de Insumos ---")
    print(f"{'Nome':20} {'Qtd':>8} {'Unidade':10} {'Validade':12} {'Fornecedor':20}")
    print("-"*75)
    for insumo in insumos:
        print(f"{insumo['nome']:20} {insumo['quantidade']:>8} {insumo['unidade']:10} {insumo['validade']:12} {insumo['fornecedor']:20}")
    print()

# -----------------------------
# FUNÇÃO: GERAR RELATÓRIO JSON 30 DIAS
# -----------------------------
def gerar_relatorio_30_dias():
    hoje = datetime.now()
    limite = hoje - timedelta(days=30)
    relatorio = []

    for insumo in insumos:
        historico_recente = [h for h in insumo["historico"] if datetime.strptime(h["data"], "%Y-%m-%d") >= limite]
        if historico_recente:
            relatorio.append({"nome": insumo['nome'], "movimentacoes_30_dias": historico_recente})

    with open("relatorio_30_dias.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=4)

    print("✅ Relatório JSON dos últimos 30 dias gerado com sucesso!\n")

# -----------------------------
# NOVA FUNÇÃO: GERAR RELATÓRIO COMPLETO EM TXT
# -----------------------------
def gerar_relatorio_txt():
    if not insumos:
        print("⚠ Nenhum insumo cadastrado.\n")
        return

    with open("relatorio_completo.txt", "w", encoding="utf-8") as f:
        f.write("=== RELATÓRIO COMPLETO DE MOVIMENTAÇÕES DE INSUMOS ===\n\n")
        for insumo in insumos:
            f.write(f"Insumo: {insumo['nome']}\n")
            f.write(f"Quantidade atual: {insumo['quantidade']} {insumo['unidade']}\n")
            f.write(f"Validade: {insumo['validade']}\n")
            f.write(f"Fornecedor: {insumo['fornecedor']}\n")
            f.write("Histórico:\n")
            for h in insumo["historico"]:
                f.write(f"  - {h['data']} | {h['tipo'].capitalize()} | Quantidade: {h['quantidade']}\n")
            f.write("\n")
    print("✅ Relatório completo em TXT gerado com sucesso!\n")

# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    while True:
        print("""
🌾 SISTEMA DE ESTOQUE DE INSUMOS AGRÍCOLAS
1. Adicionar insumo novo
2. Adicionar quantidade a insumo existente
3. Registrar saída de insumo
4. Listar estoque completo
5. Pesquisar insumo
6. Gerar relatório JSON (últimos 30 dias)
7. Excluir insumo do estoque
8. Editar insumo existente
9. Gerar relatório completo em TXT
0. Sair
""")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            adicionar_insumo_novo()
        elif opcao == "2":
            adicionar_quantidade_existente()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            listar_estoque()
        elif opcao == "5":
            pesquisar_insumo()
        elif opcao == "6":
            gerar_relatorio_30_dias()
        elif opcao == "7":
            excluir_insumo()
        elif opcao == "8":
            editar_insumo()
        elif opcao == "9":
            gerar_relatorio_txt()
        elif opcao == "0":
            print("Saindo do sistema!")
            break
        else:
            print("⚠ Opção inválida. Digite novamente.\n")

# -----------------------------
# EXECUÇÃO DO PROGRAMA
# -----------------------------
menu()