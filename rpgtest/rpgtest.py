from arcade import Window

from rpgtest.views.mainview import MainView

class RPGWindow(Window):
    def __init__(self):
        super().__init__(1280, 720, "RPG Test", update_rate = 1 / 60)
        self.local_time = 0.0

        self.debug = False

    def on_show(self):
        self.show_view(MainView())

    def on_update(self, delta_time: float):
        self.local_time += delta_time


def main():
    win = RPGWindow()
    win.run()


if __name__ == "__main__":
    main()
