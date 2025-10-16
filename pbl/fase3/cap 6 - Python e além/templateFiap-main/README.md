# 🌾 Sistema de Estoque de Insumos Agrícolas  

Este projeto faz parte de uma aplicação voltada para o agronegócio, com foco na **gestão de insumos agrícolas** — produtos essenciais usados na produção rural, como fertilizantes, sementes, defensivos, rações e outros materiais de apoio.

O sistema foi desenvolvido em **Python** e tem como objetivo **automatizar o controle de estoque de insumos** em propriedades agrícolas, cooperativas ou empresas do setor. Ele permite o registro, edição e monitoramento das entradas e saídas de insumos, facilitando o controle logístico e evitando desperdícios.

## 🧩 Descrição do Problema

No agronegócio, a gestão de insumos agrícolas é essencial para garantir produtividade e reduzir desperdícios. Entretanto, muitos produtores rurais ainda realizam esse controle manualmente, utilizando planilhas ou registros físicos. Isso gera problemas como:

- Falta de rastreabilidade de fornecedores  
- Perda de insumos por validade vencida  
- Dificuldade em calcular reposições  
- Falhas em relatórios e controle de custos  

Esses desafios afetam diretamente a eficiência operacional e o planejamento produtivo das propriedades rurais.

## 💡 Proposta de Solução

O sistema foi criado para digitalizar e automatizar a **gestão de insumos agrícolas**, permitindo um controle mais eficiente e confiável. Ele possibilita:

- Registro completo de cada insumo (nome, unidade, validade, fornecedor)  
- Controle de entradas e saídas de estoque  
- Edição e exclusão de registros  
- Geração automática de relatórios em **JSON** e **TXT**  

Com isso, o sistema promove **rastreamento, economia e precisão** no controle de recursos agrícolas.

## 🚜 Contexto no Agronegócio

O projeto está inserido no contexto da **gestão operacional agrícola**, mais especificamente na organização de **estoques de insumos** usados em lavouras e criações.

Ele permite:
- Controlar **quantidade, validade e fornecedor** de cada produto  
- Registrar movimentações de **entrada e saída**  
- Gerar **relatórios automáticos** para auditorias e planejamento  

Essa solução ajuda produtores, técnicos e engenheiros agrônomos a manterem estoques **organizados e atualizados**, dentro dos princípios da **Agricultura 4.0**.

## ⚙️ Funcionalidades Principais

- 📦 Adicionar e editar insumos agrícolas  
- ➕ Registrar entradas e ➖ saídas de estoque  
- 📅 Controlar validade e fornecedor  
- 🔍 Pesquisar insumos específicos  
- 🧾 Gerar relatórios automáticos  
  - JSON – movimentações dos últimos 30 dias  
  - TXT – histórico completo e estoque atual  

## 🧠 Estrutura do Sistema

O sistema é modular, organizado em funções que tornam o código fácil de entender e manter.

| Função | Descrição |
|--------|------------|
| `adicionar_insumo_novo()` | Cadastra um novo insumo |
| `adicionar_quantidade_existente()` | Adiciona quantidade a um insumo já existente |
| `registrar_saida()` | Registra saídas e atualiza o estoque |
| `editar_insumo()` | Permite editar validade e fornecedor |
| `listar_estoque()` | Exibe todos os insumos cadastrados |
| `pesquisar_insumo()` | Busca um insumo pelo nome |
| `excluir_insumo()` | Remove um insumo do estoque |
| `gerar_relatorio_30_dias()` | Cria relatório JSON dos últimos 30 dias |
| `gerar_relatorio_txt()` | Gera relatório completo em TXT |
| `menu()` | Interface principal de interação com o usuário |

## 🧰 Tecnologias e Bibliotecas Usadas

| Tecnologia / Biblioteca | Finalidade |
|--------------------------|-------------|
| **Python 3.x** | Linguagem principal de desenvolvimento |
| **json** | Geração e manipulação de relatórios estruturados |
| **datetime** | Controle de datas, validade e histórico de movimentações |
| **TXT (arquivo texto)** | Geração de relatórios completos e legíveis |
| **Funções customizadas** | Validação de entrada e controle de fluxo |

## 🌱 Aplicação Prática

Este sistema pode ser usado em:
- Fazendas, cooperativas e armazéns agrícolas  
- Projetos de **Agricultura 4.0** e **IoT agrícola**  
- Treinamentos técnicos de **gestão rural** e **controle logístico agrícola**  

Com pequenas adaptações, ele pode ser expandido para bancos de dados, dashboards e integração com sensores IoT.

## 🚀 Execução

### Requisitos
- Python 3.8 ou superior

### Passos para executar o sistema

1. Salve o código em um arquivo chamado:
   ```
   estoque_insumos_agricolas.py
   ```
2. Abra o terminal na pasta onde o arquivo está salvo.  
3. Execute o comando:
   ```bash
   python estoque_insumos_agricolas.py
   ```
4. O menu principal será exibido:
   ```
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
   ```

5. Escolha a opção desejada e siga as instruções exibidas.

## 💾 Saídas Geradas

Durante a execução, o sistema gera automaticamente relatórios que auxiliam no controle e na análise de estoque:

| Arquivo | Formato | Descrição |
|----------|----------|------------|
| `relatorio_30_dias.json` | JSON | Movimentações (entradas/saídas) dos últimos 30 dias |
| `relatorio_completo.txt` | TXT | Histórico completo de insumos e movimentações |

Esses relatórios são úteis para auditorias, controle de validade e planejamento de compras.

## 🧩 Benefícios da Solução

- Elimina controles manuais e planilhas  
- Reduz erros e perdas por vencimento  
- Facilita o rastreamento de fornecedores  
- Automatiza relatórios e histórico de movimentações  
- Promove a digitalização do agronegócio e a eficiência na gestão
