from manim import *
from .base import DDPMBaseMixin


class TitleSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        self.add_sound("/Users/sagi/Music/GarageBand/A.m4a")

        # 3B1B style title with elegant typography
        title = Text(
            "Denoising Diffusion",
            font="TeX Gyre Termes",
            font_size=52,
            color="#87CEEB",
            weight=BOLD,
        )
        title.move_to(UP * 1.5)

        subtitle = Text(
            "Probabilistic Models",
            font="TeX Gyre Termes",
            font_size=52,
            color="#87CEEB",
            weight=BOLD,
        )
        subtitle.next_to(title, DOWN, buff=0.2)

        # Elegant underline
        underline = Line(start=LEFT * 3, end=RIGHT * 3, color="#4A90E2", stroke_width=3)
        underline.next_to(subtitle, DOWN, buff=0.3)

        # Paper reference in smaller, elegant font
        authors = Text(
            "Ho, Jain, Abbeel (2020)",
            font="TeX Gyre Termes",
            font_size=28,
            color="#B0B0B0",
        )
        authors.next_to(underline, DOWN, buff=0.8)

        course = Text(
            "Stochastic Processes in Modern ML",
            font="TeX Gyre Termes",
            font_size=22,
            color="#808080",
        )
        course.next_to(authors, DOWN, buff=0.4)

        presenter = Text(
            "Sagi Ahrac", font="TeX Gyre Termes", font_size=22, color="#808080"
        )
        presenter.next_to(course, DOWN, buff=0.3)

        # Smooth 3B1B style animations
        self.wait(1.5)
        self.play(Write(presenter, run_time=0.75))
        self.wait(3.5)
        self.play(
            Write(title, run_time=1.5), Write(subtitle, run_time=1.5), lag_ratio=0.1
        )
        self.play(Create(underline), FadeIn(authors), FadeIn(course))
        self.wait(1)

        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(underline),
            FadeOut(authors),
            FadeOut(course),
            FadeOut(presenter),
        )

