#external modules
import sys
import pygame

#internal modules
#import title,core

class Game:
    def __init__(self):
        self.SCREENX = 800
        self.SCREENY = 600
        self.WINDOW =  pygame.display.set_mode((self.SCREENX,self.SCREENY),pygame.DOUBLEBUF,32)
        self.CLOCK = pygame.time.Clock()
        self.state='title'
        self.STATELIST={'title':self.runTitle,'game':self.runGame}#,'death':self.runDeath}
        self.run()

    def run(self):
        self.STATELIST[self.state]()

    def runTitle(self):
        self.title=title.Title(self)
        while self.state == 'title':
            self.update(self.title)
        self.run()

    def runGame(self):
        self.core=core.Core(self)
        while self.state == 'game':
            self.update(self.core)
        self.run()

    def update(self,module):
        module.update()
        pygame.display.update()
        self.CLOCK.tick(module.REFRESH)

    def quit(self):
        pygame.quit()
        sys.exit()

pygame.init()
game=Game()
