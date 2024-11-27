import socket, time, platform, os, re, ast

# Создание сокета и подключение к серверу
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
def get_local_ip():
    try:
        # Создаем временный сокет
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Подключаем сокет к любому адресу (можете использовать любой внешний)
        s.connect(('8.8.8.8', 80))  # Google DNS (или любой внешний адрес)
        local_ip = s.getsockname()[0]  # Получаем IP-адрес
        s.close()  # Закрываем сокет
        return local_ip
    except Exception as e:
        print(f"Ошибка при получении локального IP: {e}")
        return None
s.connect((get_local_ip(), 6952))  # Подключаемся к серверу
os.system("title CHAT - App.py")

local_ip, local_port = s.getsockname()
print(f"Локальный IP-адрес: {local_ip}, Локальный порт: {local_port}")

codes = {'а': 'p1vTLSEE', 'б': 'lLS4As63', 'в': 'kCpvj0VI', 'г': 'UPyX5G7Q', 'д': '0Y51zlGl', 'е': 'dIYcfOsB', 'ж': 'MiaziqVQ', 'з': 'Smfi2bH9', 'и': 'LteLz0cd', 'й': 'xkWV4pGR', 'к': 'PefitTNd', 'л': 'pHboQi9K', 'м': 'YkpVlBVj', 'н': 'Rh20Zs1W', 'о': '1ftWDzwI', 'п': '0LHRXkCk', 'р': 'Gbu8IS6G', 'с': 'mZCzXkp7', 'т': 'OOifgI6i', 'у': 'NonsYkfQ', 'ф': 'vVmuyteK', 'х': 'Jy1EqsX6', 'ц': 'zxWoWFNy', 'ч': 'ycjKidHq', 'ш': 'ZuxAaLfM', 'щ': 'TTdFJmDk', 'ъ': 'Dl4PEEGe', 'ы': 'H3J0P2iZ', 'ь': 'r8teMdUP', 'э': 'nTDM2iK7', 'ю': 'lvDH4L86', 'я': 'H3DSbiPz', 'А': 'Hb3iG3LA', 'Б': 'RKOL8j9w', 'В': 'SMTts85W', 'Г': '22deZJE4', 'Д': 'iUtdSf7Q', 'Е': 'wqI39kXq', 'Ж': 'w9EPbDe1', 'З': 'kUEPZptH', 'И': '6YjQdfY2', 'Й': 'ajginsFB', 'К': 'S7F9od5C', 'Л': '6i3xaagC', 'М': 'esBPUbxL', 'Н': 'rStp9Rmt', 'О': '0VnesTAk', 'П': 'TjUOpvH8', 'Р': 'OOdA3Cq0', 'С': 'pGrmw9EM', 'Т': 'g1k5JUDZ', 'У': 'WZGBjyTY', 'Ф': 'R4uZvKti', 'Х': '61rgoMh6', 'Ц': 'N3tgrXZC', 'Ч': 'oNVkCcNE', 'Ш': 'eUGJ4tda', 'Щ': 'vcJeT0qr', 'Ъ': 'DRhiUgr4', 'Ы': 'irD96pNE', 'Ь': 'GZxeDGAQ', 'Э': 'wfTJMR5o', 'Ю': '7ysTAsYX', 'Я': '5LlRs1nm', 'a': 'ckfqdJSe', 'b': 'd2ncgtah', 'c': 't1IXxLPo', 'd': 'isnVmknn', 'e': 'af4wBVoV', 'f': 'LMUKOtqG', 'g': 'SF5Pn7Ox', 'h': 'qkspHxg3', 'i': 'I17pKl23', 'j': 'cobGa5C5', 'k': 'lddYuksc', 'l': 'DtshAAAh', 'm': 'fdLnZlq0', 'n': 'uN6Okz23', 'o': '6gFFxZ1K', 'p': 'gmktoFJU', 'q': 'aNx9VFkV', 'r': 'lPGRlL4D', 's': 'IRJRXHAn', 't': 'Wz8p6Au0', 'u': 'Jq422G2y', 'v': 't3JwSKRv', 'w': 'lp6RijhQ', 'x': 'nNGVcZT5', 'y': 'uoLw8Zko', 'z': 'KQR3Eysm', 'A': 'nyquE1oK', 'B': 'WNBg94iC', 'C': 'OyTtpNwk', 'D': 'V3txzstz', 'E': 'rh5lRbaK', 'F': 'MAKoMvj8', 'G': 'DJ1BBVKJ', 'H': 'uSoTy3Gy', 'I': 'kG3p5DUt', 'J': 'Y9mtfTiU', 'K': '07CaC2Wu', 'L': 'jEtll3pY', 'M': 'QAE9SF0U', 'N': 'hOnl7jWj', 'O': 'XC7dG8lU', 'P': 'HhitGNGr', 'Q': 'WNXQ2Fmv', 'R': 'nJepVyMG', 'S': 'CD4pRadD', 'T': 's0hffFft', 'U': 'vQa40s8t', 'V': 'PwOZq3g2', 'W': 'vrnKeh6a', 'X': 'AY7esPoP', 'Y': 'BcS8Aa4j', 'Z': 'uiOkE42H', '0': 'swmAqVI4', '1': 'BDzchu9I', '2': '2EVhNa4s', '3': 'Mh4slBVQ', '4': 'qMdYNoLW', '5': 'KAWb4h7F', '6': 'XGltI9O7', '7': 'IGRXXHLX', '8': 'J3wqZyWI', '9': 'dhA6vqLJ'}

