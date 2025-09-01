from colorama import Fore, Style, init
import os
import requests
import webbrowser

# Автор программы - github.com/ech0ware

init()

def cat():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '''
／l、
（ﾟ､ ｡７
l、ﾞ~ヽ
じしf_, )ノ
    ''' + Style.RESET_ALL, Fore.RESET)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ipinfo(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        main_data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Организация]': response.get('org'),
        }

        geo_data = {
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Индекс]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon')
        }

        clear()
        cat()
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Основная информация" + Style.RESET_ALL)
        for k, v in main_data.items():
            print(Fore.LIGHTGREEN_EX + f"{k}: {v}")

        print(Fore.LIGHTRED_EX + Style.BRIGHT + "\nГео-данные" + Style.RESET_ALL)
        for k, v in geo_data.items():
            print(Fore.LIGHTGREEN_EX + f"{k}: {v}")

        print(Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"[!] Ошибка запроса: {e}" + Fore.RESET)


def torrents(ip='127.0.0.1'):
    url = f"https://iknowwhatyoudownload.com/en/peer/?ip={ip}"
    clear()
    cat()
    print(Fore.LIGHTRED_EX + Style.BRIGHT + f"Раздаваемые торренты для {ip}" + Style.RESET_ALL)
    webbrowser.open(url)

def menu():
    clear()
    print(Fore.RED + '''                                             
    ,--.,------.     ,--------. ,-----.  ,-----. ,--.    
    |  ||  .--. '    '--.  .--''  .-.  ''  .-.  '|  |    
    |  ||  '--' |       |  |   |  | |  ||  | |  ||  |    
    |  ||  | --'        |  |   '  '-'  ''  '-'  '|  '--. 
    `--'`--'            `--'    `-----'  `-----' `-----' 
                      By ech0ware                                                          
    ''' + Fore.RESET)

    print(Fore.LIGHTRED_EX + '[1] Досье по IP\n'
          '[2] Раздаваемые торренты по IP\n'
          '[3] IP-Логгер\n'
          '[4] Github\n'
          '[0] Выход')

    return int(input(Style.BRIGHT + Fore.RED + '-> ' + Style.RESET_ALL + Fore.RESET))

while True:
    vibor = menu()
    if vibor == 1:
        target_ip = input(Fore.LIGHTRED_EX + Style.BRIGHT + 'Введите IP (0 для отмены) -> ' + Style.RESET_ALL + Fore.RESET)
        if target_ip == '0':
            continue
        else:
            ipinfo(target_ip)
            input(Fore.YELLOW + "[Нажмите Enter для возврата в меню]" + Fore.RESET)
    elif vibor == 2:
        target_ip = input(Fore.LIGHTRED_EX + Style.BRIGHT + 'Введите IP (0 для отмены) -> ' + Style.RESET_ALL + Fore.RESET)
        if target_ip == '0':
            continue
        else:
            torrents(target_ip)
            input(Fore.YELLOW + "[Нажмите Enter для возврата в меню]" + Fore.RESET)
    elif vibor == 3:
        webbrowser.open('grabify.link')
        menu()
    elif vibor == 4:
        webbrowser.open('https://github.com/ech0ware')
        menu()
    elif vibor == 0:
        break
