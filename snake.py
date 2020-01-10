import pygame
import random

WIDTH, HEIGHT = 500, 500
ROWS = 20
SPACE=WIDTH//ROWS

class Snake:
    def __init__(self,surface):
        self.surface = surface
        self.dirx = -SPACE
        self.diry = 0
        self.color = (255,0,0)
        self.body = []
        self.length = 2
        for x in range(self.length-1):
            self.body.append(pygame.draw.rect(self.surface, self.color, ((10+x+1)*SPACE, 10*SPACE, SPACE+1,SPACE+1)))
        self.rect = pygame.draw.rect(self.surface, self.color, (10*SPACE, 10*SPACE, SPACE+1,SPACE+1))
        self.fruit = self.make_apple()

    def move(self):
        if self.boundary_check() or self.hit_check() == True:
            self.reset()
        else:
            self.body.insert(0,self.rect)
            self.rect = self.rect.move(self.dirx,self.diry)
            if self.rect == self.fruit:
                self.fruit = self.make_apple()
            else:
                self.body.pop()
            for snake in self.body:
                pygame.draw.rect(self.surface, self.color,snake)
            pygame.draw.rect(self.surface, self.color,self.rect)
            pygame.draw.rect(self.surface,(0,255,0),self.fruit)

    def direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.diry != SPACE:
                    self.dirx = 0
                    self.diry = -SPACE
                    break

                elif event.key == pygame.K_DOWN and self.diry != -SPACE:
                    self.dirx = 0
                    self.diry = SPACE
                    break

                elif event.key == pygame.K_LEFT and self.dirx != SPACE:
                    self.dirx = -SPACE
                    self.diry = 0
                    break

                elif event.key == pygame.K_RIGHT and self.dirx != -SPACE:
                    self.dirx = SPACE
                    self.diry = 0
                    break

    def boundary_check(self):
        if any([
            self.rect.x == 0 and self.dirx == -SPACE,
            self.rect.x == 475 and self.dirx == SPACE,
            self.rect.y == 0 and self.diry == -SPACE,
            self.rect.y == 475 and self.diry == SPACE
        ]):
            return True

    def hit_check(self):
        if self.rect in self.body:
            return True


    def reset(self):
        self.body.clear()
        for x in range(self.length-1):
            self.body.append(pygame.draw.rect(self.surface, self.color, ((10+x+1)*SPACE, 10*SPACE, SPACE+1,SPACE+1)))
        #self.rect = self.body[0]
        self.rect = pygame.draw.rect(self.surface, self.color, (10*SPACE, 10*SPACE, SPACE+1,SPACE+1))
        self.dirx = -SPACE
        self.diry = 0

    def make_apple(self):
        fruit_x = rand_x = random.randrange(0, WIDTH, SPACE)
        fruit_y = rand_y = random.randrange(0, HEIGHT, SPACE)
        print(fruit_x,fruit_y)
        return pygame.draw.rect(self.surface, (0,255,0), (fruit_x,fruit_y,SPACE+1,SPACE+1))



class Map:
    def __init__(self,surface):
        self.surface = surface

    def draw_grid(self):
        startPoint=0
        for l in range(ROWS):
            startPoint = startPoint+SPACE
            pygame.draw.line(self.surface, (225, 225, 225), (startPoint, 0), (startPoint, WIDTH))
            pygame.draw.line(self.surface, (225, 225, 225), (0, startPoint), (WIDTH, startPoint))

    def redraw_window(self,snake):
        self.surface.fill((0,0,0))
        self.draw_grid()
        snake.move()
        snake.direction()
        pygame.display.update()
        pygame.time.delay(200)





def main():
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    s = Snake(screen)
    m = Map(screen)
    while 1:
        m.redraw_window(s)
    pass

main()
