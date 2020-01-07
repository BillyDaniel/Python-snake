import pygame

WIDTH, HEIGHT = 500, 500
ROWS = 20
SPACE=WIDTH//ROWS

class Snake:
    def __init__(self,surface):
        self.surface = surface
        self.pos = []
        self.dirx = -SPACE
        self.diry = 0
        self.color = (255,0,0)
        self.body = []
        self.length = 4
        for x in range(self.length):
            self.pos.append((10-x,10))
            self.body.append(pygame.draw.rect(self.surface, self.color, (self.pos[x][0]*SPACE, self.pos[x][1]*SPACE, SPACE+1,SPACE+1)))
        self.rect = self.body[0]

    def move(self):
        if self.boundary_check() == True:
            self.reset()
        else:

            self.body.insert(0,self.rect.move(self.dirx,self.diry))
            self.rect = self.body[0]
            self.body.pop()
            self.rect = self.body[0]

            #self.rect.move_ip(self.dirx,self.diry)
            #self.rect.move_ip(self.dirx, self.diry)
            for snake in self.body:
                pygame.draw.rect(self.surface, self.color,snake)

    def direction(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.diry != SPACE:
                    self.dirx = 0
                    self.diry = -SPACE

                if event.key == pygame.K_DOWN and self.diry != -SPACE:
                    self.dirx = 0
                    self.diry = SPACE

                if event.key == pygame.K_LEFT and self.dirx != SPACE:
                    self.dirx = -SPACE
                    self.diry = 0

                if event.key == pygame.K_RIGHT and self.dirx != -SPACE:
                    self.dirx = SPACE
                    self.diry = 0

    def boundary_check(self):
        if any([
            self.rect.x == 0 and self.dirx == -SPACE,
            self.rect.x == 475 and self.dirx == SPACE,
            self.rect.y == 0 and self.diry == -SPACE,
            self.rect.y == 475 and self.diry == SPACE
        ]):
            return True

    def reset(self):
        self.body.clear()
        for x in range(self.length):
            self.body.append(pygame.draw.rect(self.surface, self.color, (self.pos[x][0]*SPACE, self.pos[x][1]*SPACE, SPACE+1,SPACE+1)))
            self.rect = self.body[0]
        #self.rect = pygame.draw.rect(self.surface, self.color, (self.pos[0]*SPACE, self.pos[1]*SPACE, SPACE+1,SPACE+1))

        self.dirx = -SPACE
        self.diry = 0

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
