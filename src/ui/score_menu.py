from tkinter import ttk, constants
from database_handler import DatabaseHandler


class ScoreMenuView:
    """A class representing the score menu view in a game using Tkinter.
    """

    def __init__(self, root, show_main_menu, player1_name, player2_name, score=0):
        """Initializes a ScoreMenuView object.

        Args:
            root (_type_): root Tkinter window.
            show_main_menu (_type_): A function that shows the main menu view.
            score (int, optional): Score of the game. Defaults to 0.
        """
        self._root = root
        self._frame = None
        self._show_main_menu_view = show_main_menu
        self.score = score
        self.player1_name = player1_name
        self.player2_name = player2_name

        self._initialize()

    def pack(self):
        """Packs the elements of the score menu frame onto the root window.
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy this frame.
        """
        self._frame.destroy()

    def _initialize(self):
        """Initialize the score menu view.
        """
        db_handler = DatabaseHandler()
        if self.score > 0:
            db_handler.add_score(
                self.player1_name, self.player2_name, self.score)

        best_team = db_handler.get_highest_score_team()

        self._frame = ttk.Frame(master=self._root)
        score_label = ttk.Label(
            master=self._frame, text=f"Your score was {self.score} ! :)")

        score_label.grid(row=0, column=0, columnspan=2, padx=5, pady=2)

        if best_team[0] is not None:
            best_team_label = ttk.Label(
                master=self._frame, text=f"High score so far: {best_team[2]} by {best_team[0]} and {best_team[1]}"
            )
            best_team_label.grid(row=1, column=0, padx=5, pady=2, sticky="EW")

        ok_button = ttk.Button(
            master=self._frame,
            text="Main menu",
            command=self._show_main_menu_view
        )

        ok_button.grid(row=2, column=0, padx=5, pady=2, sticky="EW")

        self._root.grid_columnconfigure(1, weight=1)
