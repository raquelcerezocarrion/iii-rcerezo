import unittest
import socket
from threading import Thread
from server import start_server

class TestServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = Thread(target=start_server, args=(16031,), daemon=True)
        cls.server_thread.start()

    def test_fecha(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 16031))
            s.sendall("FECHA".encode('utf-8'))
            response = s.recv(1024).decode('utf-8')
            self.assertRegex(response, r"\d{4}-\d{2}-\d{2}")