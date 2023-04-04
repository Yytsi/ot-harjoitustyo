from tkinter import ttk, constants

class MainMenuView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text="Welcome to play the game!")
        
        start_game_button = ttk.Button(
            master=self._frame,
            text="Start game",
            command=lambda:{
                print("pressed button!")
            }
        )

        title_label.grid(row=0, column=0)
        start_game_button.grid(row=1, column=0)
