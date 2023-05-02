import pygame


class Renderer:
    """Renders objects of the game.
    """

    def __init__(self, display, play_zone):
        """Initialize with display and game objects.

        Args:
            display (_type_): pygame display object.
            play_zone (_type_): Holds game objects used for rendering.
        """
        self._display = display
        self._play_zone = play_zone

    def render(self):
        self._display.fill("white")
        score_text, pos = self._play_zone.get_score_text()
        self._display.blit(score_text, pos)
        self._play_zone.all_sprites.draw(self._display)
        pygame.display.update()
