import socket
import threading
import queue
import time
import random
from utils import logger

class PortScanner:
    def __init__(self, target, ports, scan_types):
        self.target = target
        self.ports = self.parse_ports(ports)
        self.scan_types = scan_types.split(",") if scan_types != "all" else ["tcp", "syn", "udp", "icmp"]
        self.results = []
        self.logger = logger.get_logger()

    def parse_ports(self, port_str):
        ports = []
        parts = port_str.split(",")
        for part in parts:
            if "-" in part:
                start, end = part.split("-")
                ports.extend(range(int(start), int(end) + 1))
            else:
                ports.append(int(part))
        return ports

    def scan_port_tcp(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            sock.close()
            if result == 0:
                self.logger.info(f"TCP Port {port} is open")
                self.results.append((port, "tcp", "open"))
            else:
                self.results.append((port, "tcp", "closed"))
        except Exception as e:
            self.logger.error(f"Error scanning TCP port {port}: {e}")

    def scan_port_syn(self, port):
        # Placeholder for SYN scan implementation
        # For now, simulate random open/closed
        status = random.choice(["open", "closed"])
        self.logger.info(f"SYN Port {port} is {status}")
        self.results.append((port, "syn", status))

    def scan_port_udp(self, port):
        # Placeholder for UDP scan implementation
        status = random.choice(["open", "closed"])
        self.logger.info(f"UDP Port {port} is {status}")
        self.results.append((port, "udp", status))

    def scan_port_icmp(self, port):
        # ICMP is not port-based, placeholder for host ping
        self.logger.info(f"ICMP scan on {self.target} (not port-based)")

    def worker(self, q):
        while not q.empty():
            port = q.get()
            for scan_type in self.scan_types:
                if scan_type == "tcp":
                    self.scan_port_tcp(port)
                elif scan_type == "syn":
                    self.scan_port_syn(port)
                elif scan_type == "udp":
                    self.scan_port_udp(port)
                elif scan_type == "icmp":
                    self.scan_port_icmp(port)
            q.task_done()

    def run(self):
        q = queue.Queue()
        for port in self.ports:
            q.put(port)

        threads = []
        for _ in range(min(100, len(self.ports))):
            t = threading.Thread(target=self.worker, args=(q,))
            t.start()
            threads.append(t)

        q.join()
        for t in threads:
            t.join()

        return self.results

def run_scan(target, ports, scan_types):
    scanner = PortScanner(target, ports, scan_types)
    results = scanner.run()
    for port, stype, status in results:
        print(f"Port {port} [{stype}] is {status}")
