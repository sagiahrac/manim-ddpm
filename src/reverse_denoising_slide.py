from manim import *
from .base import DDPMBaseMixin


class ReverseDenoisingSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        # Title
        title = Text(
            "Reverse Process: Learned Denoising",
            font="TeX Gyre Termes",
            font_size=36,
            color="#90EE90",
        )
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))

        # Start with pure noise
        noise_img = self.tmp_create_noisy_image(1.0, size=1.2)
        noise_img.move_to(LEFT * 5)

        noise_label = MathTex("x_T", font_size=24, color=WHITE)
        noise_label.next_to(noise_img, DOWN, buff=0.3)

        self.play(FadeIn(noise_img, scale=0.8), Write(noise_label))

        # Neural network representation
        nn_box = Rectangle(width=1.5, height=2, color="#FF9500", fill_opacity=0.2)
        nn_box.move_to(UP * 1.5)
        nn_text = Text("Neural\nNetwork", font_size=16, color="#FF9500")
        nn_text.move_to(nn_box.get_center())

        self.play(Create(nn_box), Write(nn_text))

        # Show denoising steps
        positions = [LEFT * 3, LEFT * 1, RIGHT * 1, RIGHT * 3, RIGHT * 5]
        noise_levels = [0.8, 0.6, 0.4, 0.2, 0.0]

        images = [noise_img]

        for i, (pos, noise) in enumerate(zip(positions, noise_levels)):
            if noise == 0.0:
                # Final clean image
                clean_img = self.create_image_representation(BLUE_B, size=1.2)
            else:
                clean_img = self.tmp_create_noisy_image(noise, size=1.2)

            clean_img.move_to(pos)

            label = MathTex(f"x_{{{4 - i}}}", font_size=24, color=WHITE)
            label.next_to(clean_img, DOWN, buff=0.3)

            # Arrow from neural network
            nn_arrow = Arrow(
                nn_box.get_bottom(),
                clean_img.get_top(),
                color="#90EE90",
                stroke_width=3,
            )

            # Arrow between images
            img_arrow = CurvedArrow(
                images[-1].get_right() + RIGHT * 0.1,
                clean_img.get_left() + LEFT * 0.1,
                color="#90EE90",
                stroke_width=3,
            )

            self.play(
                Create(img_arrow),
                Create(nn_arrow),
                FadeIn(clean_img, scale=0.8),
                Write(label),
                run_time=1.5,
            )
            self.play(FadeOut(nn_arrow), run_time=0.5)

            images.append(clean_img)

        # Mathematical formulation
        reverse_eq = MathTex(
            r"p_\theta(x_{t-1}|x_t) = \mathcal{N}(\mu_\theta(x_t, t), \Sigma_\theta(x_t, t))",
            font_size=28,
            color="#90EE90",
        )
        reverse_eq.to_edge(DOWN, buff=1)
        self.play(Write(reverse_eq))

        self.wait(3)
