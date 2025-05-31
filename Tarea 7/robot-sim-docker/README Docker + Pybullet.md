>[!Important]
> Para mayor información revisar el archivo adjunto "Docker_pybullet.pdf" (contiene más de 5 páginas)

# Proyecto: Simulación de Robot de Dos Articulaciones

## 📋 Descripción

Este proyecto consiste en la simulación de un robot de dos articulaciones usando **PyBullet** y **Python 3**, ejecutado dentro de un contenedor Docker configurado para soportar entorno gráfico.

La simulación permite:
- Controlar el movimiento de las dos articulaciones mediante sliders.
- Ajustar dinámicamente la velocidad de simulación.
- Pausar y reanudar la simulación en tiempo real.

## 🛠️ Archivos principales

- **`main.py`**: Script principal que lanza la simulación y gestiona la interacción.
- **`two_joint_robot_custom.urdf`**: Archivo URDF que define la estructura física del robot.
- **`Dockerfile`**: Configura un contenedor Docker que instala todas las dependencias necesarias.

## 🧩 Estructura del Código (`main.py`)

- Inicializa PyBullet en modo GUI.
- Carga el plano base y el robot desde su archivo URDF.
- Configura sliders para controlar:
  - Articulación 1 (Joint 1)
  - Articulación 2 (Joint 2)
  - Velocidad de simulación
  - Pausa y continuación
- Usa `POSITION_CONTROL` para mover las articulaciones.
- Permite ajustar el tiempo entre pasos de simulación basado en el control de velocidad.

## 🐳 Configuración de Docker (`Dockerfile`)

- **Imagen base**: `python:3`
- **Paquetes de sistema instalados**:
  - `xvfb`, `x11-utils`, `libgl1-mesa-glx` (soporte gráfico).
- **Paquetes de Python instalados**:
  - `pybullet`
  - `numpy`
- **Archivos copiados**:
  - `main.py`
  - `two_joint_robot_custom.urdf`
- **Comando de inicio**:
  - Ejecuta automáticamente `main.py` con Python 3.

## 🚀 Cómo construir y correr el contenedor

1. Construir la imagen:

```bash
docker build -t robot-simulator .
```

2. Correr el contenedor con soporte gráfico:

```bash
xhost +local:docker
docker run --rm -it \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    robot-simulator
```

## 🎯 Requisitos

- Docker instalado en el sistema host.
- Servidor X11 habilitado para la visualización gráfica.
- Permitir acceso gráfico desde contenedores (usando `xhost`).

## 📷 Resultados esperados

Al ejecutar el contenedor:
- Aparecerá una ventana PyBullet.
- Se podrá controlar las articulaciones del robot con sliders en tiempo real.
  
[Robot-sim-docker.webm](https://github.com/user-attachments/assets/c27c4ecf-8a1a-474b-b320-de53277bf460)








