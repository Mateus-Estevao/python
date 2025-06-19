💰 Sistema Bancário em Python
Este é um projeto simples de sistema bancário em Python, feito com menus interativos no terminal. O sistema permite ao usuário realizar operações básicas como depósito, saque e consulta de extrato, com limites e validações.

📋 Funcionalidades
 Depósito com valor positivo

 Saque com limite de valor e quantidade

 Extrato com histórico de operações

 Interface via terminal

 Verificações de erros e mensagens ao usuário

🧾 Menu
text
Copiar
Editar
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
⚙️ Regras do Sistema
O limite máximo de saque por operação é de R$ 500,00.

O usuário pode fazer até 3 saques por dia.

Não é permitido sacar ou depositar valores negativos ou iguais a zero.

O extrato mostra todas as movimentações realizadas.

💡 Como usar
Clone o repositório ou copie o código:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/sistema-bancario.git
Execute o script:

bash
Copiar
Editar
python banco.py
Interaja com o menu, escolhendo as opções digitando:

d para depositar

s para sacar

e para ver o extrato

q para sair do sistema

🧠 Exemplo de uso
text
Copiar
Editar
=> d
Informe o valor do deposito: 1000
=> s
Informe o valor que deseja sacar: 200
=> e

=================== EXTRATO ===================
Deposito : R$ 1000.00
Saque: R$ 200.00

Saldo: R$ 800.00
=================================================
📁 Arquivo
banco.py: Arquivo principal com o código-fonte do sistema bancário.

🛠 Requisitos
Python 3.6 ou superior

Terminal (CMD, Bash ou PowerShell)

🧑‍💻 Autor
Desenvolvido por Mateus Grillo.
