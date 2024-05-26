# tests/test_protocol.py
import unittest
from protocol import Protocol

class TestProtocol(unittest.TestCase):
    def test_fecha(self):
        response = Protocol.handle_message("FECHA")
        self.assertRegex(response, r"\d{4}-\d{2}-\d{2}")

    def test_hora(self):
        response = Protocol.handle_message("HORA")
        self.assertRegex(response, r"\d{2}:\d{2}:\d{2}")

    def test_error(self):
        response = Protocol.handle_message("HELLO")
        self.assertEqual(response, "ERROR")

if __name__ == "__main__":
    unittest.main()
