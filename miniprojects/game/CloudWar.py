import pygame
import random
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT,
                           K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

def main():
    screen_width = 800
    screen_height = 600

    # Defender extends sprite.Sprite
    class Defender(pygame.sprite.Sprite):
        def __init__(self):
            super(Defender, self).__init__()
            self.surf = pygame.image.load("E:\\blog_git\\codingbitz\\miniprojects\\game\\images\\jet.jpg")
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect()

        # Moving sprite
        def update(self, pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

            # Keep player on the screen
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen_width:
                self.rect.right = screen_width
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= screen_height:
                self.rect.bottom = screen_height

    # Adding collision impacting object : Enemy
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load("E:\\blog_git\\codingbitz\\miniprojects\\game\\images\\missile.jpg")
            self.surf.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(screen_width + 20, screen_width + 100),
                    random.randint(0, screen_height),
                ))
            self.speed = random.randint(5, 20)

        # Move the sprite based on speed
        def update(self):
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    # Adding non collision impacting object : Cloud
    class Cloud(pygame.sprite.Sprite):
        def __init__(self):
            super(Cloud, self).__init__()
            self.surf = pygame.image.load("E:\\blog_git\\codingbitz\\miniprojects\\game\\images\\cloud.jpg")
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            # The starting position is randomly generated
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(screen_width + 20, screen_width + 100),
                    random.randint(0, screen_height),
                ))

        def update(self):
            self.rect.move_ip(-5, 0)
            if self.rect.right < 0:
                self.kill()

    # Initialize mixer & game
    pygame.mixer.init()
    pygame.init()
    defender = Defender()

    # Setup the clock
    clock = pygame.time.Clock()

    # Create the screen object
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create a custom event
    add_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(add_enemy, 250)
    add_cloud = pygame.USEREVENT + 2
    pygame.time.set_timer(add_cloud, 750)

    # Create groups
    enemies = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(defender)

    pygame.mixer.music.load("E:\\blog_git\\codingbitz\\miniprojects\\game\\sounds\\rain.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(0.4)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

            elif event.type == add_enemy:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == add_cloud:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        # Get the set of keys pressed ,check for user input and then update
        pressed_keys = pygame.key.get_pressed()
        defender.update(pressed_keys)

        # Update positions
        enemies.update()
        clouds.update()

        # Fill the screen
        screen.fill((135, 206, 250))

        # Draw all sprites
        for e in all_sprites:
            screen.blit(e.surf, e.rect)

        # Collision
        if pygame.sprite.spritecollideany(defender, enemies):
            defender.kill()
            running = False
        pygame.display.flip()
        clock.tick(30)
    pygame.mixer.quit()

if __name__ == '__main__':
    main()