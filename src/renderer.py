import pygame


class Renderer:
    def __init__(self, display, play_zone):
        self._display = display
        self._play_zone = play_zone

    def render(self):
        self._display.fill("white")
        score_text, pos = self._play_zone.get_score_text()
        self._display.blit(score_text, pos)
        self._play_zone.all_sprites.draw(self._display)
        pygame.display.update()
