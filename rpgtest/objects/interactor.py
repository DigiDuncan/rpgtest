from pyglet.math import Vec2
import arcade.color

from rpgtest.lib.draw import draw_cross
from rpgtest.objects.player import Player

class Interactor:
    def __init__(self, position: Vec2, interaction_range: float):
        self.position = position
        self.interaction_range = interaction_range

        self.active = False

    def update(self, delta_time: float, player: Player):
        self.active = player.position.distance(self.position) <= self.interaction_range

    def draw(self):
        draw_cross(self.position, 3, arcade.color.GREEN if self.active else arcade.color.GRAY)
