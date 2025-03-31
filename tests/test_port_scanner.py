import unittest
from port_scanner import scan_ports

class TestPortScanner(unittest.TestCase):

    def test_scan_common_ports(self):
        target = "127.0.0.1"
        try:
            scan_ports(target)
        except Exception as e:
            self.fail(f"scan_ports raised Exception unexpectedly: {e}")

if __name__ == "__main__":
    unittest.main()
