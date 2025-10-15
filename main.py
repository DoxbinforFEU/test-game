import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Destroy The Roids")

BG = pygame.transform.scale(pygame.image.load("3d-space-scene.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
ROID_WIDTH = 20
ROID_HEIGHT = 30
ROID_VEL = 5

FONT = pygame.font.SysFont("bbhsansbogle", 40)

def draw(player, elapsed_time, roids):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "red", player)
    
    for roid in roids:
        pygame.draw.rect(WIN, "grey", roid)
    
    pygame.display.update()

def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()    
    elapsed_time = 0

    roid_add_increment = 2000
    roid_count = 0

    roids = []
    hit = False

    while run:
        roid_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if roid_count > roid_add_increment:
            for _ in range(5):
                roid_x = random.randint(0, WIDTH - ROID_WIDTH) 
                roid = pygame.Rect(roid_x, -ROID_HEIGHT, ROID_WIDTH, ROID_HEIGHT)
                roids.append(roid)

            roid_add_increment = max(500, roid_add_increment - 50)
            roid_count = 0    

        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL >= 0:
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.height <= HEIGHT:
            player.y += PLAYER_VEL

        for roid in roids[:]:
            roid.y += ROID_VEL
            if roid.y > HEIGHT:
                roids.remove(roid)
            elif roid.y + roid.height >= player.y and roid.colliderect(player):
                roids.remove(roid)
                hit = True
                break
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)
            break

        draw(player, elapsed_time, roids)

    pygame.quit()

if __name__ == "__main__":
    main()
    