def formating(n: str) -> str:
    """Кодирование (шифрование) сообщения."""
    encrypted_message = ''.join(codes.get(c, c) for c in n)
    return encrypted_message


def decrypt(n: str) -> str:
    """Декодирование (расшифрование) сообщения."""
    # Создаём обратный словарь для декодирования
    reverse_codes = {v: k for k, v in codes.items()}
    
    # Функция для замены кода на оригинал
    def replace_code(match):
        code = match.group(0)
        return reverse_codes.get(code, code)  # Возвращаем оригинал или сам код, если не найден

    # Используем регулярное выражение для поиска всех кодов в строке
    pattern = '|'.join(re.escape(code) for code in reverse_codes.keys())
    decrypted_message = re.sub(pattern, replace_code, n)
    
    return decrypted_message
class user:
    def __init__(self, login: str, password: str, type: str):
        self.login = formating(login)
        self.password = formating(password)
        if type == 'login':
            self.status = True
        else:
            s.sendall(f'{self.login}:{self.password}:CREATE'.encode('utf-8'))
            response = s.recv(1024)
            if response.decode('utf-8') == "True":
                self.status = True
            else:
                self.status = False
        os.system("title CHAT - App.py $ " + login)

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def waiting(n):
    for i in range(1, n+1):
        time.sleep(1)
    print()
waiting(5)
def check_input(message: str, n: int):
    try:
        while True:
            t = input(message)
            
            try:
                t = int(t)
                if t in range(1, n):
                    return t
                else:
                    print("Введено некорректное значение")
                    waiting(5)
            except:
                print("Введено некорректное значение")
                waiting(5)
            clear()
    except KeyboardInterrupt:
        clear()
        exit()
def auth():
    clear()
    print("""                           Добро пожаловать в CHAT!
          
Вам необходимо войти в аккаунт. Выберите один из вариантов:
1 - Вход в аккаунт
2 - Регистрация
3 - Выход
""")
    t = check_input("> ", 3)
    if t == 1:
        login()
    elif t == 2:
        register()
    elif t == 3:
        clear()
        exit()



def login():
    def check_login(login: str):
        s.sendall(f'{login}:CHECK'.encode('utf-8'))  # Отправляем фразу
        response = s.recv(1024)  # Получаем данные из сокета
        if response.decode('utf-8') == "True":
            return True
        else:
            return False
    def check_password(login: str, password: str):
        s.sendall(f'{login}:{password}:CHECK'.encode('utf-8'))  # Отправляем фразу
        response = s.recv(1024)  # Получаем данные из сокета
        if response.decode('utf-8') == "True":
            return True
        else:
            return False
    try:
        while True:
            login = input("Введите логин: ")
            if check_login(formating(login)):
                password = input("Введите пароль: ")
                if check_password(formating(login), formating(password)):
                    main(user(login, password, 'login'))
                else:
                    print("Неверный пароль")
                    waiting(5)
            else:
                print("Такого логина не существует")
                waiting(5)
    except KeyboardInterrupt:
        clear()
        exit()
def register():
    def check_login(login: str):
        s.sendall(f'{login}:CHECK'.encode('utf-8'))  # Отправляем фразу
        response = s.recv(1024)  # Получаем данные из сокета
        if response.decode('utf-8') == "True":
            return True
        else:
            return False
    def check_password(password: str):
        if len(password) < 8:
            return False
        else:
            return True
    try:
        while True:
            login = input("Введите логин: ")
            if check_login(formating(login)):
                print("Такой логин уже занят")
                waiting(5)
            else:
                password = input("Введите пароль: ")
                if check_password(password):
                    main(user(login, password, 'register'))
                else:
                    print("Неверный пароль (Пароль не может быть меньше 8 символов!)")
                    waiting(5)
    except KeyboardInterrupt:
        clear()
        exit()

def chat(name, user):
    clear()
    print(f"Вы в чате с {name} (exit - выход)")
    while True:
        message = input("> ").replace(' ', '_')
        if message == "exit":
            s.close()
            clear()
            exit()
        if message != "" and message != "\n":
            message = f"{user.login}:{user.password}:{formating(name)}:{formating(message)}"
            s.sendall(message.encode('utf-8'))
        else:
            message = f"{user.login}:{user.password}:{formating(name)}:None"
            s.sendall(message.encode('utf-8'))
            
        try:
            data = s.recv(1024)
            if '|' in data.decode('utf-8'):
                data = decrypt(data.decode('utf-8')).split('|')
                if data[1] != 'None':
                    print(f"{data[0]}: {data[1].replace('_', ' ')}")
        except Exception as e:
            print(f"Ошибка при приёме данных: {e}")


def chats(user):
    while True:
        print(f"""Введите никнейм собеседника:
[1] - Выход""")
        
        t = input("> ")
        try:
            if t == '1':
                clear()
                exit()
            else:
                message = f"{formating(t)}:CHECK"
                s.sendall(message.encode('utf-8'))
                response = s.recv(1024)
                if response.decode('utf-8') == "True":
                    chat(t, user)
                else:
                    print("Такого пользователя не существует")
                    waiting(5)
        except ValueError:
            print("Введено некорректное значение")
            waiting(5)
        clear()

def main(user):
    clear()
    if user.status == False:
        print("Не удалось создать аккаунт/подключиться к аккаунту")
        waiting(5)
        clear()
        exit()
    try:
       chats(user)
    except KeyboardInterrupt:
        clear()
        exit()

if __name__ == "__main__":
    auth()
