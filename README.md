> [!Note]
> Actulización - Segundo corte: Scroll down para el desarollo de las diferentes actividades (Tarea 6 y 7)

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
  
[Pybullet Start Guide]([https://pages.github.com/](https://raw.githubusercontent.com/bulletphysics/bullet3/master/docs/pybullet_quickstartguide.pdf)

### Se plantea los pasos de intalación en bash y la simulación de un brazo 
![Entorno Pybullet](https://images.app.goo.gl/FfdMXZuVKzJGFzeD8)

---
## Instalación de ROS2 y Gazebo vía Docker
Docker + ROS 2 + Gazebo Application

Esta aplicación utiliza **Docker** para contenerizar un entorno de simulación robótica basado en **ROS 2** y **Gazebo**.  
Permite ejecutar simulaciones de robots de forma portátil, sin necesidad de instalar las herramientas directamente en el sistema operativo.

## Herramientas

- **Docker**: Para crear entornos de desarrollo aislados y reproducibles.
- **ROS 2**: Framework de software robótico para comunicaciones, control y simulaciones.
- **Gazebo**: Motor de simulación 3D de robots, sensores y entornos físicos.

  ![Simulación Nao pepper en Gazebo](https://images.app.goo.gl/3HoQz5rXF3v3wE4n9)
---

# 🚀 Tarea 7: Doker, Pybullet, Brazo robotico

---
## Decostrucción Algoritmo del brazo (main.py):

 - Inicializa PyBullet en modo interfez gráfica.
 - Carga el plano del entorno y el robot definido en archivo URDF.
 - Crea sliders:

        Controlar posición de Joint 1 y Joint 2.

        Controlar la velocidad de simulación.

        Botón para pausar o reanudar la simulación.
- ciclos:

        Lee valores de sliders.

        Aplica control de posición a las articulaciones.

        Ajusta la velocidad de simulación

# 📦 Aplicación con Docker

📁 Estructura del Contenedor:

robot-sim-docker/ \
├── Dockerfile \
├── main.py  \            
└── two_joint_robot_custom.urdf  \

📁 Archivos del proyecto 
  📄 Dockerfile
    📄 main.py
      📄 two_joint_robot_custom.urdf
  
  📄 Ejecutar PyBullet en modo GUI con Python3


▶️ Construir y correr el contenedor
  
  -Construir contenedor: 'docker build -t pybullet-robot-sim 
  - Ejecuta el contenedor con GUI
  
  - 

 
