import socket

def start_client(server_ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        for message in ["FECHA", "HORA", "UNKNOWN"]:
            s.sendall(message.encode('utf-8'))
            data = s.recv(1024)
            print(f"Respuesta del servidor: {data.decode('utf-8')}")

if __name__ == "__main__":
    server_ip = input("Ingrese la dirección IP del servidor: ")
    start_client(server_ip, 16031)
