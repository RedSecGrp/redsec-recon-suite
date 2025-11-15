  _____                           _____       _ _       
 |  __ \                         / ____|     (_) |      
 | |__) |___  ___ ___  _ __     | (___  _   _ _| |_ ___ 
 |  _  // _ \/ __/ _ \| '_ \     \___ \| | | | | __/ _ \
 | | \ \  __/ (_| (_) | | | |    ____) | |_| | | ||  __/
 |_|  \_\___|\___\___/|_| |_|   |_____/ \__,_|_|\__\___|
 
          R E D S E C   G R O U P  ·  C A P A  8
      recon-suite — modular recon & offensive scanning

# 🔍 RedSec Recon Suite  
*Framework modular de reconocimiento y escaneo desarrollado por RedSec Group*

Bienvenido a **RedSec Recon Suite**, una herramienta profesional diseñada para equipos de **pentesting, red teaming y ciberseguridad ofensiva**.  
Su enfoque modular permite extender rápidamente las capacidades del escáner y adaptarlo a proyectos empresariales, auditorías técnicas o laboratorios de aprendizaje.

---

## 🚀 Características principales

- 🔎 **Escáner de puertos básico y avanzado**
- 🧩 **Arquitectura modular** (agrega tus propios escáneres)
- 📦 **Framework extensible**
- ⚙️  **Detección de servicios obsoletos**
- 🛠️  **Salida limpia en consola**
- 🧪 **Incluye pruebas automatizadas**

---

## 📂 Estructura del proyecto

```
redsec-recon-suite/
├── src/
│   ├── core.py
│   ├── port_scanner.py
│   └── modules/
│       ├── base_module.py
│       └── outdated_services.py
└── tests/
```

---

## 🛡️ Instalación

```bash
git clone https://github.com/RedSecGroup/redsec-recon-suite.git
cd redsec-recon-suite
pip install -r requirements.txt
```

---

## ▶️ Uso rápido

```bash
python3 src/core.py --host 192.168.1.10 --scan ports
```

Salida esperada:

```
[+] Escaneando puertos para 192.168.1.10
[+] Puerto 22/tcp abierto (SSH)
[+] Puerto 80/tcp abierto (HTTP)
```

---

## 🧰 Modo avanzado: Ejecutar todos los módulos

```bash
python3 src/core.py --host ejemplo.com --scan all
```

---

## 🧩 Crear un módulo nuevo (extensión personalizada)

Crea un archivo dentro de `src/modules/` basado en `base_module.py`.

```python
class MyModule(BaseModule):
    name = "Mi Módulo"
    description = "Describa aquí lo que hace este módulo."

    def run(self, target):
        print(f"Ejecutando módulo sobre {target}...")
```

---

## 🛣️ Roadmap

- [ ] Escaneo multi-hilo de puertos
- [ ] Integración con Shodan
- [ ] Fingerprinting avanzado
- [ ] Output en JSON
- [ ] Dashboard web para reportes
- [ ] Módulo de descubrimiento de subdominios
- [ ] API REST del framework

---

## 🤝 Contribuir

Ver archivo `CONTRIBUTING.md`.

---

## 🔐 Seguridad

Reporta vulnerabilidades en `SECURITY.md`.

---

## 🏢 Autor

**RedSec Group — "Código. Evolución. Seguridad."**  
**Mtr.S.I. Luis Campista**
https://github.com/RedSecGroup
