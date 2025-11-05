import pygame

from settings import Settings
from ship import Ship
import sys

class AlienInvasion:
    ## overall class that manage game assets and behavior
    
    def __init__(self):
        # initialize the game, and creat game resources.
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        self.screen = pygame.display.set_mode ((1200, 800))
        pygame.display.set_caption("Ailen Invasion")
        
        self.ship  = Ship(self)
       
        # Set the background color.
        self.bg_color = (250, 250, 250)
        
    def run_game(self):
   
     # star the main loop for the game, this vary inportent for the game 
       while True: 
           for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit() 
                
                self._check_events()
                self._update_screen()
                self.clock.tick(60) 
    #watch for kaybord and mouse events 
     # Redraw the screen during each pass through the loop.
    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # make the most rescently drawn creen visibel 
            pygame.display.flip()
            

if __name__ == '__main__':
    # make a game  instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()