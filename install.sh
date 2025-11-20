#!/usr/bin/env bash

# RedSec Recon Suite Installer
# By RedSecGrp — "Código. Evolución. Seguridad."
# -------------------------------------------------------

set -e

echo "🔥 Installing RedSec Recon Suite environment..."
sleep 1

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 no encontrado. Instálalo antes de continuar."
    exit 1
fi

# Create virtual environment
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# Activate
source venv/bin/activate

# Upgrade pip
echo "⬆️  Actualizando pip..."
pip install --upgrade pip

# Install core requirements
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Install dev requirements if flag provided
if [ "$1" == "--dev" ]; then
    echo "🧪 Instalando dependencias de desarrollo..."
    pip install -r requirements-dev.txt
fi

# Permissions
echo "🔧 Ajustando permisos..."
chmod +x src/main.py 2>/dev/null || true

echo ""
echo "✨ Instalación completada con éxito."
echo "🔥 Para ejecutar:    source venv/bin/activate"
echo "🔥 Para desarrollo:  ./install.sh --dev"
echo ""
