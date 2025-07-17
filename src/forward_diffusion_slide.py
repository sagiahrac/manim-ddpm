from manim import *
from .base import DDPMBaseMixin


class ForwardDiffusionSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        # Section title with 3B1B styling
        title = Text(
            "Forward Process: Adding Noise",
            font="TeX Gyre Termes",
            font_size=36,
            color="#FFD700",
        )
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))

        # Create smooth image representations
        image_size = 1.2

        # Original "image" - more sophisticated representation
        original = self.create_image_representation(
            BLUE_B, opacity=0.9, size=image_size
        )
        original.move_to(LEFT * 5)

        # Label with mathematical notation
        x0_label = MathTex("x_0", font_size=24, color=WHITE)
        x0_label.next_to(original, DOWN, buff=0.3)

        self.play(FadeIn(original, scale=0.8), Write(x0_label))

        # Create noise progression with smooth transitions
        images = [original]
        labels = [x0_label]

        positions = [LEFT * 3, LEFT * 1, RIGHT * 1, RIGHT * 3, RIGHT * 5]
        noise_levels = [0.2, 0.4, 0.6, 0.8, 1.0]

        for i, (pos, noise) in enumerate(zip(positions, noise_levels)):
            # Create increasingly noisy image
            noisy_img = self.tmp_create_noisy_image(noise, size=image_size)
            noisy_img.move_to(pos)

            # Mathematical label
            label = MathTex(f"x_{{{i + 1}}}", font_size=24, color=WHITE)
            label.next_to(noisy_img, DOWN, buff=0.3)

            # Smooth curved arrow
            arrow = CurvedArrow(
                images[-1].get_right() + RIGHT * 0.1,
                noisy_img.get_left() + LEFT * 0.1,
                color="#FF6B6B",
                stroke_width=3,
            )

            # Add noise equation above arrow
            if i == 0:
                noise_eq = MathTex(r"+\varepsilon", font_size=20, color="#FF6B6B")
                noise_eq.next_to(arrow, UP, buff=0.1)
                self.play(
                    Create(arrow),
                    FadeIn(noisy_img, scale=0.8),
                    Write(label),
                    Write(noise_eq),
                    run_time=1.5,
                )
            else:
                self.play(
                    Create(arrow),
                    FadeIn(noisy_img, scale=0.8),
                    Write(label),
                    run_time=1.2,
                )

            images.append(noisy_img)
            labels.append(label)

        # Mathematical formulation
        forward_eq = MathTex(
            r"q(x_t|x_{t-1}) = \mathcal{N}(\sqrt{1-\beta_t}x_{t-1}, \beta_t I)",
            font_size=32,
            color="#87CEEB",
        )
        forward_eq.to_edge(DOWN, buff=1)

        # Highlight the key parts
        self.play(Write(forward_eq))

        # Add explanation box
        explanation = Text(
            "Each step adds Gaussian noise", font_size=20, color="#B0B0B0"
        )
        explanation.next_to(forward_eq, UP, buff=0.3)
        self.play(Write(explanation))

        self.wait(3)
