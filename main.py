from pygame import*
init()
# розмір вікна
W = 700
H = 700
# створили вікно
window = display.set_mode((W, H))

display.set_caption("labyrinth")
display.set_icon(image.load('treasure.png'))

back = transform.scale(image.load('background1.jpg'), (W, H))
clock = time.Clock()

mixer.init()
mixer.music.load('fonmusic.mp3')
mixer.music.set_volume(0.4)
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self, player_imp, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_imp), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()#отримуємо список отриманих клавіш
        if keys_pressed[K_w] and self.rect.y > 0:# перевірка клавіши у верх
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 65:# перевіряємо клавішу у низ
            self.rect.y += self.speed
            
        if keys_pressed[K_a] and self.rect.x > 0:# перевіряємо клавіши в вліво
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < W - 65:# перевіряємо клавішу право
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "right"# напрямок руху ворога
    
    def update(self, start, end):
        if self.rect.x >= end:# якщо ми доходимо до кінця 
            self.direction = 'left'# міняємо напрямок в ліво
            self.image = transform.scale(image.load('dogenemy.png'), (65, 65))# змінюємо на картинку яка повернута вліво
        if self.rect.x <= start:# якщо ми доходимо до початку
            self.direction = 'right'# міняємо напрямок в право
            self.image = transform.scale(image.load('dogenemy1.png'), (65, 65))# змінюємо на картинку яка повернута в право
        
        if self.direction == 'left':# ідемо вліво
            self.rect.x -= self.speed
        if self.direction == 'right':# ідемо в право
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_w, wall_h, wall_x, wall_y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.widht = wall_w
        self.height = wall_h
        self.image = Surface((self.widht, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

gold = GameSprite('fishcoi1.png', 590, 590, 0) 
hero = Player('cathero1.png', 40, 40, 3)
enemy = Enemy('dogenemy.png', 350, 400, 2)
game = True
# рамка
wall1 = Wall(108, 126, 130, 680, 10, 10, 20)
wall2 = Wall(108, 126, 130, 10, 660, 10, 20)
wall3 = Wall(108, 126, 130, 670, 10, 20, 670)
wall4 = Wall(108, 126, 130, 10, 660, 680, 20)
# лабіринт вертикальні
wall6 = Wall(108, 126, 130, 10, 180, 160, 30)
wall9 = Wall(108, 126, 130, 10, 100, 380, 30)
wall10 = Wall(108, 126, 130, 10, 100, 380, 210)
wall12 = Wall(108, 126, 130, 10, 100, 480, 120)
wall14 = Wall(108, 126, 130, 10, 180, 580, 120)
wall21 = Wall(108, 126, 130, 10, 180, 520, 400)
wall22 = Wall(108, 126, 130, 10, 100, 290, 400)
wall25 = Wall(108, 126, 130, 10, 100, 100, 490)
wall27 = Wall(108, 126, 130, 10, 100, 240, 580)
# горизонтальні
wall13 = Wall(108, 126, 130, 390, 10, 100, 300)
wall5 = Wall(108, 126, 130, 60, 10, 20, 120)
wall7 = Wall(108, 126, 130, 120, 10, 160, 120)
wall8 = Wall(108, 126, 130, 120, 10, 260, 210)
wall11 = Wall(108, 126, 130, 100, 10, 380, 120)
wall15 = Wall(108, 126, 130, 100, 10, 580, 210)
wall16 = Wall(108, 126, 130, 100, 10, 20, 400)
wall17 = Wall(108, 126, 130, 140, 10, 210, 400)
wall18 = Wall(108, 126, 130, 110, 10, 470, 390)
wall19 = Wall(108, 126, 130, 90, 10, 590, 490)
wall20 = Wall(108, 126, 130, 170, 10, 520, 580)
wall23 = Wall(108, 126, 130, 140, 10, 290, 490)
wall24 = Wall(108, 126, 130, 110, 10, 100, 490)
wall26 = Wall(108, 126, 130, 330, 10, 100, 580)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back, (0, 0))
    gold.reset()
    hero.reset()
    hero.update()
    enemy.reset()
    enemy.update(350, 450)
    wall1.reset()
    wall2.reset()
    wall3.reset()
    wall4.reset()
    wall5.reset()
    wall6.reset()
    wall7.reset()
    wall8.reset()
    wall9.reset()
    wall10.reset()
    wall11.reset()
    wall12.reset()
    wall13.reset()
    wall14.reset()
    wall15.reset()
    wall16.reset()
    wall17.reset()
    wall18.reset()
    wall19.reset()
    wall20.reset()
    wall21.reset()
    wall22.reset()
    wall23.reset()
    wall24.reset()
    wall25.reset()
    wall26.reset()
    wall27.reset()
    if sprite.collide_rect(hero, wall1) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7) or sprite.collide_rect(hero, wall8) or sprite.collide_rect(hero, wall9) or sprite.collide_rect(hero, wall10) or sprite.collide_rect(hero, wall11) or sprite.collide_rect(hero, wall12) or sprite.collide_rect(hero, wall13) or sprite.collide_rect(hero, wall14) or sprite.collide_rect(hero, wall15) or sprite.collide_rect(hero, wall16) or sprite.collide_rect(hero, wall17) or sprite.collide_rect(hero, wall18) or sprite.collide_rect(hero, wall19) or sprite.collide_rect(hero, wall20) or sprite.collide_rect(hero, wall21) or sprite.collide_rect(hero, wall22) or sprite.collide_rect(hero, wall23) or sprite.collide_rect(hero, wall24) or sprite.collide_rect(hero, wall25) or sprite.collide_rect(hero, wall26) or sprite.collide_rect(hero, wall27) or sprite.collide_rect(hero, enemy):
        hero.rect.x = 20
        hero.rect.y = 40
    if sprite.collide_rect(hero, gold):
        game = False
    display.update()
    clock.tick(60)