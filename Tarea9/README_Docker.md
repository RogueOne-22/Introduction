# 🎮 Pygame Arcade Games

## Docker Hub: [Pausc0222 - pygame-games](https://hub.docker.com/r/pausc0222/pygame-games)

¡Juegos arcade retro hechos en Python con Pygame, listos para Docker o de manera local

- 🚀 **SpaceMax** (tipo Galaga)
- 🧱 **Tetris Clásico**
- 🔫 **Batalla de Tanques**

---

## 📦 Requisitos

- Python 3.x y pygame (si deseas correrlos localmente)
- Docker 

Instalar Pygame localmente:
```bash
pip install pygame
```

## 📁 Estructura del proyecto en Docker
```
juegos/
├── Dockerfile
├── Tetris_TareaP.py
├── TanquesP.py
└── space_game/
    ├── space.py
    └── assets/
        ├── images/
        └── sounds/
```

---

## ✨ Características 

### SpaceMax Defender
- Disparos con enemigos en movimiento, jefe final con barra de vida
- Pausa (`P`), reinicio (`R`) y salida (`ESC`)
- Jugabilidad tipo Galaga

### Tetris
- Rotaciones, caída, puntuación y niveles
- Pausa (`ENTER`), reinicio (`CTRL`)

### Tanques
- Movimiento con WASD, disparo con `ESPACIO`
- Vida, enemigos IA y sistema de puntuación

---

## 🧑‍💻 Autor

Desarrollado por Paula S ✨

---

## 📜 Licencia

Este proyecto es libre de usar para fines educativos.
