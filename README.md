> [!Note]
> Actulización - Segundo corte: Scroll down para el  resumen de las diferentes actividades (Tarea 6 y 7) \
> Para mayor informacion revisar los documentos adjuntos en las carpetas de cada tarea

# Tarea 6:  Pepper, PyBullet, ROS2 y Gazebo

Dentro de este repositorio  se encuentra la carperta "Tarea 6" contiene informacion y ejemplos básicos para el desarrollo de aplicaciones de robótica simulada utilizando:

- Librerías esenciales para el robot humanoide **Pepper**
- Simulación brazo robotico con **PyBullet**
- Entorno de simulación con **ROS2 y Gazebo** vía Docker y visualización de Pepper

---

## 📦 Librerías principales para el robot Pepper

A continuación se listan algunas de las principales librerías utilizadas para desarrollar aplicaciones en el robot Pepper:

- **qi**: Conecta con los servicios internos de NAOqi.
- **almath**: Librería matemática de SoftBank Robotics para cinemática y transformaciones.
- **motion (ALMotion)**: Controla articulaciones, posturas y movimientos del robot.
- **argparse**: Gestión de argumentos por consola.
- **sys** y **os**: Interacción con el sistema operativo.
- **json** y **httplib**: Comunicación con servicios web y manejo de datos.

---

## Simulación con PyBullet

**PyBullet** es un motor de simulación física de código abierto. Se utiliza para simular dinámicas, posicionamiento y articulaciones de robots, ideal para probar algoritmos antes de implementarlos.

### Características:
- Simulación de robots, sensores y entornos 3D.
- Fácil integración con Python.
- Interfase visual básico para pruebas rápidas.
  
[Pybullet Start Guide] [https://pages.github.com/](https://raw.githubusercontent.com/bulletphysics/bullet3/master/docs/pybullet_quickstartguide.pdf)

### Se plantea los pasos de intalación en bash y la simulación de un brazo 

![Screenshot from 2025-04-24 20-10-54](https://github.com/user-attachments/assets/95527279-d504-4ba3-b5f9-14c91764a3f4)

[Screencast from 04-24-2025 09:18:15 PM.webm](https://github.com/user-attachments/assets/2c4ea4b7-37f7-4dd8-aa42-925c335a40bb)

---
## Instalación de ROS2 y Gazebo vía Docker
Docker + ROS 2 + Gazebo Application

Esta aplicación utiliza **Docker** para contenerizar un entorno de simulación robótica basado en **ROS 2** y **Gazebo**.  
Permite ejecutar simulaciones de robots de forma portátil, sin necesidad de instalar las herramientas directamente en el sistema operativo.

## Herramientas

- **Docker**: Para crear entornos de desarrollo aislados y reproducibles.
- **ROS 2**: Framework de software robótico para comunicaciones, control y simulaciones.
- **Gazebo**: Motor de simulación 3D de robots, sensores y entornos físicos.
![Screenshot from 2025-04-24 17-55-26](https://github.com/user-attachments/assets/097d9322-b51b-49e4-9a0d-90aaebefcd4e)

  
---

# 🚀 Tarea 7: PT1: Proyecto: Simulación de Robot de Dos Articulaciones en  ejecutado desde Docker

Este proyecto consiste en la simulación de un robot de dos articulaciones usando **PyBullet**, ejecutado dentro de un contenedor Docker configurado para soportar entorno gráfico.

La simulación permite:
- Controlar el movimiento de las dos articulaciones mediante sliders.
- Ajustar dinámicamente la velocidad de simulación.
- Pausar y reanudar la simulación en tiempo real.

## 🛠️ Archivos utilizados

- **`main.py`**: Script principal que lanza la simulación 
- **`two_joint_robot_custom.urdf`**: Archivo URDF que define la estructura del robot.
- **`Dockerfile`**: Configura un contenedor Docker.

## 🚀 Cómo ejecutar el contenedor


1. Correr el contenedor con soporte gráfico:

```bash
xhost +local:docker
docker run --rm -it \
    --env="DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    robot-simulator
```

## 📷 Resultados esperados

 [Demostracion.webm](https://github.com/user-attachments/assets/cea2c372-31bd-427f-8e39-27fc9e0883bc)


 # 🤖 Tarea 7: PT2 Simulación del TurtleBot3 con ROS Noetic

Este proyecto implementa una simulación del robot móvil TurtleBot3 utilizando ROS Noetic y el simulador Gazebo. Se integran herramientas de SLAM para la exploración y mapeo de entornos, evaluando los modelos Burger y Waffle.

---

## 🧩 Descripción General

El **TurtleBot3** es un robot modular, compacto y económico, desarrollado por **ROBOTIS** en colaboración con la comunidad ROS. Está diseñado para aplicaciones educativas, de investigación y prototipado rápido.

## 🧪 Resultados de la Simulación

### 🔹 Modelo Burger
- Mejores resultados en entornos abiertos.
- Sensor LiDAR de gran alcance y buena velocidad de respuesta.
- Adecuado para mapeo rápido de áreas con obstáculos dispersos.
- 
![Screenshot from 2025-05-01 19-12-48](https://github.com/user-attachments/assets/fa744ccc-7583-418a-b35b-56fc7ea49dd1)


### 🔹 Modelo Waffle
- Adecuado para espacios cerrados y angostos.
- Sensor LiDAR + cámara 3D (Intel RealSense).
- Mejor capacidad de percepción tridimensional.
- 
![Screenshot from 2025-05-01 19-16-15](https://github.com/user-attachments/assets/1dff06f2-55e2-47fb-8dbf-5de48b28ce37)

>[Note!]
>Los viedos se encuentran en la carpeta de desarollo 
---

## 📌 Conclusiones

- Ambos modelos son funcionales y emplean el mismo sensor LiDAR.
- Waffle/Waffle Pi añade percepción 3D gracias a la cámara RealSense.
- Burger es más ligero y ágil.


 
