# Introducción a PyBullet

> [!Important]
> Para visualizar mas información acerca del desarrollo de la actividad revisar el archivo "Tarea_6-1 - Pybullet.pdf" (más de 5 páginas)

---

## ¿Qué es PyBullet?

**PyBullet** es un módulo de Python para la simulación de física en tiempo real.  
Está basado en el motor físico **Bullet**, una biblioteca rápida y de código abierto utilizada en videojuegos, robótica y aprendizaje por refuerzo.

---

## 🛠️ Características principales

- Simulación de cuerpos rígidos 
- Detección de colisiones
- Cinemática y dinámica para robots
- Simulación de sensores (cámaras, IMUs, sensores de fuerza)
- API sencilla en Python

---

## 🧪 Instalación

Instala PyBullet con pip:

```bash
pip install pybullet
```

```bash

sudo apt-get install python3
sudo apt install python3-pip
sudo pip3 install pybullet
python3 -m pip show pybullet
```
![Screenshot from 2025-04-21 20-21-43](https://github.com/user-attachments/assets/767f303a-3213-4fe5-b7e6-f9e2a2bee23b)
![Screenshot from 2025-04-21 20-28-02](https://github.com/user-attachments/assets/bfed1225-486c-481f-888c-a6f804fe55a8)
![Screenshot from 2025-04-21 20-54-38](https://github.com/user-attachments/assets/87462556-9366-437e-861c-4514392c838e)

## 🛠️ Utilidades con PyBullet:

- Importar y animar modelos URDF (usados en ROS)
- Usar cinemática inversa para mover brazos robóticos
- Recoger datos de sensores
- Crear entornos fı́sicos personalizados
- Entrenar agentes con aprendizaje por refuerzo (RL)
  
[PyBullet Quickstart Guide](https://raw.githubusercontent.com/bulletphysics/bullet3/master/docs/pybullet_quickstartguide.pdf)

## 🤖 Simulación de Brazo Robótico en PyBullet

Se simula un brazo robótico con 7 grados de libertad tomado del repositorio kuka_experimental. La simulación se desarrolla en tres etapas:
    - Inicialización del entorno y parámetros básicos
    - Fijación del brazo en el entorno para estabilidad
    - Manejo matemático de articulaciones con control individual
    
#Código de Simulación 1 (sin base fija)

```python
#Codigo inicial para estelbecer parametros del robot y genera la simulacion de una caida,  buscando una torcion de 0.2 metros en cada articulacion sin una base fija
    
    #importa librerias necesarias
    import pybullet
    import time
    import pybullet_data
    
    #Genera Gui de  pybullet 
    physicsClient= pybullet.connect(pybullet.GUI) 
    
    #Set PybulletData
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    
    #load plane - simulation ground from import pybullet_data
    planeID=pybullet.loadURDF("plane.urdf")
    
    #Load Robot from directory
    robot= pybullet.loadURDF("kuka_experimental/kuka_lbr_iiwa_support/urdf/lbr_iiwa_14_r820.urdf")
    
    #How many joints?
    pybullet.getNumJoints(robot)
    
    #Get info position, orientation
    position, orientation=pybullet.getBasePositionAndOrientation(robot)
    
    #Info for Joint No.7
    pybullet.getJointInfo(robot,7)
    
    joint_positions=[j[0] for j in pybullet.getJointStates(robot,range(7))]
    joint_positions
    
    #Info for world orientation
    world_position, world_orientation=pybullet.getLinkState(robot,2)[:2]
    
    world_position
    world_orientation
    
    pybullet.setGravity(0,0,-9.81)
    
    #No real time Simulation - by default
    pybullet.setRealTimeSimulation(0) 
    
    pybullet.setJointMotorControlArray(robot, range(7), pybullet.POSITION_CONTROL, targetPositions=[0.2]*7)
    
    #simula ejecucion dado que no esta en tiempo real 
    for _ in range(10000):
    	pybullet.stepSimulation()
    	time.sleep(1./240.)
```
![Screenshot from 2025-04-24 18-57-56](https://github.com/user-attachments/assets/c62a4f47-84af-47e9-8d44-7a9e5e0669e9)
![Screenshot from 2025-04-24 19-42-27](https://github.com/user-attachments/assets/66a8e8ea-77c2-4da3-9eba-c91a2cde6027)
![Screenshot from 2025-04-24 20-10-54](https://github.com/user-attachments/assets/56d964e1-39cd-458e-98d7-58ec59552f63)

# Código simulación 2:
```python
#Esta version agrega una base fija permitiendo que se pueda realizar la torcion de 1.5 metros en cada articulacion

    #Reset simulation
    pybullet.resetSimulation()
    
    #Start Over
    import pybullet
    import time
    import pybullet_data
     
    physicsClient= pybullet.connect(pybullet.GUI) 
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeID=pybullet.load("plane.urdf")
    robot= pybullet.loadURDF("kuka_experimental/kuka_lbr_iiwa_support/urdf/lbr_iiwa_14_r820.urdf",[0,0,0],useFixedBase=1)
    pybullet.setGravity(0,0,-9.81)
    pybullet.setRealTimeSimulation(0)
    pybullet.setJointMotorControlArray(robot, range(7), pybullet.POSITION_CONTROL, targetPositions=[1.5]*7)
    
    for _ in range(300):
    	pybullet.stepSimulation()
    	time.sleep(1./10.)
  ```
![Screenshot from 2025-04-25 04-18-49](https://github.com/user-attachments/assets/f2854e21-0db4-4eeb-8250-7bac65780c76)
![Screenshot from 2025-04-25 04-21-56](https://github.com/user-attachments/assets/abcba1ee-493c-42af-a1d1-e6c9e7e18ad5)

# Código simulación 3:
```python
#Version Final: Se agrega cinemática inversa para realizar adecuadamente la torcion de 1.5 metros en cada articulacion
#Reset simulation
    import pybullet
    import time
    import pybullet_data
     
    physicsClient= pybullet.connect(pybullet.GUI) 
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    planeID=pybullet.loadURDF("plane.urdf")
    robot= pybullet.loadURDF("kuka_experimental/kuka_lbr_iiwa_support/urdf/lbr_iiwa_14_r820.urdf",[0,0,0],useFixedBase=1)
    pybullet.setGravity(0,0,-9.81)
    pybullet.setRealTimeSimulation(0)
    Orientation=pybullet.getQuaternionFromEuler([3.14,0.,0.])
    
    targetPositionsJoints=pybullet.calculateInverseKinematics(robot,7,[0.1,0.1,0.4],targetOrientation=Orientation)
    
    pybullet.setJointMotorControlArray(robot, range(7),pybullet.POSITION_CONTROL,targetPositions=targetPositionsJoints)
    
    for _ in range(300):
    	pybullet.stepSimulation()
    	time.sleep(1./10.) 
  ```

![Screenshot from 2025-04-25 04-24-13](https://github.com/user-attachments/assets/f64fd61d-a0a9-4600-8f5f-19a1f66922a5)

[Screencast from 04-24-2025 09:18:15 PM.webm](https://github.com/user-attachments/assets/89302a6e-0850-403c-85df-1d1e2d9c9b3a)

---
### 🛠️Conclusiones

El uso de PyBullet como motor de simulación fı́sica en proyectos de robótica y simulación
ofrece múltiples ventajas, especialmente en entornos académicos de simulación y de desarrollo rápido. 

- PyBullet permite una simulación realista de dinámicas fı́sicas, incluyendo  articulaciones robóticas, gravedad, etc. Lo que facilita el desarrollo y prueba de algoritmos
sin necesidad de hardware.
- Su integración con Python ayuda a la fácil programación y automatización de pruebas,convirtiéndolo en una herramienta accesible para estudiantes.
- La posibilidad de visualizar en tiempo real las simulaciones mediante interfaces gráficas,mejora la comprensión del comportamiento del robot.
- PyBullet incluye modelos de robots, sensores y escenarios, reduciendo el tiempo deconfiguración inicial y permitiendo centrarse en el desarrollo del sistema o del control.
- Su uso debe estar orientado principalmente a entornos de desarrollo, educación y validación de pruebas.

