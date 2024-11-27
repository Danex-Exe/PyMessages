from databaze import DataBaze
from Colors import Colors
import datetime, socket, random, re, platform, os, threading


color = Colors()
db = DataBaze()
data_file = db.file("messages")
data_file.create()
os.system("title SERVER - Server.py")
default_data = {
    "chats": {},
    "messages": {},
    "users": {},
    "admins": {},
    "online": []
}

if data_file.read == None or data_file.read == "" or data_file.read == {} or data_file.info()['size'] < 10:
    data_file.write(default_data)
codes = {'а': 'p1vTLSEE', 'б': 'lLS4As63', 'в': 'kCpvj0VI', 'г': 'UPyX5G7Q', 'д': '0Y51zlGl', 'е': 'dIYcfOsB', 'ж': 'MiaziqVQ', 'з': 'Smfi2bH9', 'и': 'LteLz0cd', 'й': 'xkWV4pGR', 'к': 'PefitTNd', 'л': 'pHboQi9K', 'м': 'YkpVlBVj', 'н': 'Rh20Zs1W', 'о': '1ftWDzwI', 'п': '0LHRXkCk', 'р': 'Gbu8IS6G', 'с': 'mZCzXkp7', 'т': 'OOifgI6i', 'у': 'NonsYkfQ', 'ф': 'vVmuyteK', 'х': 'Jy1EqsX6', 'ц': 'zxWoWFNy', 'ч': 'ycjKidHq', 'ш': 'ZuxAaLfM', 'щ': 'TTdFJmDk', 'ъ': 'Dl4PEEGe', 'ы': 'H3J0P2iZ', 'ь': 'r8teMdUP', 'э': 'nTDM2iK7', 'ю': 'lvDH4L86', 'я': 'H3DSbiPz', 'А': 'Hb3iG3LA', 'Б': 'RKOL8j9w', 'В': 'SMTts85W', 'Г': '22deZJE4', 'Д': 'iUtdSf7Q', 'Е': 'wqI39kXq', 'Ж': 'w9EPbDe1', 'З': 'kUEPZptH', 'И': '6YjQdfY2', 'Й': 'ajginsFB', 'К': 'S7F9od5C', 'Л': '6i3xaagC', 'М': 'esBPUbxL', 'Н': 'rStp9Rmt', 'О': '0VnesTAk', 'П': 'TjUOpvH8', 'Р': 'OOdA3Cq0', 'С': 'pGrmw9EM', 'Т': 'g1k5JUDZ', 'У': 'WZGBjyTY', 'Ф': 'R4uZvKti', 'Х': '61rgoMh6', 'Ц': 'N3tgrXZC', 'Ч': 'oNVkCcNE', 'Ш': 'eUGJ4tda', 'Щ': 'vcJeT0qr', 'Ъ': 'DRhiUgr4', 'Ы': 'irD96pNE', 'Ь': 'GZxeDGAQ', 'Э': 'wfTJMR5o', 'Ю': '7ysTAsYX', 'Я': '5LlRs1nm', 'a': 'ckfqdJSe', 'b': 'd2ncgtah', 'c': 't1IXxLPo', 'd': 'isnVmknn', 'e': 'af4wBVoV', 'f': 'LMUKOtqG', 'g': 'SF5Pn7Ox', 'h': 'qkspHxg3', 'i': 'I17pKl23', 'j': 'cobGa5C5', 'k': 'lddYuksc', 'l': 'DtshAAAh', 'm': 'fdLnZlq0', 'n': 'uN6Okz23', 'o': '6gFFxZ1K', 'p': 'gmktoFJU', 'q': 'aNx9VFkV', 'r': 'lPGRlL4D', 's': 'IRJRXHAn', 't': 'Wz8p6Au0', 'u': 'Jq422G2y', 'v': 't3JwSKRv', 'w': 'lp6RijhQ', 'x': 'nNGVcZT5', 'y': 'uoLw8Zko', 'z': 'KQR3Eysm', 'A': 'nyquE1oK', 'B': 'WNBg94iC', 'C': 'OyTtpNwk', 'D': 'V3txzstz', 'E': 'rh5lRbaK', 'F': 'MAKoMvj8', 'G': 'DJ1BBVKJ', 'H': 'uSoTy3Gy', 'I': 'kG3p5DUt', 'J': 'Y9mtfTiU', 'K': '07CaC2Wu', 'L': 'jEtll3pY', 'M': 'QAE9SF0U', 'N': 'hOnl7jWj', 'O': 'XC7dG8lU', 'P': 'HhitGNGr', 'Q': 'WNXQ2Fmv', 'R': 'nJepVyMG', 'S': 'CD4pRadD', 'T': 's0hffFft', 'U': 'vQa40s8t', 'V': 'PwOZq3g2', 'W': 'vrnKeh6a', 'X': 'AY7esPoP', 'Y': 'BcS8Aa4j', 'Z': 'uiOkE42H', '0': 'swmAqVI4', '1': 'BDzchu9I', '2': '2EVhNa4s', '3': 'Mh4slBVQ', '4': 'qMdYNoLW', '5': 'KAWb4h7F', '6': 'XGltI9O7', '7': 'IGRXXHLX', '8': 'J3wqZyWI', '9': 'dhA6vqLJ'}

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
clear()
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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Сервер запущен и слушает на порту {color.rgb_color(255, 255, 200)}3030{color.reset}...")
online = []
auth = []
def handle_client(conn, addr):
    global online
    try:
        while True:
            try:
                find_t = False
                for i in range(len(online)):
                    if online[i][0] == formating(str(addr[1])):
                        find_t = True
                if find_t == False and addr[1] not in auth:
                    print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Подключен клиент с адресом {color.rgb_color(255, 255, 200)}{addr}{color.reset}")
                    online.append([formating(str(addr[1])), 'None', conn])
                    auth.append(addr[1])
                else:
                    for i in range(len(online)):
                        if online[i][0] == formating(str(addr[1])):
                            online.remove(online[i])
                    auth.remove(addr[1])
                    break
                
                while True:
                    try:
                        data = conn.recv(1024)
                    except:
                        return
                    response = "None"
                    if not data:
                        print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Клиент с адресом {color.rgb_color(255, 255, 200)}{addr}{color.reset} отключился.")
                        for i in range(len(online)):
                            if online[i][0] == formating(str(addr[1])):
                                online.remove(online[i])
                        break
                    
                    decoded_data = data.decode('utf-8')
                    if decoded_data.count(':') == 1:
                        decoded_data_split = decoded_data.split(':')
                        if decoded_data_split[1] == "CHECK":
                            if decoded_data_split[0] in data_file.read()['users']:
                                response = "True"
                            else:
                                response = "False"
                        else:
                            response = "Некорректный запрос"
                    elif decoded_data.count(':') == 2:
                        decoded_data_split = decoded_data.split(':')
                        if decoded_data_split[2] == "CHECK":
                            if decoded_data_split[0] in data_file.read()['users']:
                                if decoded_data_split[1] == data_file.read()['users'][decoded_data_split[0]]['password']:
                                    response = "True"
                                    print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Клиент с адресом {color.rgb_color(255, 255, 200)}{addr}{color.reset} вошел в аккаунт: {color.rgb_color(255, 255, 200)}{decrypt(decoded_data_split[0])}{color.reset}")
                                    for i in range(len(online)):
                                        if online[i][0] == formating(str(addr[1])):
                                            online[i][1] = decoded_data_split[0]
                                else:
                                    response = "False"
                            else:
                                response = "False"
                        elif decoded_data_split[2] == "CREATE":
                            if 'users' in data_file.read():
                                if decoded_data_split[0] in data_file.read()['users']:
                                    response = "False"
                                else:
                                    t = data_file.read()
                                    t['users'][decoded_data_split[0]] = {
                                        "password": decoded_data_split[1],
                                    }
                                    data_file.write(t)
                                    response = "True"
                                    print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Клиент с адресом {color.rgb_color(255, 255, 200)}{addr}{color.reset} создал аккаунт: {color.rgb_color(255, 255, 200)}{decrypt(decoded_data_split[0])}{color.reset}")
                                    for i in range(len(online)):
                                        if online[i][0] == formating(str(addr[1])):
                                            online[i][1] = decoded_data_split[0]
                            else:
                                response = "False"
                        elif decoded_data_split[2] == "DELETE":
                            if decoded_data_split[0] in data_file.read()['users']:
                                if decoded_data_split[1] == data_file.read()['users'][decoded_data_split[0]]['password']:
                                    t = data_file.read()
                                    del t['users'][decoded_data_split[0]]
                                    data_file.write(t)
                                    response = "True"
                                else:
                                    response = "False"
                            else:
                                response = "False"
                        else:
                            if 'users' in data_file.read():
                                if decoded_data_split[0] in data_file.read()['users']:
                                    if decoded_data_split[1] == data_file.read()['users'][decoded_data_split[0]]['password']:
                                        login = decrypt(decoded_data_split[0])
                                        decoded_data_split[2:]
                                        decoded_data_split = "".join(decoded_data_split[2:]).replace('_', ' ')
                                        print(f"{color.rgb_bgcolor(80, 80, 80)} {color.rgb_color(200, 0, 200)}[{get_time()}] {color.reset} Пользователь {color.rgb_color(255, 255, 200)}{login}{color.reset} отправил сообщение: {color.rgb_color(255, 255, 200)}{decrypt(decoded_data_split)}{color.reset}")
                                        response = "OK"
                                    else:
                                        response = "Пользователь не зарегистрирован"
                                else:
                                    response = "Пользователь не зарегистрирован"
                    elif decoded_data.count(':') == 3:
                        decoded_data_split = decoded_data.split(':')
                        for i in online:
                            try:
                                if i[1] == decoded_data_split[2]:
                                    login = decrypt(decoded_data_split[0])
                                    decoded_data_split = ":".join(decoded_data_split[3:])
                                    message = login+'|'+decoded_data_split
                                    i[2].sendall(message.encode('utf-8'))
                                    response = None
                            except:
                                response = "False"
                    else:
                        response = "Некорректный запрос"
                
                    if response != None and response != 'None':
                        conn.sendall(response.encode('utf-8'))

                conn.close()  # Закрываем соединение после выхода из внутреннего цикла
            except KeyboardInterrupt:
                break
    except KeyboardInterrupt:
        s.close()
        quit()

    s.close()

"""
AUTHOR:PASSWORD:USERNAME:MESSAGE
AUTHOR:PASSWORD:USERNAME:DELETE
AUTHOR:PASSWORD:USERNAME:CHAT
AUTHOR:PASSWORD:NEWPASSWORD:NEWPASSWORD
AUTHOR:PASSWORD:CHECK
AUTHOR:PASSWORD:CHATS
AUTHOR:PASSWORD:ONLINE
AUTHOR:PASSWORD:DELETE
AUTHOR:PASSWORD:CREATE
USERNAME:CHECK
"""

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 6952))
    s.listen(15)  # Максимум 5 ожидающих подключений

    while True:
        try:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
        except KeyboardInterrupt:
            break
    s.close()
    print("Сервер остановлен.")

if __name__ == "__main__":
    start_server()