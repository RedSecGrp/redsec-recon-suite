from src.port_scanner import PortScanner

def test_scanner_instance():
    s = PortScanner()
    assert isinstance(s, PortScanner)
