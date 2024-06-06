from arcade import Camera2D, Vec2, View
import arcade.key

from rpgtest.objects.collider import Collider
from rpgtest.objects.interactor import Interactor, Woah
from rpgtest.objects.player import Player

class MainView(View):
    def __init__(self):
        super().__init__()

        self.camera = Camera2D()
        self.player = Player(self.window.center)
        self.colliders: list[Collider] = [
            Collider(700, 900, 100, 620)
        ]
        self.interactors: list[Interactor] = [
            Woah(Vec2(self.window.center_x - 200, self.window.center_y), 25)
        ]

    def on_key_press(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.W:
                self.player.moving_up = True
            case arcade.key.S:
                self.player.moving_down = True
            case arcade.key.A:
                self.player.moving_left = True
            case arcade.key.D:
                self.player.moving_right = True

            case arcade.key.GRAVE:
                self.window.debug = not self.window.debug

            case arcade.key.ENTER:
                for i in self.interactors:
                    i.activate()

    def on_key_release(self, symbol: int, modifiers: int):
        match symbol:
            case arcade.key.W:
                self.player.moving_up = False
            case arcade.key.S:
                self.player.moving_down = False
            case arcade.key.A:
                self.player.moving_left = False
            case arcade.key.D:
                self.player.moving_right = False

    def on_update(self, delta_time: float):
        self.player.update(delta_time, self.colliders)

        for i in self.interactors:
            i.update(delta_time, self.player)

        self.camera.position = self.player.position

        return super().on_update(delta_time)

    def on_draw(self):
        self.clear()
        with self.camera.activate():
            self.player.draw()
            for c in self.colliders:
                c.draw()
            for i in self.interactors:
                i.draw()
