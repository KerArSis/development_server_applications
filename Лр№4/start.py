import subprocess
import time
import os

# Определите абсолютные пути
server_path = os.path.join('C:\\Users\\Арсен\\Desktop\\Lr_RSP\\Лр№4', 'server.py')
client_path = os.path.join('C:\\Users\\Арсен\\Desktop\\Lr_RSP\\Лр№4', 'client.py')

# Запуск сервера
server_process = subprocess.Popen(['python', server_path])
print("Сервер запущен...")

# Ждем, чтобы сервер инициализировался (можно заменить на ожидание готовности сервера)
time.sleep(2)

# Запуск клиента два раза подряд
for i in range(2):
    client_process = subprocess.Popen(['python', client_path])
    print(f"Клиент запущен {i + 1} раз...")

# Ожидание завершения процесса сервера
server_process.wait()
