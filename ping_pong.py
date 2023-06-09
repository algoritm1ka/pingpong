from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed

back = (255, 228, 181)
width = 600
height = 500
window = display.set_mode((width, height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
fps = 60

platform1 = Player('platform.png', 30, 200, 4, 50, 150)
platform2 = Player('platform.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)

lose1 = font.render('PLAYER 1 LOSE!', True, (0, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (0, 0, 0))

dx = 3
dy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(background, (0,0))
        platform1.update_left()
        platform2.update_right()
        ball.rect.x += dx
        ball.rect.y += dy
        if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
            dx *= -1
        if ball.rect.y > height - 50 or ball.rect.y < 0:
            dy *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (200, 200))    

        platform1.reset()
        platform2.reset()
        ball.reset()

    display.update()
    clock.tick(fps)