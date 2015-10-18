__author__ = 'Volodymyr'

class Character:

    def __init__(self, width, height, pictures, run = 1):
        self.sprites = []
        for pic in pictures:
            self.sprites.append( pic )

        self.rect = self.sprites[0].get_rect()
        self.direction = DIR_UP
        self.width, self.height = width, height
        self.speed = [0,0]
        self.run = run
        self.action = 0

    def get_sprite(self):
        index = self.direction
        if self.action == 1:
            index += 4
        return self.sprites[index]

    def move(self, direction):
        # print("char", direction)
        self.direction = direction
        if direction == DIR_LEFT:
            self.speed = [-self.run, 0]
        if direction == DIR_RIGHT:
            self.speed = [self.run, 0]
        if direction == DIR_UP:
            self.speed = [0, -self.run]
        if direction == DIR_DOWN:
            self.speed = [0, self.run]

        if self.rect.left < 0:
            if self.speed[0] < 0:
                self.speed[0] = 0
        if self.rect.right > self.width:
            if self.speed[0] > 0:
                self.speed[0] = 0
        if self.rect.top < 0:
            if self.speed[1] < 0:
                self.speed[1] = 0
        if self.rect.bottom > self.height:
            if self.speed[1] > 0:
                self.speed[1] = 0

    def stab(self, action):
        self.action = action

    def update(self):
        self.rect = self.rect.move(self.speed)

    def stop(self):
        self.speed = [0, 0]