from colorama import Fore, init
import os
import re
import time

# Reseta a cor
init(autoreset=True)
os.system('clear')

def banner():
    print(f'''
{Fore.RED}
  _   _      _   _              __          ___                  _ 
 | \ | |    | | | |             \ \        / (_)                | |
 |  \| | ___| |_| |     ___   __ \ \  /\  / / _ ______ _ _ __ __| |
 | . ` |/ _ \ __| |    / _ \ / _` \ \/  \/ / | |_  / _` | '__/ _` |
 | |\  |  __/ |_| |___| (_) | (_| |\  /\  /  | |/ / (_| | | | (_| |
 |_| \_|\___|\__|______\___/ \__, | \/  \/   |_/___\__,_|_|  \__,_|
                              __/ |                                
                             |___/                                    
{Fore.RESET}
[{Fore.GREEN}x{Fore.RESET}] Autor: brunofsec
[{Fore.GREEN}x{Fore.RESET}] Github: https://github.com/brunofrs/NetLogWizard
    ''')

def menu():
    print(f'''
=====================
-> LOGS DE ACESSO <-
=====================
[{Fore.CYAN}1{Fore.RESET}] - Logs de login no sistema
    ''')

def menu_escolhido():
    op = input("Digite sua escolha: ")
    if op == '1':
        time.sleep(0.5)
        os.system('clear')
        print(f'{Fore.GREEN}Iniciando coleta de logs de login do sistema...')
        login_logs = login_sistema_log()
        filtro = r'(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}).*New session \w+ of user (\w+-\w+)'
        if login_logs:
            print(f"{Fore.GREEN}Login no sistema:")
            for log in login_logs:
                linha_filtrada = re.search(filtro, log)
                if linha_filtrada:
                    date = linha_filtrada.group(1)
                    user = linha_filtrada.group(2)
                    print(f"{Fore.YELLOW}Data: {date}, {Fore.WHITE}Usuário: {Fore.GREEN}{user}")
        else:
            print(f"{Fore.YELLOW}Nenhum log de login encontrado.")
            return

# função para obter logs do sistema de login
def login_sistema_log():
    login_logs = []

    # caminho completo para o arquivo auth.log
    auth_log_path = '/var/log/auth.log'

    # verifica se o arquivo existe
    if not os.path.exists(auth_log_path):
        return login_logs

    # comando para obter as informações de acesso
    log_comando = f'cat {auth_log_path} | grep "New session"'

    try:
        with os.popen(log_comando) as log_arquivo:
            linhas = log_arquivo.readlines()
            login_logs = [linha.strip() for linha in linhas]

    except Exception as e:
        login_logs.append(f"Erro ao acessar os logs de login: {str(e)}")

    return login_logs


if __name__ == '__main__':
    banner()
    menu()
    menu_escolhido()
