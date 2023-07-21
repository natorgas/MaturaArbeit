from coordinate_calculator import x1, y1, x2, y2, x3, y3, x4, y4
from equationsolver_double_pendulum import fps, duration, alpha0_1, beta0_1, l1, l2, t
from manim import *


class DoublePendulum(MovingCameraScene):
    def construct(self):

        x1tracker = ValueTracker(x1[0])
        y1tracker = ValueTracker(y1[0])
        x2tracker = ValueTracker(x2[0])
        y2tracker = ValueTracker(y2[0])
        x3tracker = ValueTracker(x3[0])
        y3tracker = ValueTracker(y3[0])
        x4tracker = ValueTracker(x4[0])
        y4tracker = ValueTracker(y4[0])
        t_tracker = ValueTracker(0)
        t_count = always_redraw(lambda: DecimalNumber(t_tracker.get_value()).move_to([(l1+l2)*(16/9)-1, l1+l2, 0]).scale_to_fit_height(((l1+l2)*2 + 2)/20, about_edge=UR))
        rod1 = always_redraw(lambda: Line([0, 0, 0], [x1tracker.get_value(), y1tracker.get_value(), 0], stroke_width=0.3*((l1+l2)*2 + 2)*(16/9)))
        rod2 = always_redraw(lambda: Line([x1tracker.get_value(), y1tracker.get_value(), 0], [x2tracker.get_value(), y2tracker.get_value(), 0], stroke_width=0.3*((l1+l2)*2 + 2)*(16/9)))
        rod3 = always_redraw(lambda: Line([0, 0, 0], [x3tracker.get_value(), y3tracker.get_value(), 0], stroke_width=0.3*((l1+l2)*2 + 2)*(16/9)))
        rod4 = always_redraw(lambda: Line([x3tracker.get_value(), y3tracker.get_value(), 0], [x4tracker.get_value(), y4tracker.get_value(), 0], stroke_width=0.3*((l1+l2)*2 + 2)*(16/9)))
        m1 = always_redraw(lambda: Circle(radius=0.013*((l1+l2)*2 + 2)*(16/9), color=RED, fill_color=RED, fill_opacity=1).next_to(rod1.get_end(), buff=0, direction=ORIGIN))
        m2 = always_redraw(lambda: Circle(radius=0.013*((l1+l2)*2 + 2)*(16/9), color=DARK_BLUE, fill_color=DARK_BLUE, stroke_color=DARK_BLUE, fill_opacity=1).next_to(rod2.get_end(), buff=0, direction=ORIGIN))
        m3 = always_redraw(lambda: Circle(radius=0.013*((l1+l2)*2 + 2)*(16/9), color=RED, fill_color=RED, fill_opacity=1).next_to(rod3.get_end(), buff=0, direction=ORIGIN))
        m4 = always_redraw(lambda: Circle(radius=0.013*((l1+l2)*2 + 2)*(16/9), color=DARK_BLUE, fill_color=DARK_BLUE, stroke_color=DARK_BLUE, fill_opacity=1).next_to(rod4.get_end(), buff=0, direction=ORIGIN))

        self.play(self.camera.frame.animate.set(width=((l1+l2)*2 + 2)*(16/9), height=(l1+l2)*2 + 2 + 0.03*((l1+l2)*2 + 2)*(16/9)), run_time=0.001)
        self.play(Create(rod1), Create(rod2), Create(rod3), Create(rod4))
        self.play(Create(m1), Create(m2), Create(m3), Create(m4))
        self.play(Create(t_count))
        self.wait(1.5)

        for coordinate in range(len(x1)):
            group = AnimationGroup(x1tracker.animate.set_value(x1[coordinate]),
                                   y1tracker.animate.set_value(y1[coordinate]),
                                   x2tracker.animate.set_value(x2[coordinate]),
                                   y2tracker.animate.set_value(y2[coordinate]),
                                   x3tracker.animate.set_value(x3[coordinate]),
                                   y3tracker.animate.set_value(y3[coordinate]),
                                   x4tracker.animate.set_value(x4[coordinate]),
                                   y4tracker.animate.set_value(y4[coordinate]),
                                   t_tracker.animate.set_value(t[coordinate]),
                                   lag_ratio=0)
            self.play(group, rate_func=linear, run_time=1/fps)

        self.wait(3)
        print(f"Duration: {duration}s")
        print(f"Alpha: {np.degrees(alpha0_1)}")
        print(f"Beta: {np.degrees(beta0_1)}")