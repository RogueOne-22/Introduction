# 🎮 Tetris Multinivel en Python

Este es un juego de Tetris desarrollado en Python utilizando la biblioteca [Pygame](https://www.pygame.org/). Incluye características como múltiples niveles, pausa, reinicio, nuevas formas de bloques, interfaz tipo retro y control de rotación.

---

## 🧱 Características

- Modo clásico de Tetris con caída automática de piezas.
- Sistema de niveles: sube de nivel al alcanzar ciertos puntos.
- Pausa con `ENTER`.
- Reinicio con `CTRL`.
- Nuevas formas adicionales además de las clásicas.
- Controles visibles en pantalla.
- Márgenes visibles del campo de juego.

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
   python Tetris_final_corregido.py
   ```

---

## 🧠 Estructura del código

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

## ✨ Créditos

- Hecho con ❤️ en Python y Pygame.
- Inspirado en el clásico juego de Tetris.
