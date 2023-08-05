from equationsolver_double_pendulum import sol1
from equationsolver_double_pendulum import fps
from manim import *
import numpy as np


class DoublePendulum(Scene):
    def construct(self):

        alpha_tracker = ValueTracker(0)
        beta_tracker = ValueTracker(0)
        angles_alpha = sol1.T[0]
        angles_beta = sol1.T[1]
        rod1 = always_redraw(lambda: Line([0, 0, 0], [2*np.sin(alpha_tracker.get_value()), 2-2*np.cos(alpha_tracker.get_value()), 0]))
        rod2 = always_redraw(lambda: Line([0, -2, 0], [2*np.sin(beta_tracker.get_value()), -2*np.cos(beta_tracker.get_value()), 0]).next_to(rod1.get_end(), buff=0, aligned_edge=UP))
        m1 = always_redraw(lambda: Circle(radius=0.1, color=RED, fill_color=RED, fill_opacity=1).next_to(rod1.get_end(), buff=0, direction=ORIGIN))
        m2 = always_redraw(lambda: Circle(radius=0.1, color=RED, fill_color=DARK_BLUE, stroke_color=DARK_BLUE, fill_opacity=1).next_to(rod2.get_end(), buff=0, direction=ORIGIN))

        self.play(Create(rod1), Create(rod2))
        self.play(Create(m1), Create(m2))

        for angle in range(len(angles_alpha)):

            if angle != 0:
                self.play(beta_tracker.animate.set_value(angles_beta[angle]), rate_func=linear, run_time=1/(2*fps))
                self.play(alpha_tracker.animate.set_value(angles_alpha[angle]), rate_func=linear, run_time=1/(2*fps))

            else:
                self.play(beta_tracker.animate.set_value(angles_beta[angle]), rate_func=smooth, run_time=1)
                self.play(alpha_tracker.animate.set_value(angles_alpha[angle]), rate_func=smooth, run_time=1)
                self.wait(1)

        self.wait(3)