import pygame

pygame.init()

win = pygame.display.set_mode((800, 400))
surf = pygame.image.load('C:/Я картинки/Милыйдинозавр.ico')
pygame.display.set_icon(surf)

pygame.display.set_caption('First Game')

walkLeft = [pygame.image.load('Hulk\L1.PNG'), pygame.image.load('Hulk\L2.PNG'),
            pygame.image.load('Hulk\L3.PNG'),
            pygame.image.load('Hulk\L4.PNG')]
walkRight = [pygame.image.load('Hulk\R1.PNG'), pygame.image.load('Hulk\R2.PNG'),
             pygame.image.load('Hulk\R3.PNG'),
             pygame.image.load('Hulk\R4.PNG')]
bg = pygame.image.load('bg.PNG')
stand = pygame.image.load('Hulk\Front.PNG')

screen_width = 800
screen_height = 400

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.wav')
hitSound = pygame.mixer.Sound('hit.wav')

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

score = 0

class Player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 8
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 5, self.y, 30, 56)  # this is rectangle
        #                x,            y,  width, height

    def draw(self, win):
        if self.walkCount + 1 >= 16:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 5, self.y, 30, 56)
        # pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 8
        self.x = 30
        self.y = 200
        self.walkCount = 0
        font_1 = pygame.font.SysFont('comicsans', 100)
        text = font_1.render('-5', 1, (0, 0, 255))
        win.blit(text, (400 - text.get_width()/2, 220))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()

class Projectile(object):

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy():
    walkRight = [pygame.image.load('Leviathan\R1.PNG'), pygame.image.load('Leviathan\R2.PNG'),
             pygame.image.load('Leviathan\R3.PNG'), pygame.image.load('Leviathan\R4.PNG')]
    walkLeft = [pygame.image.load('Leviathan\L1.PNG'), pygame.image.load('Leviathan\L2.PNG'),
            pygame.image.load('Leviathan\L3.PNG'), pygame.image.load('Leviathan\L4.PNG')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x, self.y + 35, 100, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 16:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1

            self.hitbox = (self.x, self.y + 35, 100, 60)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 100, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 100 - (10 * (10 - self.health)), 10))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    text = font.render('Score: ' + str(score), 1, (255, 0, 0))
    win.blit(text, (600, 10))
    hulk.draw(win)
    snake.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
font = pygame.font.SysFont('comicsans', 30, True, True)
hulk = Player(x=30, y=200, width=40, height=56)
bullets = []
shootLoop = 0
snake = Enemy(x=120, y=180, width=96, height=96, end=400)
run = True
while run:
    # pygame.time.delay(50)
    clock.tick(32)
    if snake.visible:  # if it equals to True
        if hulk.hitbox[1] < snake.hitbox[1] + snake.hitbox[3] and hulk.hitbox[1] + hulk.hitbox[3] > snake.hitbox[1]:
            if hulk.hitbox[0] < snake.hitbox[0] + snake.hitbox[2] and hulk.hitbox[0] + hulk.hitbox[2] > snake.hitbox[0]:
                hulk.hit()
                #  collideSound.play()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 5:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if snake.visible:
            if bullet.y + bullet.radius > snake.hitbox[1] and bullet.y - bullet.radius < snake.hitbox[1] + snake.hitbox[3]:
                if bullet.x + bullet.radius > snake.hitbox[0] and bullet.x - bullet.radius < snake.hitbox[0] + snake.hitbox[2]:
                    snake.hit()
                    hitSound.play()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if 0 < bullet.x < screen_width:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if hulk.left:
            Facing = -1
        else:
            Facing = 1

        if len(bullets) < 5:
            bullets.append(Projectile(round(hulk.x + hulk.width // 2), round(hulk.y + hulk.height // 2), 6, (0, 0, 255),
                                      Facing))
        bulletSound.play()
        shootLoop = 1

    if keys[pygame.K_LEFT] and hulk.x > hulk.vel:
        hulk.x -= hulk.vel
        hulk.left = True
        hulk.right = False
        hulk.down = False
        hulk.up = False
        hulk.standing = False
    elif keys[pygame.K_RIGHT] and hulk.x < screen_width - hulk.width - hulk.vel:
        hulk.x += hulk.vel
        hulk.right = True
        hulk.left = False
        hulk.down = False
        hulk.up = False
        hulk.standing = False
    else:
        hulk.standing = True
        hulk.walkCount = 0

    if not hulk.isJump:
        # if keys[pygame.K_UP] and hulk.y > hulk.vel:
        #     hulk.y -= hulk.vel
        #     hulk.up = True
        #     hulk.right = False
        #     hulk.left = False
        #     hulk.down = False
        # if keys[pygame.K_DOWN] and hulk.y < screen_height - hulk.height - hulk.vel:
        #     hulk.y += hulk.vel
        #     hulk.down = True
        #     hulk.right = False
        #     hulk.left = False
        #     hulk.up = False
        if keys[pygame.K_UP]:
            hulk.isJump = True
            hulk.standing = True
            hulk.walkCount = 0
    else:
        if hulk.jumpCount >= -8:
            neg = 0.5
            if hulk.jumpCount < 0:
                neg = -0.5
            hulk.y -= hulk.jumpCount ** 2 * neg
            hulk.jumpCount -= 1
        else:
            hulk.isJump = False
            hulk.jumpCount = 8

    redrawGameWindow()
    # win.fill((0, 0, 0))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # pygame.display.update()

pygame.quit()
