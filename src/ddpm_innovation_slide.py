from manim import *
from .base import DDPMBaseMixin
import numpy as np


class DDPMInnovationSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        # Start with noisy corgi in the center
        corgi = ImageMobject("media/images/corgi.png")
        corgi.scale(0.15)
        corgi.set_opacity(0.4)

        # Add noise dots to noisy version
        noise_group = self.create_noise_group(
            center=corgi.get_center(),
            n_dots=25,
            x_offset=corgi.get_width() * 0.4,
            y_offset= corgi.get_height() * 0.4,
        )
        
        extra_noise_group = self.create_noise_group(
            center=corgi.get_center(),
            n_dots=35,
            x_offset=corgi.get_width() * 0.4,
            y_offset= corgi.get_height() * 0.4,
        )
        
        corgi_noisy = Group(corgi, noise_group, extra_noise_group)
        corgi_noisy.move_to(ORIGIN + UP * 1.5)

        # Show the noisy image
        self.play(FadeIn(corgi_noisy), run_time=1.5)
        self.wait(1)
        
        # Separate the extra noise group and move it aside
        corgi_denoised = Group(corgi.copy(), noise_group.copy())
        corgi_denoised.move_to(DOWN * 1.5)
        
        # Down arrow to corgi denoised
        down_arrow = Arrow(
            corgi_noisy.get_bottom() + DOWN * 0.1,
            corgi_denoised.get_top() + UP * 0.1,
            color=WHITE,
            stroke_width=3,
        )
        
        self.play(Create(down_arrow), run_time=0.5)
        self.play(FadeIn(corgi_denoised), run_time=0.5)


        # self.play(
        #     extra_noise_group.animate.shift(RIGHT * 2).scale(1.2),
        #     corgi_noisy.animate.shift(LEFT * 2),
        #     run_time=2
        # )
        
        # # Add minus between them
        # minus_sign = MathTex("-", font_size=40, color=WHITE)
        # minus_center = (corgi_denoised.get_center() + extra_noise_group.get_center()) / 2
        # minus_sign.move_to(minus_center)
        # self.play(Write(minus_sign), run_time=1)
        # self.wait(1)
        
        

        # # Create clean image and noise separately
        # corgi_clean = ImageMobject("media/images/corgi.png")
        # corgi_clean.scale(0.15)

        # # Create noise visualization
        # noise_only = Group()
        # for dot in noise_group:
        #     noise_dot = dot.copy()
        #     noise_dot.set_color("#32CD32")
        #     noise_only.add(noise_dot)

        # # Move the elements apart using move_to
        # self.play(
        #     corgi_clean.animate.move_to(LEFT * 3 + UP * 0.5),
        #     noise_only.animate.move_to(RIGHT * 1 + UP * 0.5),
        #     corgi_noisy.animate.fade(1),  # Hide the noisy version
        #     noise_group.animate.fade(1),   # Hide the original noise
        #     run_time=2
        # )

        # # Add labels
        # clean_label = MathTex("x_0", font_size=24, color=WHITE)
        # clean_label.next_to(corgi_clean, DOWN, buff=0.3)

        # noise_label = MathTex(r"\epsilon", font_size=24, color="#32CD32")
        # noise_label.next_to(noise_only, DOWN, buff=0.3)

        # self.play(
        #     Write(clean_label),
        #     Write(noise_label),
        #     run_time=1
        # )

        # # Add subtraction and equals signs
        # minus_sign = MathTex("-", font_size=40, color=WHITE)
        # minus_sign.move_to((corgi_clean.get_center() + noise_only.get_center()) / 2 + UP * 0.5)

        # equals_sign = MathTex("=", font_size=40, color=WHITE)
        # equals_sign.move_to(ORIGIN + DOWN * 1)

        # # Show the mathematical relationship
        # self.play(
        #     Write(minus_sign),
        #     Write(equals_sign),
        #     run_time=1
        # )

        # # Move the noisy image to show the result
        # result_noisy = noisy_corgi_with_noise.copy()
        # result_noisy.set_opacity(1)  # Make it fully visible
        # result_noisy.move_to(equals_sign.get_center() + DOWN * 1)

        # result_label = MathTex("x_t", font_size=24, color=WHITE)
        # result_label.next_to(result_noisy, DOWN, buff=0.3)

        # self.play(
        #     FadeIn(result_noisy),
        #     Write(result_label),
        #     run_time=1
        # )
        # self.wait(2)

        # # Fade out the mathematical demonstration
        # self.play(
        #     FadeOut(Group(
        #         corgi_clean, noise_only, clean_label, noise_label,
        #         minus_sign, equals_sign, result_noisy, result_label, noisy_label
        #     )),
        #     run_time=1.5
        # )

        # # Show the two key concepts
        # concepts_title = Text("Unifying Two Key Concepts",
        #                      font="TeX Gyre Termes", font_size=32, color="#DDA0DD")
        # concepts_title.move_to(ORIGIN + UP * 2)

        # self.play(Write(concepts_title), run_time=1.5)
        # self.wait(1)

        # # Create concept boxes with no fill color, only colored frames
        # diffusion_box = RoundedRectangle(
        #     width=4, height=2, corner_radius=0.1,
        #     fill_opacity=0, stroke_color="#FF6B6B", stroke_width=3
        # )
        # diffusion_text = Text("Diffusion\\nModels", font_size=24, color=WHITE, weight=BOLD)
        # diffusion_text.move_to(diffusion_box)
        # diffusion_group = VGroup(diffusion_box, diffusion_text).move_to(LEFT * 3)

        # score_box = RoundedRectangle(
        #     width=4, height=2, corner_radius=0.1,
        #     fill_opacity=0, stroke_color="#87CEEB", stroke_width=3
        # )
        # score_text = Text("Denoising Score\\nMatching", font_size=24, color=WHITE, weight=BOLD)
        # score_text.move_to(score_box)
        # score_group = VGroup(score_box, score_text).move_to(RIGHT * 3)

        # # Show the concepts
        # self.play(
        #     FadeIn(diffusion_group),
        #     FadeIn(score_group),
        #     run_time=2
        # )
        # self.wait(1)

        # # Create straight arrows connecting them in a cycle
        # arrow1 = Arrow(
        #     start=diffusion_group.get_right() + RIGHT * 0.1,
        #     end=score_group.get_left() + LEFT * 0.1,
        #     color="#FFD700", stroke_width=4,
        #     tip_length=0.3
        # )

        # arrow2 = Arrow(
        #     start=score_group.get_left() + LEFT * 0.1 + DOWN * 0.5,
        #     end=diffusion_group.get_right() + RIGHT * 0.1 + DOWN * 0.5,
        #     color="#FFD700", stroke_width=4,
        #     tip_length=0.3
        # )

        # # Show the arrows creating a cycle
        # self.play(
        #     Create(arrow1),
        #     run_time=1.5
        # )
        # self.wait(0.5)

        # self.play(
        #     Create(arrow2),
        #     run_time=1.5
        # )

        # # Final emphasis
        # self.play(
        #     diffusion_group.animate.set_stroke(width=5),
        #     score_group.animate.set_stroke(width=5),
        #     run_time=1
        # )

        # self.wait(2)

        # # Fade everything out
        # self.play(
        #     FadeOut(Group(
        #         title, concepts_title, diffusion_group, score_group, arrow1, arrow2
        #     )),
        #     run_time=2
        # )

        # self.wait(1)
