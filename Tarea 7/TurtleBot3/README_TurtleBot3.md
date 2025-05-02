# 🤖 Simulación del TurtleBot3 con ROS Noetic

Este proyecto implementa una simulación del robot móvil TurtleBot3 utilizando ROS Noetic y el simulador Gazebo. Se integran herramientas de SLAM para la exploración y mapeo de entornos, evaluando los modelos Burger y Waffle.

---

## 🧩 Descripción General

El **TurtleBot3** es un robot modular, compacto y económico, desarrollado por **ROBOTIS** en colaboración con la comunidad ROS. Está diseñado para aplicaciones educativas, de investigación y prototipado rápido.

---

## 🛠️ Entorno Docker

Se utiliza un contenedor Docker para ejecutar la simulación con la siguiente configuración:

### Imagen base
```dockerfile
FROM osrf/ros:noetic-desktop-full
```

### Instalación de paquetes
```dockerfile
RUN apt-get update && apt-get install -y \
    ros-noetic-turtlebot3 \
    ros-noetic-turtlebot3-simulations \
    ros-noetic-slam-gmapping
```

### Variables de entorno
```dockerfile
ENV TURTLEBOT3_MODEL=waffle_pi
RUN echo "export TURTLEBOT3_MODEL=w" >> ~/.bashrc
```

### Comando de inicio
```dockerfile
CMD bash -c "source /opt/ros/noetic/setup.bash && \
roslaunch turtlebot3_gazebo turtlebot3_house.launch"
```

---

## 🧪 Resultados de la Simulación

### 🔹 Modelo Burger
- Mejores resultados en entornos abiertos.
- Sensor LiDAR de gran alcance y buena velocidad de respuesta.
- Adecuado para mapeo rápido de áreas con obstáculos dispersos.

### 🔹 Modelo Waffle
- Adecuado para espacios cerrados y angostos.
- Sensor LiDAR + cámara 3D (Intel RealSense).
- Mejor capacidad de percepción tridimensional.

---

## 📌 Conclusiones

- Ambos modelos son funcionales y emplean el mismo sensor LiDAR.
- Waffle/Waffle Pi añade percepción 3D gracias a la cámara RealSense.
- Burger es más ligero y ágil.

---

## 🔗 Recursos

- Manual oficial: [emanual.robotis.com](https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/)
- Sitio oficial: [turtlebot.com](https://www.turtlebot.com/turtlebot3/)
