from src.modules.base_module import BaseModule


class OutdatedServicesModule(BaseModule):
    name = "Servicios Obsoletos"
    description = "Identifica servicios potencialmente desactualizados"

    def run(self, target):
        print(f"[→] Analizando servicios obsoletos en {target}...")
        print("[!] (Demo) Se detectó Apache 2.2 — versión antigua")
