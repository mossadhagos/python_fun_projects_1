import pygame
import sys

class AlienInvasion:
    ## overall class that manage game assets and behavior
    
    def __init__(self):
        # initialize the game, and creat game resources.
        pygame.init()
        
        self.screen = pygame.display.set_mode ((1200, 800))
        pygame.display.set_caption("Ailen Invasion")
        
    def run_game(self):
     # star the main loop for the game, this vary inportent for the game 
        while True: 
            #watch for kaybord and mouse events 
            for event in pygame.event.set():
                if event.typ == pygame.QUIT:
                    sys.exit()
            
            # make the most rescently drawn creen visibel 
            pygame.display.flip()

if __name__ == '__main__':
    # make a game  instance, and run the game.
    ai = AlienInvasion
    ai.run_game()