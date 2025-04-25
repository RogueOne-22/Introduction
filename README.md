> [!Note]
> Actulización - Segundo corte:

# Tarea 6:  Pepper, PyBullet, ROS2 y Gazebo

Dentro de este repositorio  se encuentra la carperta "Tarea 6" contiene informacion y ejemplos básicos para el desarrollo de aplicaciones de robótica simulada utilizando:

- Librerías esenciales para el robot humanoide **Pepper**
- Simulación brazo robotico con **PyBullet**
- Entorno de simulación con **ROS2 y Gazebo** vía Docker y visualización de Pepper

---

## 📦 Librerías principales para el robot Pepper

A continuación se listan algunas de las principales librerías utilizadas para desarrollar aplicaciones en el robot Pepper utilizando Python:

- **qi**: Conecta con los servicios internos de NAOqi.
- **almath**: Librería matemática de SoftBank Robotics para cinemática y transformaciones.
- **motion (ALMotion)**: Controla articulaciones, posturas y movimientos del robot.
- **argparse**: Gestión de argumentos por consola.
- **sys** y **os**: Interacción con el sistema operativo.
- **json** y **httplib**: Comunicación con servicios web y manejo de datos.

---

## 🧠 Simulación con PyBullet

**PyBullet** es un motor de simulación física de código abierto. Se utiliza para simular dinámicas, colisiones y articulaciones, ideal para probar algoritmos antes de implementarlos en hardware real.

### Características:
- Simulación en tiempo real de robots, sensores y entornos 3D.
- Fácil integración con Python.
- Renderizado visual básico para pruebas rápidas.
  
[Pybullet Start Guide]([https://pages.github.com/](https://raw.githubusercontent.com/bulletphysics/bullet3/master/docs/pybullet_quickstartguide.pdf)

### Se plantea los pasos de intalación en bash y la simulación de un brazo 
![Entorno Pybullet](https://images.app.goo.gl/eE6MFWKDSWs7NXhXA)

---
## 🚀 Instalación de ROS2 y Gazebo vía Docker
Docker + ROS 2 + Gazebo Application

Esta aplicación utiliza **Docker** para contenerizar un entorno de simulación robótica basado en **ROS 2** y **Gazebo**.  
Permite ejecutar simulaciones de robots de forma portátil, aislada y reproducible, sin necesidad de instalar las herramientas directamente en el sistema operativo.

## Tecnologías

- **Docker**: Para crear entornos de desarrollo aislados y reproducibles.
- **ROS 2**: Framework de software robótico para comunicaciones, control y simulaciones.
- **Gazebo**: Motor de simulación 3D de robots, sensores y entornos físicos.

## Beneficios

- Entorno listo para usar con un solo comando (`docker run`).
- Sin conflictos de versiones o dependencias locales.
- Facilita el desarrollo, la simulación y las pruebas de robots en ROS 2.
- Fácil de compartir con otros usuarios mediante imágenes Docker.

  ![Simulación Nao pepper en Gazebo](https://images.app.goo.gl/3HoQz5rXF3v3wE4n9)
