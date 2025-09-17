from pyservers import PyServer, PyClient
import threading
import time

def run_server():
    server = PyServer(host='localhost', port=8000)
    print("Сервер запущен...")
    server.start()

# Запуск сервера в отдельном потоке
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Ждём запуск сервера
time.sleep(2)

# Создаём клиента
client = PyClient(host='localhost', port=8000)
if client.connect():
    print("Клиент подключён!")
    client.send("Привет, сервер!")
    time.sleep(1)
    client.disconnect()

print("Тест завершён")