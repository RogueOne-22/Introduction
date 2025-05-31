import pygame
import random
import os

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceMax Tarea")

# Cargar imágenes y sonidos
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
img_path = os.path.join(assets_path, 'images')
snd_path = os.path.join(assets_path, 'sounds')

player_img = pygame.image.load(os.path.join(img_path, 'player.png')).convert_alpha()
enemy_imgs = [
    pygame.image.load(os.path.join(img_path, f'enemy{i+1}.png')).convert_alpha()
    for i in range(3)
]
bullet_img = pygame.image.load(os.path.join(img_path, 'bullet.png')).convert_alpha()
background = pygame.image.load(os.path.join(img_path, 'background.jpg')).convert()

laser_sound = pygame.mixer.Sound(os.path.join(snd_path, 'laser.ogg'))
explosion_sound = pygame.mixer.Sound(os.path.join(snd_path, 'explosion.ogg'))

# Clases
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 2
        self.lives = 10
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.image = enemy_imgs[type % len(enemy_imgs)]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = 1
        self.shoot_delay = random.randint(120, 240)

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 30
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 5)
            enemy_bullets.add(bullet)
            all_sprites.add(bullet)
            self.shoot_delay = random.randint(120, 240)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0 or self.rect.top > HEIGHT:
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_imgs[0], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.y = 50
        self.speed = 3
        self.health = 20
        self.max_health = 20
        self.shoot_delay = 60

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed *= -1
        self.shoot_delay -= 1
        if self.shoot_delay <= 0:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, 7)
            enemy_bullets.add(bullet)
            all_sprites.add(bullet)
            self.shoot_delay = 60

# Inicialización de juego
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

level = 1
boss_fight = False
boss = None
paused = False
boss_defeated = False

def spawn_enemies():
    for row in range(3):
        for column in range(8):
            enemy = Enemy(40 + column * 60, 40 + row * 50, row)
            all_sprites.add(enemy)
            enemies.add(enemy)

spawn_enemies()

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_r:
                level = 1
                player.lives = 3
                player.score = 0
                boss_fight = False
                boss_defeated = False
                all_sprites.empty()
                enemies.empty()
                bullets.empty()
                enemy_bullets.empty()
                player.rect.centerx = WIDTH // 2
                all_sprites.add(player)
                spawn_enemies()
            elif event.key == pygame.K_SPACE and not paused and not boss_defeated:
                bullet = Bullet(player.rect.centerx, player.rect.top, -10)
                all_sprites.add(bullet)
                bullets.add(bullet)
                laser_sound.play()
            elif event.key == pygame.K_ESCAPE and boss_defeated:
                running = False

    if not paused and not boss_defeated:
        all_sprites.update()

        if not boss_fight:
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                explosion_sound.play()
                player.score += 100

            if pygame.sprite.spritecollide(player, enemies, True):
                player.lives -= 1
                if player.lives <= 0:
                    running = False

            if len(enemies) == 0:
                if level == 1:
                    boss_fight = True
                    boss = Boss()
                    all_sprites.add(boss)
                else:
                    running = False
        else:
            for bullet in pygame.sprite.spritecollide(boss, bullets, True):
                boss.health -= 1
                explosion_sound.play()
            if boss.health <= 0:
                player.score += 1000
                boss.kill()
                boss_fight = False
                boss_defeated = True
                level += 1

        if pygame.sprite.spritecollide(player, enemy_bullets, True):
            player.lives -= 1
            if player.lives <= 0:
                running = False

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 30)
    screen.blit(font.render(f"Score: {player.score}  Lives: {player.lives}", True, (255,255,255)), (10, 10))

    if paused:
        pause_text = font.render("PAUSA", True, (255, 255, 0))
        screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2))

    if boss_fight and boss:
        bar_width = 100
        health_ratio = boss.health / boss.max_health
        health_bar = pygame.Rect(boss.rect.x, boss.rect.top - 10, int(bar_width * health_ratio), 5)
        pygame.draw.rect(screen, (255, 0, 0), health_bar)
        pygame.draw.rect(screen, (255, 255, 255), (boss.rect.x, boss.rect.top - 10, bar_width, 5), 1)

    if boss_defeated:
        win_text = font.render("¡Ganaste! R - Reiniciar | ESC - Salir", True, (0, 255, 0))
        screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()

