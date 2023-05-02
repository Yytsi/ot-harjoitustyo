from ui.main_menu import MainMenuView
from ui.score_menu import ScoreMenuView


class UI:
    """A class representing the user interface in a game using Tkinter.
    """

    def __init__(self, root):
        """Initializes an UI instance.

        Args:
            root (Tk): root Tkinter window.
        """
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_main_menu_view(self):
        self._hide_current_view()

        self._current_view = MainMenuView(
            self._root,
            self._show_score_menu_view
        )

        self._current_view.pack()

    def _show_score_menu_view(self, player1_name, player2_name, score):
        self._hide_current_view()

        self._current_view = ScoreMenuView(
            self._root,
            self._show_main_menu_view,
            player1_name,
            player2_name,
            score
        )

        self._current_view.pack()
