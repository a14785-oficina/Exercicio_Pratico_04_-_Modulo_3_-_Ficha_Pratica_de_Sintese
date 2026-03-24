**Relatório Breve: Organização do Programa por Funções**
**Contexto:** 10.º Ano | Programação e Sistemas de Informação (PSI) | Python

---

## 1. Introdução

O programa desenvolvido consiste num sistema de **Gestão de Stock** para materiais escolares, implementado em Python. A versão entregue representa uma evolução significativa relativamente ao código original, demonstrando como as funções permitem não apenas organizar o código, mas também facilitar a implementação de melhorias estruturais e validações robustas.

## 2. Como as Funções Organizam o Programa

### 2.1 Modularidade e Separação de Responsabilidades

O programa está dividido em **seis funções principais**, cada uma com uma responsabilidade única e bem definida:

- **`adicionar_material(stock)`** – Regista novos materiais com validação de dados (impede quantidades negativas e verifica duplicados)
- **`consultar_stock(stock)`** – Permite pesquisar o stock de um material específico
- **`atualizar_stock(stock)`** – Gerencia a adição ou remoção de quantidades, com controlo de erros (ex: impede remover mais do que existe em stock)
- **`exibir_stock(stock)`** – Apresenta uma tabela formatada com o estado geral de todos os materiais
- **`file_export(stock)`** – **Melhoria adicionada:** Exporta os dados para um ficheiro `.txt` com data/hora no nome, permitindo backup e análise posterior
- **`main()`** – Função principal que coordena o fluxo do programa, apresentando o menu e direcionando para as funções adequadas conforme a escolha do utilizador

### 2.2 Benefícios da Organização por Funções

1. **Reutilização de Código:** A estrutura `stock` (dicionário) é passada como argumento entre funções, evitando variáveis globais e permitindo que cada função opere sobre os mesmos dados de forma organizada.

2. **Facilidade de Manutenção:** Como demonstrado nas capturas de ecrã, quando se adicionou a funcionalidade de exportação (`file_export`), foi necessário apenas criar uma nova função independente e adicionar uma opão no menu principal, sem alterar as restantes funções existentes.

3. **Legibilidade:** O código torna-se autoexplicativo. O nome de cada função indica claramente a sua função (ex: `consultar_stock` consulta stock), facilitando a compreensão para alunos e professores.

4. **Testabilidade:** Cada função pode ser testada individualmente. Por exemplo, na captura de ecrã 02.03, verifica-se que a função `atualizar_stock` rejeita valores negativos, demonstrando que as validações funcionam corretamente de forma isolada.

## 3. Evolução do Programa: Original vs. Melhorado

Analisando os comentários no código-fonte que indicam as secções "Original", identificam-se melhorias cruciais implementadas através da estrutura por funções:

| Aspeto | Versão Original | Versão Melhorada (Entregue) |
|--------|----------------|---------------------------|
| **Validação de Entrada** | Conversão direta de `int(input())` causava erros se o utilizador inserisse texto | Utilização de `try-except` para capturar `ValueError` e mensagens amigáveis |
| **Quantidades Negativas** | Aceitava valores negativos (lógica incoerente) | Verificação `if quantidade < 0` com retorno imediato da função |
| **Persistência de Dados** | Não existia | Nova função `file_export()` gera ficheiros com timestamp (ex: `2026.03.17.09.25.31-Stock_Export.txt`) |
| **Feedback ao Utilizador** | Mensagens básicas | Mensagens contextuais (ex: "Cobre adicionado com sucesso!", "Erro: Quantidade não pode ser negativa!") |

## 4. Sugestões de Melhoria Futuras (Nível 10.º Ano)

Para evoluções posteriores do projeto, recomenda-se:

1. **Funções de Validação Reutilizáveis:** Criar funções auxiliares como `validar_numero_positivo()` ou `material_existe()` para evitar repetição de código nas funções `adicionar_material` e `atualizar_stock`.

2. **Constantes para o Menu:** Definir constantes (ex: `OPCAO_ADICIONAR = "1"`) para tornar o código da função `main()` mais robusto e legível.

3. **Documentação Docstring:** Adicionar docstrings às funções para explicar parâmetros (ex: `:param stock: Dicionário com materiais e quantidades`), prática profissional importante para documentação técnica.

4. **Tratamento de Case-Insensitive:** Embora `.capitalize()` seja usado, uma função normalizadora de input garantiria consistência total (ex: "cobre", "COBRE" e "Cobre" serem tratados igualmente).

5. **Função de Importação:** Complementar `file_export()` com uma função `importar_stock()` para carregar dados previamente guardados, demonstrando manipulação completa de ficheiros.

## 5. Conclusão

As funções transformaram um script linear numa aplicação modular e robusta. A estrutura permite adicionar funcionalidades (como a exportação demonstrada) sem "quebrar" o código existente. Para o contexto académico do 10.º ano, este exemplo ilustra perfeitamente como a programação estruturada facilita o desenvolvimento colaborativo, a depuração de erros (como visível nas capturas de ecrã que demonstram tratamento de exceções) e a expansão gradual de projetos de software.

**Nota:** As capturas de ecrã demonstram a execução real do programa, confirmando o funcionamento correto do menu cíclico, da validação de inputs (rejeição de quantidades negativas) e da exportação bem-sucedida do ficheiro de stock.
