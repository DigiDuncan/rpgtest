from pyglet.math import Vec2

from arcade import Rect, draw_rect_filled, draw_rect_outline, XYWH
import arcade.color

from rpgtest.objects.collider import Collider

class Player:
    def __init__(self, position: tuple[float, float]):
        self.position = Vec2(*position)

        self.move_speed = 100.0  # px/s
        self.player_size = 10

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.attempted_pos = Vec2(*position)

        self.window = arcade.get_window()

    @property
    def hitbox(self) -> Rect:
        return XYWH(self.position.x, self.position.y, self.player_size, self.player_size)

    def update(self, delta_time: float, colliders: list[Collider]):
        new_x, new_y = self.position

        # Modify the new position we want to be at based on what directions we're moving.
        if self.moving_up:
            new_y += self.move_speed * delta_time
        if self.moving_down:
            new_y -= self.move_speed * delta_time
        if self.moving_left:
            new_x -= self.move_speed * delta_time
        if self.moving_right:
            new_x += self.move_speed * delta_time

        self.attempted_pos = Vec2(new_x, new_y)

        # Make sure we're not about to be inside a collider.
        for collider in colliders:
            new_x, new_y = collider.collide(self.hitbox, Vec2(new_x, new_y))

        # Confirm our changes.
        self.position = Vec2(new_x, new_y)

    def draw(self):
        draw_rect_filled(self.hitbox, arcade.color.BLUE)
        if self.window.debug:
            draw_rect_outline(self.hitbox.at_position(self.attempted_pos), arcade.color.YELLOW)
