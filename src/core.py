import argparse
import os
from src.modules.base_module import BaseModule
from src.modules.outdated_services import OutdatedServicesModule
from src.port_scanner import PortScanner

LOGO_PATH = os.path.join(os.path.dirname(__file__), "assets", "logo.txt")


def load_logo():
    try:
        with open(LOGO_PATH, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] Logo no encontrado.")


def run_scan(target, scan_type):

    if scan_type == "ports":
        scanner = PortScanner()
        scanner.scan(target)

    elif scan_type == "all":
        scanner = PortScanner()
        scanner.scan(target)

        modules: list[BaseModule] = [
            OutdatedServicesModule(),
        ]

        for module in modules:
            print(f"\n[+] Ejecutando módulo: {module.name}")
            module.run(target)

    else:
        print("[!] Tipo de escaneo no válido.")


def main():
    load_logo()

    parser = argparse.ArgumentParser(description="RedSec Recon Suite")
    parser.add_argument("--host", required=True, help="Host o IP objetivo")
    parser.add_argument("--scan", required=True, choices=["ports", "all"],
                        help="Tipo de escaneo a ejecutar")

    args = parser.parse_args()
    run_scan(args.host, args.scan)


if __name__ == "__main__":
    main()
