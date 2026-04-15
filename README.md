📊 Calculadora de Média com Substituição de CP
Programa em Python que calcula a média final de um aluno com base em três notas de CP (Checkpoint), aplicando automaticamente a regra de substituição da menor nota pela CP3.

📋 Descrição
O aluno insere as notas das três CPs (valores entre 0 e 10). O programa identifica qual das duas primeiras CPs é a menor e a substitui pelo valor da CP3 — simulando a regra de aproveitamento adotada em algumas instituições de ensino. Em seguida, calcula e exibe a média final.
Regra aplicada:

Se CP1 for a menor → CP1 é substituída pela CP3
Se CP2 for a menor → CP2 é substituída pela CP3
Se CP1 = CP2 (empate), nenhuma substituição é feita
Média final = (CP1 + CP2) / 2 após a substituição


🚀 Como usar
Pré-requisito: Python 3 instalado.
bashpython main.py
Exemplo de execução:
Digite sua CP1: 6.0
Digite sua CP2: 8.0
Digite sua CP3: 9.0
8.5

CP1 (6.0) era a menor, foi substituída pela CP3 (9.0).
Média final: (9.0 + 8.0) / 2 = 8.5


✅ Validação de entrada
O programa não aceita notas fora do intervalo permitido. Caso o usuário digite um valor inválido, a entrada é solicitada novamente:
Digite sua CP1: -3
Digite sua CP1: 11
Digite sua CP1: 7.5   ✔

🗂️ Estrutura do projeto
📁 projeto/
└── main.py   # script principal

🛠️ Tecnologias

Python 3
Estrutura de repetição while para validação de entrada
Condicionais if/elif para lógica de substituição
Entrada de dados com input() e conversão com float()


📄 Licença MIT
Projeto livre para uso educacional.
