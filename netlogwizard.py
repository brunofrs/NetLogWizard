from colorama import Fore, Back, Style, init

# reseta a cor
init(autoreset=True)

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
                             |___/                      {Fore.YELLOW}V:0.1(beta)         
{Style.RESET_ALL}
[{Fore.GREEN}x{Style.RESET_ALL}] Autor: brunofsec
[{Fore.GREEN}x{Style.RESET_ALL}] Github: https://github.com/brunofrs/NetLogWizard


Conteúdo em construção!
    ''')
    


if __name__ == '__main__':
    banner()
