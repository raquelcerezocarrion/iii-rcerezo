import socket
import datetime

def handle_message(message: str) -> str:
    message = message.strip().upper()
    if message == "FECHA":
        return datetime.datetime.now().strftime("%Y-%m-%d")
    elif message == "HORA":
        return datetime.datetime.now().strftime("%H:%M:%S")
    else:
        return "ERROR"

def start_server(port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f"Servidor escuchando en el puerto {port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexión establecida con {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode('utf-8')
                    response = handle_message(message)
                    conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    start_server(16031)

