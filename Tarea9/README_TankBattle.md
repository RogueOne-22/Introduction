# 🔫 Tank Battle Mejorado

## Docker Hub: [Pausc0222 - pygame-games](https://hub.docker.com/r/pausc0222/pygame-games)

Una versión mejorada de un juego de tanques 2D desarrollado en Python con [Pygame](https://www.pygame.org/). Controla un tanque, dispara a los enemigos y divierte!

---

## 🕹️ Controles

| Tecla        | Acción              |
|-------------|---------------------|
| `W/A/S/D` o `↑←↓→` | Mover tanque          |
| `ESPACIO`    | Disparar            |
| `ENTER`      | Pausar/reanudar     |

---

## ▶️ Cómo ejecutar

1. Instala Python 3.8 o superior.
2. Instala Pygame si aún no lo tienes:
   ```bash
   pip install pygame
   ```
3. Ejecuta el juego:
   ```bash
   python Tanques_mejorado.py
   ```

---

## 🧠 Partes clave en el código:

### 🎨 1. **Diseño de tanques**
Los tanques ahora simulan una forma más parecida a un carro:
```python
self.image = pygame.Surface((50, 20), pygame.SRCALPHA)
pygame.draw.rect(self.image, color, (0, 5, 50, 10))  # cuerpo
pygame.draw.rect(self.image, GRAY, (5, 0, 10, 5))    # cabina izquierda
pygame.draw.rect(self.image, GRAY, (35, 0, 10, 5))   # cabina derecha
```

---

### 🧘‍♂️ 2. **Pausar con ENTER**
Se agregó una variable `paused` y lógica de evento:
```python
elif event.key == pygame.K_RETURN:
    paused = not paused

if paused:
    # Muestra texto "PAUSADO" y detiene actualizaciones
    ...
    continue
```

---

### ❤️ 3. **Vida visible de los enemigos**
Cada enemigo tiene una barra de vida renderizada encima de su sprite:
```python
for enemy in enemies:
    pygame.draw.rect(screen, RED, (enemy.rect.x, enemy.rect.y - 10, 50, 5))
    pygame.draw.rect(screen, GREEN, (enemy.rect.x, enemy.rect.y - 10, 50 * (enemy.health / 100), 5))
```

---

### 📋 4. **Controles en pantalla**
Los controles se muestran al pie de la pantalla en todo momento:
```python
controls_text = font.render("WASD/↑↓←→: mover   ESPACIO: disparar   ENTER: pausar", True, WHITE)
screen.blit(controls_text, (10, HEIGHT - 40))
```
---
