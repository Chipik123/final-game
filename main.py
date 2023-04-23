import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Колір екрану
WHITE = (255, 255, 255)

# Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Створення екрану
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Завершення гри
game_over = False

# Швидкість автомобіля
car_speed = 10

# Завантаження зображень
background_image = pygame.transform.scale(pygame.image.load("bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
car_image = "car.png"


# Розміри автомобіля
car_width = 100
car_height = 200

# Початкові координати автомобіля
car_x = (SCREEN_WIDTH / 2) - (car_width / 2)
car_y = SCREEN_HEIGHT - car_height - 10

# Створення перешкод
obstacle_width = 100
obstacle_height = 100
obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
obstacle_y = -obstacle_height

# Головний цикл гри
while not game_over:
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    # Обробка руху автомобіля
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed
    
    # Обробка руху перешкод
    obstacle_y += car_speed / 2
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
    
    # Перевірка на зіткнення
    if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        game_over = True
    
    # Очищення екрану
    screen.fill(WHITE)
    # Відображення зображень
    screen.blit(background_image, (0, 0))
    screen.blit(car_image, (car_x, car_y))
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    
    # Оновлення екрану
    pygame.display.update()
    
# Завершення Pygame
pygame.quit()