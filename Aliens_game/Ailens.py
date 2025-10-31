import pygame

from settings import Settings
import sys

class AlienInvasion:
    ## overall class that manage game assets and behavior
    
    def __init__(self):
        # initialize the game, and creat game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode ((1200, 800))
        pygame.display.set_caption("Ailen Invasion")
        
        # Set the background color.
        self.bg_color = (230, 230, 230)
   
    def run_game(self):
     # star the main loop for the game, this vary inportent for the game 
        while True: 
            #watch for kaybord and mouse events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
                self.screen.fill(self.settings.bg_color)
            # make the most rescently drawn creen visibel 
                pygame.display.flip()
                self.clock.tick(60)

if __name__ == '__main__':
    # make a game  instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
    
    
        
     
        
        