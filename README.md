bank-system-python
Sistema bancário simples desenvolvido em Python, utilizando a biblioteca tkinter para interface gráfica e operações básicas como depósito, saque e consulta de extrato.

Funcionalidades
Login: Acesso seguro com usuário e senha.
Depósito: Permite ao usuário depositar valores na sua conta.
Saque: Realiza saques dentro de limites definidos.
Extrato: Exibe um extrato com todas as transações realizadas pelo usuário.
Requisitos
Python 3.x
Biblioteca tkinter para a interface gráfica.
Banco de dados em memória utilizando dicionários Python.
Como rodar o projeto
1. Clonar o repositório
bash
Copy
Edit
git clone https://github.com/<seu_usuario>/r-bank-system-python.git
2. Instalar dependências
Este projeto não depende de bibliotecas externas além do tkinter, que já vem instalado com o Python.

3. Rodar o sistema
Para rodar o sistema, execute o seguinte comando:

bash
Copy
Edit
python main.py
4. Interagir com o sistema
Ao iniciar o sistema, você será solicitado a realizar login com um dos usuários pré-cadastrados no arquivo users.py.

Usuários de exemplo:
Usuário 1:

Usuário: user1
Senha: 1337
Saldo inicial: R$ 0.00
Usuário 2:

Usuário: user2
Senha: ab1337
Saldo inicial: R$ 1500.00
Após o login, você poderá acessar as opções de depósito, saque e extrato.

Estrutura de arquivos
banco.py: Contém as funções para realizar operações bancárias como depósito, saque e exibição de extrato.
users.py: Define as contas e usuários do sistema.
main.py: Executa a interface gráfica e coordena as interações do usuário com o sistema bancário.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
