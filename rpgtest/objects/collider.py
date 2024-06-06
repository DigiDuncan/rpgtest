from arcade import Rect, LRBT, Vec2, draw_rect_outline
import arcade.color

from rpgtest.lib.types import Number

class Collider(Rect):
    def __new__(cls, left: Number, right: Number, bottom: Number, top: Number):
        r = LRBT(left, right, bottom, top)
        return super().__new__(cls, **r.kwargs)

    def collide(self, original_hitbox: Rect, new_point: Vec2) -> Vec2:
        moved_hitbox = original_hitbox.at_position(new_point)
        if self.intersection(moved_hitbox):
            # Try just moving the X
            moved_x_hitbox = original_hitbox.align_x(new_point.x)
            if self.intersection(moved_x_hitbox):
                # Try just moving the Y?
                moved_y_hitbox = original_hitbox.align_y(new_point.y)
                if self.intersection(moved_y_hitbox):
                    # Give up
                    return original_hitbox.center
                return moved_y_hitbox.center
            return moved_x_hitbox.center
        return new_point

    def draw(self):
        draw_rect_outline(self, arcade.color.RED)
