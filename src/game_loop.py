import pygame


class GameLoop:
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
                if event.key == pygame.K_a:
                    self._play_zone.player1.player_moving[0] = True
                if event.key == pygame.K_w:
                    self._play_zone.player1.player_moving[1] = True
                if event.key == pygame.K_d:
                    self._play_zone.player1.player_moving[2] = True
                if event.key == pygame.K_s:
                    self._play_zone.player1.player_moving[3] = True
                if event.key == pygame.K_LEFT:
                    self._play_zone.player2.player_moving[0] = True
                if event.key == pygame.K_UP:
                    self._play_zone.player2.player_moving[1] = True
                if event.key == pygame.K_RIGHT:
                    self._play_zone.player2.player_moving[2] = True
                if event.key == pygame.K_DOWN:
                    self._play_zone.player2.player_moving[3] = True
                if event.key == pygame.K_u:
                    self._play_zone.game_over = True
                    pygame.quit()
                    return False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self._play_zone.player1.player_moving[0] = False
                if event.key == pygame.K_w:
                    self._play_zone.player1.player_moving[1] = False
                if event.key == pygame.K_d:
                    self._play_zone.player1.player_moving[2] = False
                if event.key == pygame.K_s:
                    self._play_zone.player1.player_moving[3] = False
                if event.key == pygame.K_LEFT:
                    self._play_zone.player2.player_moving[0] = False
                if event.key == pygame.K_UP:
                    self._play_zone.player2.player_moving[1] = False
                if event.key == pygame.K_RIGHT:
                    self._play_zone.player2.player_moving[2] = False
                if event.key == pygame.K_DOWN:
                    self._play_zone.player2.player_moving[3] = False

        return True
