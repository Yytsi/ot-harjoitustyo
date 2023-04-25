from tkinter import ttk, constants
from game import Game


class MainMenuView:
    def __init__(self, root, show_score_menu):
        self._root = root
        self._frame = None
        self._show_score_menu_view = show_score_menu

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def start_game(self):
        player1_name = self.player1_name_entry.get()
        player2_name = self.player1_name_entry.get()
        g = Game(player1_name=player1_name, player2_name=player2_name)
        score = g.play_game()
        self._show_score_menu_view(score)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(
            master=self._frame, text="Welcome to CatchIt game!")

        start_game_button = ttk.Button(
            master=self._frame,
            text="Start game",
            command=self.start_game
        )

        player1_name_label = ttk.Label(
            master=self._frame, text="Player 1 name:")
        player2_name_label = ttk.Label(
            master=self._frame, text="Player 2 name:")

        self.player1_name_entry = ttk.Entry(master=self._frame)
        self.player2_name_entry = ttk.Entry(master=self._frame)

        title_label.grid(row=0, column=0, columnspan=2)
        player1_name_label.grid(row=1, column=0, padx=5, pady=2)
        self.player1_name_entry.grid(
            row=1, column=1, padx=5, pady=2, sticky="EW")
        player2_name_label.grid(row=2, column=0, padx=5, pady=2)
        self.player2_name_entry.grid(
            row=2, column=1, padx=5, pady=2, sticky="EW")
        start_game_button.grid(row=3, column=0, padx=5,
                               pady=5, columnspan=2, sticky="EW")

        self._root.grid_columnconfigure(1, weight=1)
