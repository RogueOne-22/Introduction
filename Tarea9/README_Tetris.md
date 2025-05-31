# 🎮 Tetris 

## Docker Hub: [Pausc0222 - pygame-games](https://hub.docker.com/r/pausc0222/pygame-games)

Este es un juego de Tetris desarrollado en Python utilizando la biblioteca [Pygame](https://www.pygame.org/).

---

## 🧱 Características

- Caída automática de piezas.
- Varios niveles.
- Pausa con `ENTER`.
- Reinicio con `CTRL`.
- Controles en pantalla.
- Márgenes visibles.

---

## 🕹️ Controles

| Tecla      | Acción                    |
|------------|---------------------------|
| ← / →      | Mover pieza izquierda/derecha |
| ↓          | Acelerar caída            |
| ↑          | Rotar pieza               |
| ENTER      | Pausar el juego           |
| CTRL       | Reiniciar partida         |

---

## ▶️ Cómo ejecutar

1. Asegúrate de tener **Python 3.8+** instalado.
2. Instala `pygame`:
   ```bash
   pip install pygame
   ```
3. Ejecuta el archivo:
   ```bash
   python3 Tetris_final_corregido.py
   ```

---

## 🧠 Cambios en el código

### `class Pieza`
Representa una ficha del juego. Tiene propiedades como posición, color y rotación. Incluye:
- `obtener_forma()`: genera la forma actual, rotada dinámicamente.
- `rotar_matriz()`: rota la matriz 90°.

### `crear_grid()`
Genera una matriz de 10x20 que representa el campo de juego actual, combinando las piezas ya colocadas.

### `verificar_colision()`
Verifica si una pieza colisiona con los bordes o con otras piezas.

### `limpiar_lineas()`
Elimina filas completas y actualiza el estado de los bloques.

### `dibujar_ventana()`
Dibuja todo en la pantalla: la cuadrícula, la pieza activa, la próxima pieza, puntuación, nivel, controles y bordes.

### `main()`
Contiene el bucle principal del juego:
- Controla la lógica de movimiento, colisiones, pausas, reinicio y condiciones de finalización.
- Usa `pygame.time.get_ticks()` para controlar la velocidad de caída.

---
