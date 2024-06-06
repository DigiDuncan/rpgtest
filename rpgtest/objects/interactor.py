from pyglet.math import Vec2
import arcade.color

from rpgtest.lib.draw import draw_cross
from rpgtest.objects.player import Player

class Interactor:
    def __init__(self, position: Vec2, interaction_range: float):
        self.position = position
        self.interaction_range = interaction_range

        self.active = False
        self.activated_time = float("inf")

        self.window = arcade.get_window()

    def update(self, delta_time: float, player: Player):
        self.active = player.position.distance(self.position) <= self.interaction_range

    def draw(self):
        draw_cross(self.position, 3, arcade.color.GREEN if self.active else arcade.color.GRAY)

    def activate(self):
        raise NotImplementedError


class Woah(Interactor):
    def activate(self):
        if self.active:
            self.activated_time = self.window.local_time

    def draw(self):
        if self.activated_time < self.window.local_time < self.activated_time + 1:
            arcade.draw_text("!", self.position.x, self.position.y, color = arcade.color.MAGENTA, font_size = 24,
                             anchor_x = "center", anchor_y = "bottom")

        if self.window.debug:
            arcade.draw_circle_outline(self.position.x, self.position.y, self.interaction_range, arcade.color.YELLOW)

        super().draw()
