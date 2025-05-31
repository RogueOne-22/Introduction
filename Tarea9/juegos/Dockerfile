# Dockerfile para ejecutar juegos en consola
FROM python:3.10-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-dev build-essential \
    libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev \
    libsdl1.2-dev libsmpeg-dev libportmidi-dev libavformat-dev \
    libswscale-dev libfreetype6-dev libffi-dev libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /juegos

# Copiar el contenido
COPY . .

# Instalar pygame
RUN pip install pygame

# Mostrar mensaje de ayuda e iniciar bash
CMD echo "\n🕹️ Juegos disponibles:\n" \
    "  python3 space.py                # SpaceMax Defender\n" \
    "  python3 Tetris_TareaP.py        # Tetris\n" \
    "  python3 TanquesP.py             # Tanques\n\n" \
    "Ejemplo: python3 space.py \n" && bash

