from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed  = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < win_width-80:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.y >5:
            self.rect.x -= self.speed
    def update_r(self):
        keys_pressed  = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.y >5:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= win_height:
            self.rect.y += self.speed
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)

back = (200, 255, 255)
win_height = 500
win_width = 600
window = display.set_mode((win_width,win_height))
display.set_caption("Пинг-понг")
window.fill(back)

score_left = 0
score_right = 0

font.init()
font1 = font.SysFont('None', 36)
font2 = font.SysFont('Arial', 36)
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))

speed_x = 3
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 30, 200, 25, 75, 4)
racket2 = Player('racket.png', 520, 200, 25, 75, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 25, 25, 7)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball):
            speed_x = -(racket1.rect.x - ball.rect.x)/10
            speed_y = -(racket1.rect.y - ball.rect.y)/10
        
        if sprite.collide_rect(racket2, ball):
            speed_x = -(racket2.rect.x - ball.rect.x)/10
            speed_y = -(racket2.rect.y - ball.rect.y)/10
        
        if ball.rect.y < 0 or ball.rect.y > win_height - 50:
            speed_y *= -1
        
        if ball.rect.x < 0 or ball.rect.x > win_width - 50:
            speed_x *= -1
      
        if ball.rect.x < 0:
            score_right += 1 
            ball.rect.x = 300
            ball.rect.y = 225  
            speed_x = 0
            speed_y = 0   

        if ball.rect.x > win_width - 50:
            score_left += 1
            ball.rect.x = 300
            ball.rect.y = 225
            speed_x = 0
            speed_y = 0
        
        if score_right > 7:
            finish = True
            window.blit(lose1, (200,200))
        
        if score_left > 7:
            finish = True
            window.blit(lose2, (200,200))

        text1 = font2.render("Счет", 1, (255, 255, 255))
        window.blit(text1, (250, 40))
        text2 = font2.render(str(score_left)+" : "+str(score_right), 1, (255, 255, 255))
        window.blit(text2, (250, 80))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
    


