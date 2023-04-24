import pygame


class GameLoop:
    MOVEMENT_KEYS_PLAYER1 = [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]
    MOVEMENT_KEYS_PLAYER2 = [pygame.K_LEFT, pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]
    def __init__(self, play_zone, renderer, event_queue, clock):
        self._play_zone = play_zone
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        while not self._play_zone.game_over:
            if not self._handle_events():
                break

            self._play_zone.update()
            self._renderer.render()

            if self._play_zone.game_over:
                break

            self._clock.tick(60)
        self.end_game()

    def end_game(self):
        self._play_zone.game_over = True
        pygame.quit()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self._play_zone.game_over = True
                pygame.quit()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER1:
                    self._play_zone.player1.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER1.index(event.key)] = True
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER2:
                    self._play_zone.player2.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER2.index(event.key)] = True
                if event.key == pygame.K_u:
                    # End the game.
                    self._play_zone.game_over = True
                    pygame.quit()
                    return False

            if event.type == pygame.KEYUP:
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER1:
                    self._play_zone.player1.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER1.index(event.key)] = False
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER2:
                    self._play_zone.player2.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER2.index(event.key)] = False

        return True
