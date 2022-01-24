import pygame
import random
from tkinter import *
from tkinter import messagebox


class Cube():
    rows = 20
    width = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):  # dirnx == direction for x
        # dirny == direction for y
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny

        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, face=False):
        distance = self.width // self.rows

        row = self.pos[0]
        col = self.pos[1]

        pygame.draw.rect(surface, self.color, (row * distance + 1, col * distance + 1, distance - 2, distance - 2))
        #                    it's actually:          x                 y             width          height
        if face:
            center = distance // 2
            radius = 3
            circleMiddle = (row * distance + center - radius, col * distance + 8)
            circleMiddle2 = (row * distance + distance - radius * 2, col * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class Snake():
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0  # this is needed to know in which direction we are going
        self.dirny = 1

    def move(self):

            keys = pygame.key.get_pressed()  # this gives all keys (if they clicked it's 1, else -> 0)
            # it is a dictionary ^
           # for key in keys:
            if keys[pygame.K_LEFT]:  # we want to know the value of dictionary object, who's key is K_LEFT
                # if it's 1 it's True and we go inside our if statement
                self.dirnx = -1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]  # we need to remember where the head turns,
                # so the whole body would turn in that position too

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                self.dirny = 0
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirnx = 0
                self.dirny = -1
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirnx = 0
                self.dirny = 1
                # this .pos[:] statement copies list, so we won't change initial list
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            for index, cube in enumerate(self.body):
                # getting position of the cube on the screen (it's cube object from Cube class)
                p = cube.pos[:]
                # if this position is in dictionary of snake turns
                if p in self.turns:
                    # get the value
                    turn = self.turns[p]
                    # using this function from Cube class
                    cube.move(turn[0], turn[1])
                    # if we're on the last cube that turns we should delete this turn from the dictionary
                    # if we won't snake will always turn in his position
                    if index == len(self.body) - 1:
                        self.turns.pop(p)
                else:
                    # if we're not at the turn position, so we need to keep moving
                    # and if we're in the border of the screen, snake should appear on the opposite side
                    if cube.dirnx == -1 and cube.pos[0] <= 0:
                        cube.pos = (cube.rows - 1, cube.pos[1])

                    elif cube.dirnx == 1 and cube.pos[0] >= cube.rows - 1:
                        cube.pos = (0, cube.pos[1])

                    elif cube.dirny == -1 and cube.pos[1] <= 0:
                        cube.pos = (cube.pos[0], cube.rows - 1)

                    elif cube.dirny == 1 and cube.pos[1] >= cube.rows - 1:
                        cube.pos = (cube.pos[0], 0)
                    # if we're not on the border, keep moving
                    else:
                        cube.move(cube.dirnx, cube.dirny)

    def reset(self, pos):
        self.head = Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy


    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)



def drawGrid(width, rows, surface):
    sizeBeetween = width // rows

    x = 0
    y = 0

    for line in range(rows):
        x += sizeBeetween
        y += sizeBeetween

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def randomSnack(rows, snake):
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:  # filter(function, iterable)
            #              lambda arguments: expression
            '''
            filter(function, iterable) method takes two parameters:
            function - function that tests if elements of an iterable return true or false.
            If None, the function defaults to Identity function - which returns false if any elements are false.
    
            iterable - iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators
            '''
            continue
        else:
            break

    return (x,y)

def redrawWindow(surface):
    global screen_width, rows, snake, snack
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    drawGrid(screen_width, rows, surface)
    pygame.display.update()


def message_box(subject, content):
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    pygame.init()

    global screen_width, rows, snake, snack
    screen_width = 500
    screen_height = 500
    rows = 20
    win = pygame.display.set_mode((screen_width, screen_height))
    snake = Snake((255, 0, 0), (10, 10))

    snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

    clock = pygame.time.Clock()

    run = True
    while run:
        pygame.time.delay(50)  # delays time by 50 ms
        clock.tick(10)  # 10 cubes per sec

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        snake.move()

        if snake.body[0].pos == snack.pos:
            snake.addCube()
            snack = Cube(randomSnack(rows, snake), color=(0, 255, 0))

        for x in range(len(snake.body)):
            if snake.body[x].pos in list(map(lambda z: z.pos, snake.body[x + 1:])):
                '''
                map(function, iterable)
                function - map() passes each item of the iterable to this function.
                iterable - iterable which is to be mapped
                '''
                score = len(snake.body)
                message_box('You lost', 'Your score is ' + str(score))
                snake.reset((10, 10))
                break

        redrawWindow(win)

    pygame.quit()

main()
