import socket
import os

def handle_request(request):
    # Извлечение запрашиваемого пути из HTTP-запроса
    path = request.split()[1]
    # Определение полного пути к запрашиваемому файлу на сервере
    file_path = os.path.abspath(os.path.join(".", path.strip("/")))

    if os.path.isfile(file_path):
        # Если файл существует, читаем его содержимое
        with open(file_path, "rb") as file:
            content = file.read()
        # Формирование HTTP-ответа со статусом 200 OK и содержимым файла
        response = "HTTP/1.1 200 OK\r\n\r\n".encode() + content
    else:
        # Формирование HTTP-ответа со статусом 404 Not Found
        response = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found".encode()

    return response

def run_server():
    # Создание TCP-сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязка сокета к адресу и порту
    server_socket.bind(("localhost", 8000))
    # Ожидание входящих соединений
    server_socket.listen(1)
    print("Server is running...")

    while True:
        # Принятие входящего соединения
        client_socket, client_address = server_socket.accept()
        # Получение данных от клиента
        request = client_socket.recv(1024).decode()
        # Обработка запроса
        response = handle_request(request)
        # Отправка ответа клиенту
        client_socket.sendall(response)
        # Закрытие соединения
        client_socket.close()

if __name__ == "__main__":
    run_server()