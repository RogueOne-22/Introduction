# Configuración del Entorno con Docker, ROS2 y Gazebo

> [!Important]
> Para mayor información revisar el documento "Tarea_6-2 - Gazebo.pdf" (contine más de 5 páginas)
---

Este proyecto muestra cómo configurar un entorno para simulaciones robóticas utilizando **Docker**, **ROS2** y **Gazebo**. Se detallan los pasos necesarios para instalar las herramientas, construir el contenedor y visualizar simulaciones de diferentes robots incluidos en Gazebo.

Repositorio base utilizado:  
[Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo](https://github.com/mateus-mos/Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo)

---

## 🧰 Pasos de instalación

### 1. Clonar el Repositorio del Proyecto

Inicialmente se crea una carpeta para el proyecto, al ingresar al directorio elegido y se 
ejecuta el comando de Git clone con a la dirección del repositorio desde la terminal:

```bash
git clone https://github.com/mateus-mos/Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo
cd Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo
```

---

### 2. Instalar Docker Engine

A continuación, se debe instalar Docker, este paso es opcional ya que se contraba instalo. 

Se puede ejecutar el contenedor "Hello world" para confirmar la correcta instalación de la herramienta.
[Guía oficial de instalación para Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

```bash
docker run hello-world
```

---

### 3. Crear el Grupo Docker

Crear un grupo docker y agregar a los usuarios, para facilitar el uso de comandos sin
necesidad de sudo.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Más información en:  
[Posinstalación de Docker en Linux](https://docs.docker.com/engine/install/linux-postinstall/)

---

### 4. Instalar Docker Compose

El siguiente paso en la instalación es el Docker Compose, herramienta usada
para manejar aplicaciones Docker con múltiples contenedores.

```bash
sudo apt-get install docker-compose-plugin
```

---

### 5. Construir y Ejecutar el Contenedor Docker

Tras instalar Docker y Docker Compose, se debe construir el contenedor y ejecutarlo,
mostrando la ejecución de ROS2 y Gazebo.

* Para versiones recientees se debe hacer uso de docker compose, en cambio de docker-
compose.

```bash
docker compose build
docker compose up
```

Esto descargará e instalará ROS2 y Gazebo dentro del contenedor.

---

### 6. Acceder al Contenedor en Ejecución

Abrir una terminal dentro del contenedor con:

```bash
docker exec -it Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo bash
```

>[!Note]
>Reemplaza Hands-On-Workshop-TurtleBot-3-Simulation-in-Gazebo por el ID o nombre real del contenedor que se este ejecutando.

![Screenshot from 2025-04-23 22-50-05](https://github.com/user-attachments/assets/8d5016fd-08c5-4ae5-b404-fd72a0715ef7)
---

### 7. Habilitar la Interfaz para Gazebo

Se configura el acceso a la interfaz desde dentro del contenedor, esencial para el funcionamiento de Gazebo. 

```bash
xhost +local:docker
```
Esto permite que el contenedor Docker use tu servidor gráfico para mostrar ventanas como la de Gazebo.

![Screenshot from 2025-04-24 17-46-08](https://github.com/user-attachments/assets/6d755b4c-71be-44f4-90ef-8ca6acdf66d1)

---

### 8. Abrir Gazebo 

Finalmente, se muestra cómo ejecutar Gazebo dentro del contenedor y luego, se escoje una simulación de robot "NaO". 

```bash
ros2 launch gazebo_ros gazebo.launch.py
```
EL código anterior se ejecuta automaticamente.

![Screenshot from 2025-04-24 17-49-17](https://github.com/user-attachments/assets/d1387054-25c9-4e96-b1e2-65bb934fdb51)


Esto iniciará Gazebo con los modelos de robot disponibles.

---![Screenshot from 2025-04-24 17-55-26](https://github.com/user-attachments/assets/b118575c-5326-4737-b99a-b13f36fa09af)



## 🧪 Resultados esperados

- Simulación de robots como Pepper dentro de Gazebo.
- Visualización 3D en tiempo real.
---

## 📌 Recomendaciones

- Usa Docker para tener un entorno portátil.
- Verifica siempre que tus versiones de ROS2, Gazebo y Docker Compose sean compatibles en caso de crear un contenerdor propio.

---
