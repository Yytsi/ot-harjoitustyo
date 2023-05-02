import pygame


class GameLoop:
    """A class implementing the main loop of the game where all events are processed
        and from which the game is started.
    """
    MOVEMENT_KEYS_PLAYER1 = [pygame.K_a, pygame.K_w, pygame.K_d, pygame.K_s]
    MOVEMENT_KEYS_PLAYER2 = [pygame.K_LEFT,
                             pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN]

    def __init__(self, play_zone, renderer, event_queue, clock):
        """Initialize the main game loop with required components.

        Args:
            play_zone (PlayZone): An object holding entities of the game and events related to them.
            renderer (Renderer): An object that implements content rendering of the game.
            event_queue (EventQueue): An object that fetches events created by pygame.
            clock (Clock): An object that implements the pygame clock object.
        """
        self._play_zone = play_zone
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        """Starts the game loop and runs until the game is over.

        Returns:
            int: Score of the game.
        """
        while not self._play_zone.game_over:
            if not self._handle_events():
                break

            self._play_zone.update()
            self._renderer.render()

            if self._play_zone.game_over:
                break

            self._clock.tick(60)
        self.end_game()
        return self._play_zone.current_score

    def end_game(self):
        """End the game, breaking the loop and quitting pygame."""
        self._play_zone.game_over = True
        pygame.quit()

    def _handle_events(self):
        """Handle keyboard events (movement or quit game).

        Returns:
            False, if exit game key was pressed, True otherwise
        """
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self.end_game()
                return False

            # Set flags for player moving in certain direction when key is down
            # and release when that key is no longer pressed down.
            if event.type == pygame.KEYDOWN:
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER1:
                    self._play_zone.player1.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER1.index(
                        event.key)] = True
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER2:
                    self._play_zone.player2.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER2.index(
                        event.key)] = True
                if event.key == pygame.K_u:
                    self.end_game()
                    return False

            # Release movement to direction flags.
            if event.type == pygame.KEYUP:
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER1:
                    self._play_zone.player1.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER1.index(
                        event.key)] = False
                if event.key in GameLoop.MOVEMENT_KEYS_PLAYER2:
                    self._play_zone.player2.player_moving[GameLoop.MOVEMENT_KEYS_PLAYER2.index(
                        event.key)] = False

        return True
