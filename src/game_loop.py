import pygame

class GameLoop:
    def __init__(self, play_zone, renderer, event_queue, clock):
        self._play_zone = play_zone
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
    
    def start(self):
        while True:
            if not self._handle_events():
                break
            
            self._renderer.render()

            if self._play_zone.game_over():
                break
                
            self._clock.tick(60)
    
    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self._play_zone.playermoving[0] = True
                if event.key == pygame.K_w:
                    self._play_zone.playermoving[1] = True
                if event.key == pygame.K_d:
                    self._play_zone.playermoving[2] = True
                if event.key == pygame.K_s:
                    self._play_zone.playermoving[3] = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self._play_zone.playermoving[0] = False
                if event.key == pygame.K_w:
                    self._play_zone.playermoving[1] = False
                if event.key == pygame.K_d:
                    self._play_zone.playermoving[2] = False
                if event.key == pygame.K_s:
                    self._play_zone.playermoving[3] = False