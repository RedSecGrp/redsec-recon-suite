import socket


class PortScanner:

    def scan(self, host):
        print(f"[+] Escaneando puertos para {host}")

        ports = [22, 80, 443, 3306]

        for port in ports:
            if self.check_port(host, port):
                print(f"[+] Puerto {port}/tcp abierto")
            else:
                print(f"[-] Puerto {port}/tcp cerrado")

    @staticmethod
    def check_port(host, port):
        s = socket.socket()
        s.settimeout(0.5)

        try:
            s.connect((host, port))
            s.close()
            return True
        except:
            return False
