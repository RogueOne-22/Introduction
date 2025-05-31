# 🚀 Space Defender

Un juego arcade tipo Galaga desarrollado con Python y Pygame.

---

## 🎮 Cómo jugar

- ← / → : Mover la nave
- `Espacio` : Disparar
- `P` : Pausar
- `R` : Reiniciar el juego
- `ESC` : Salir (solo aparece tras vencer al jefe final)

---

## 🔄 Mejoras

### 🛠️ Reflección de las naves
Se implementó un sistema basado en sprites con las siguientes clases:
```
class Player(pygame.sprite.Sprite):
    def update(self):

class Enemy(pygame.sprite.Sprite):
    def update(self):
      
```

### 🎮 Jugabilidad y controles
Control de pausa y reinicio desde eventos del teclado:
```
elif event.key == pygame.K_p:
    paused = not paused
elif event.key == pygame.K_r:
    reiniciar_juego()
```

### 👾 Disparos enemigos
Tanto enemigos como el jefe disparan:
```
if self.shoot_delay <= 0:
    bullet = Bullet(self.rect.centerx, self.rect.bottom, 5)
```

Colisiones con balas enemigas:
```
if pygame.sprite.spritecollide(player, enemy_bullets, True):
    player.lives -= 1
```

### 👑 Jefe final
El jefe aparece tras eliminar enemigos, con barra de vida:
```
if len(enemies) == 0:
    boss = Boss()
    all_sprites.add(boss)
```
---

## 🧠 Lógica del juego

- Enemigos se mueven de manera horizontal hasta llegar cerca al jugador.
- Cuando todos los enemigos son eliminados, aparece un jefe final.
- Si el jugador recibe balas, pierde vidas.
- Al vencer al jefe, se puede reiniciar o salir del juego.

---

## 📁 Estructura del juego
```
space_game/
├── space.py              # Archivo principal del juego
└── assets/
    ├── images/           # Sprites del jugador, enemigos, balas, fondo
    └── sounds/           # Sonidos de disparo y explosión
```
---
