>[!Important]
>Para mayor información acerca de las librerias revisar el archivo "Tarea_6 - Librerias V2.pdf" (más de 5 páginas)

# Tarea 6: Librerías para el Robot Pepper - PT1

---

## 📘 Introducción

Este documento presenta una descripción de las principales librerías utilizadas en el desarrollo de aplicaciones para el robot **Pepper**. Se indican una descripción general y los requisitos de software necesarios para su correcto funcionamiento.

---

## 💻 Requisitos de Software

- Python 2.7 o 3.x (dependiendo del entorno NAOqi utilizado)
- NAOqi SDK: entorno de desarrollo oficial para Pepper
- Choregraphe Suite
- Acceso a red local del robot
- Conexión SSH

---

## 📚 Librerías

### 1. `qi`

**Descripción:** Librería del framework NAOqi para conectar y gestionar módulos internos del robot.  
**Documentación:** [qi SDK Documentation](http://doc.aldebaran.com/2-5/dev/naoqi/index.html)
```python
import qi
session = qi.Session()
session.connect("tcp://192.168.1.106")
motion_service = session.service("ALMotion")
```
### 2.  `argparse`

**Descripción:** Manejo de argumentos de línea de comandos.\
**Documentación:** [argparse — Python Docs ](https://docs.python.org/3/library/argparse.html)
```python
'import argparse'
'parser = argparse.ArgumentParser()'
'parser.add_argument("--ip", type=str, default="127.0.0.1")'
'args = parser.parse_args()'
```
### 3. `sys`

**Descripción:** Acceso al sistema, argumentos del script, salida, etc. \ 
**Documentación:** [sys — Python Docs](https://docs.python.org/3/library/sys.html)

```python
import sys
if len(sys.argv) < 2:
    sys.exit("Falta la IP del robot")
```
### 4. `OS`

**Descripción:** Interacción con el sistema operativo (archivos, rutas, etc.)\
**Documentación:**[ os — Python Docs] (https://docs.python.org/3/library/os.html)
```python
import os
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)
```
### 5. `almath`

**Descripción:** Librería matemática especializada en robótica, cinemática y geometría.\
**Documentación:** [almath — NAOqi SDK](http://doc.aldebaran.com/2-5/naoqi/motion/control-cartesian.html)
```python
import almath
transform = almath.Transform()
transform.r1_c4 = 0.5
print(transform.toVector())
```
### 6. `math`

**Descripción:** Operaciones matemáticas comunes (trigonometría, logaritmos, etc.)\
**Documentación:** math — [Python Docs](https://docs.python.org/3/library/math.html)
```python
import math
print(math.sin(math.radians(90)))
```

### 7. `motion (ALMotion)`

**Descripción:** Control de movimientos del robot: articulaciones, posturas, locomoción.\
**Documentación:** [ALMotion — NAOqi SDK] 
```python
motion = session.service("ALMotion")
motion.moveTo(0.5, 0, 0)
```

### 8. `httplib / http.client`

**Descripción:** Comunicación HTTP con servicios web. En Python 3, usar http.client.
**Documentación:** [http.client — Python Docs](https://docs.python.org/3/library/http.client.html)
```python
import http.client
conn = http.client.HTTPConnection("example.com")
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status)
```
### 9. `json`

**Descripción:** Manejo de datos JSON. Esencial para APIs y configuración.
Estas librerías forman parte del ecosistema de desarrollo para Pepper. Se recomienda explorar sus respectivas documentaciones oficiales de acuerdo a la necesidad del usuario.
**Documentación:** [json — Python Docs](https://docs.python.org/3/library/json.html)
```python
import json
data = {"nombre": "Pepper", "edad": 3}
print(json.dumps(data))
```
---
📝 Nota final

Estas librerías forman parte del ecosistema de desarrollo para Pepper. Se recomienda explorar sus respectivas documentaciones oficiales de acuerdo a la necesidad del usuario.

---
📚 Bibliografía

 - [SoftBank Robotics. (2023). NAOqi Framework](http://doc.aldebaran.com/2-5/index.html)
 - [Python Software Foundation. (2023). Python Documentation](https://docs.python.org/3/)
 - [SoftBank Robotics. (2023). Motion API](http://doc.aldebaran.com/2-5/naoqi/motion/almotion.html)
 - [item Aldebaran Robotics. (2018). Choregraphe SDK](http://doc.aldebaran.com/2-5/software/choregraphe/index.html)
