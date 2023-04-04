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

        """ 
        sc = 0
        pygame.init()
        naytto = pygame.display.set_mode((640, 480))

        robo = pygame.image.load("assets/robo.png")
        robo2 = pygame.image.load("assets/robo.png")
        x = 0
        y = 480-robo.get_height()
        x2 = 100
        y2 = y

        oikealle = False
        vasemmalle = False

        lm = False
        rm = False
        um = False
        dm = False

        kello = pygame.time.Clock()
        
        running = True

        while running:
            sc += 1
            for tapahtuma in pygame.event.get():
                if tapahtuma.type == pygame.KEYDOWN:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = True
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = True
                    if tapahtuma.key == pygame.K_a:
                        lm = True
                    if tapahtuma.key == pygame.K_d:
                        rm = True
                    if tapahtuma.key == pygame.K_w:
                        um = True
                    if tapahtuma.key == pygame.K_s:
                        dm = True
                    

                if tapahtuma.type == pygame.KEYUP:
                    if tapahtuma.key == pygame.K_LEFT:
                        vasemmalle = False
                    if tapahtuma.key == pygame.K_RIGHT:
                        oikealle = False
                    if tapahtuma.key == pygame.K_a:
                        lm = False
                    if tapahtuma.key == pygame.K_d:
                        rm = False
                    if tapahtuma.key == pygame.K_w:
                        um = False
                    if tapahtuma.key == pygame.K_s:
                        dm = False

                if tapahtuma.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    break
            
            if not running:
                break

            if oikealle:
                x += 2
            if vasemmalle:
                x -= 2
            if lm:
                x2 -= 2
            if rm:
                x2 += 2
            if um:
                y2 -= 2
            if dm:
                y2 += 2

            naytto.fill((0, 0, 0))
            naytto.blit(robo, (x, y))
            naytto.blit(robo2, (x2, y2))
            pygame.display.flip()

            kello.tick(60)
        return sc"""