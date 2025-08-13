from manim import *
from .base import DDPMBaseMixin


class DiffusionIntroSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        self.add_sound("media/videos/individual_scenes/1080p60/B_DiffusionIntroSlideScene-enhanced-v2.wav")
        # self.wait(10)

        models_group = VGroup()

        # GANs
        gan_box = RoundedRectangle(
            width=1.5,
            height=0.8,
            corner_radius=0.1,
            fill_color="#FF6B6B",
            fill_opacity=0.3,
            stroke_color="#FF6B6B",
        )
        gan_text = Text("GANs", font_size=20, color=WHITE)
        gan_text.move_to(gan_box)
        
        gan_group = VGroup(gan_box, gan_text).move_to(LEFT * 3)

        # Diffusion Models (highlighted) - now in the middle
        diff_box = RoundedRectangle(
            width=1.8,
            height=0.8,
            corner_radius=0.1,
            fill_color="#FFD700",
            fill_opacity=0.5,
            stroke_color="#FFD700",
            stroke_width=3,
        )
        diff_text = Text("Diffusion\nModels", font_size=18, color=BLACK, weight=BOLD)
        diff_text.move_to(diff_box)
        
        diff_group = VGroup(diff_box, diff_text).move_to(ORIGIN)

        # VAEs - now on the right
        vae_box = RoundedRectangle(
            width=1.5,
            height=0.8,
            corner_radius=0.1,
            fill_color="#87CEEB",
            fill_opacity=0.3,
            stroke_color="#87CEEB",
        )
        vae_text = Text("VAEs", font_size=20, color=WHITE)
        vae_text.move_to(vae_box)
        
        vae_group = VGroup(vae_box, vae_text).move_to(RIGHT * 3)

        models_group.add(gan_group, vae_group, diff_group) 

        self.play(FadeIn(diff_group), run_time=1.2)  # Diffusion models appear first
        self.wait(2.7)
        self.play(FadeIn(gan_group), run_time=0.8)   # Then GANs
        self.play(FadeIn(vae_group), run_time=0.8)   # Finally VAEs

        # Highlight diffusion models
        # self.play(diff_group.animate.scale(1.2), run_time=0.8)
        # self.play(diff_group.animate.scale(1 / 1.2), run_time=0.8)

        # Diffusion box "kicks" the other boxes off screen
        # Since diffusion is now in the center, it will kick both directions
        # First, diffusion box prepares - slight scale up
        self.play(diff_group.animate.scale(1.1), run_time=0.4)
        
        # Quick "wind up" animation - diffusion box rotates slightly
        self.play(diff_group.animate.rotate(0.15), run_time=0.3)
        
        # The kick! Diffusion box expands/pulses while others get pushed off
        kick_animations = [
            diff_group.animate.scale(1.3).rotate(-0.15),      # Diffusion expands from center
            gan_group.animate.shift(LEFT * 10).rotate(2),     # GAN flies off left with spin
            vae_group.animate.shift(RIGHT * 10).rotate(-2)    # VAE flies off right with spin
        ]
        self.play(*kick_animations, run_time=0.8)
        
        # Diffusion box settles back to normal size
        self.play(diff_group.animate.scale(1/1.3), run_time=0.3)
        
        # Victory pose - slight scale up and down
        self.play(diff_group.animate.scale(1.1), run_time=0.4)
        self.play(diff_group.animate.scale(1/1.1), run_time=0.4)
        
        # Now fade out the diffusion box
        self.play(FadeOut(diff_group), run_time=0.8)

        self.wait(1)

        # Visual: "that aim to generate samples from complex data distributions"
        # Show complex data distribution
        complex_dist = VGroup()

        # Create a complex, multi-modal distribution
        for i in range(200):
            # Multiple clusters to show complexity
            cluster = np.random.choice([0, 1, 2])
            if cluster == 0:
                # Spiral pattern
                t = np.random.uniform(0, 4 * PI)
                r = 0.1 * t + np.random.normal(0, 0.1)
                x = r * np.cos(t) * 0.3
                y = r * np.sin(t) * 0.3
            elif cluster == 1:
                # Circular cluster
                angle = np.random.uniform(0, 2 * PI)
                radius = np.random.normal(1.5, 0.2)
                x = radius * np.cos(angle) * 0.4
                y = radius * np.sin(angle) * 0.4
            else:
                # Linear cluster
                x = np.random.normal(0, 0.2)
                y = np.random.normal(-1.5, 0.1) + x * 0.5

            point = Dot(
                [x, y, 0],
                radius=0.03,
                color=interpolate_color(BLUE, PURPLE, np.random.random()),
            )
            complex_dist.add(point)

        complex_dist.move_to(ORIGIN)

        self.play(
            LaggedStart(
                *[FadeIn(point, scale=0.5) for point in complex_dist],
                lag_ratio=0.01,
                run_time=3,
            )
        )

        self.wait(1)

        # Visual: "learn to create realistic new data that looks like the data they were trained on"
        # Show generation process

        # Move original data to left
        self.play(complex_dist.animate.move_to(LEFT * 3).scale(0.7))

        # Add labels
        original_label = Text("Training Data", font_size=20, color=WHITE)
        original_label.next_to(complex_dist, DOWN, buff=0.3)
        self.play(Write(original_label))

        # Show arrow and "learning" process
        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, color="#FFD700", stroke_width=4)
        learning_text = Text("Learn", font_size=24, color="#FFD700", weight=BOLD)
        learning_text.next_to(arrow, UP, buff=0.2)

        self.play(Create(arrow), Write(learning_text))

        # Generate new samples that look similar
        new_samples = VGroup()
        for i in range(150):
            # Similar distribution but with slight variations
            cluster = np.random.choice([0, 1, 2])
            if cluster == 0:
                t = np.random.uniform(0, 4 * PI)
                r = 0.1 * t + np.random.normal(0, 0.15)  # Slightly more variation
                x = r * np.cos(t) * 0.3
                y = r * np.sin(t) * 0.3
            elif cluster == 1:
                angle = np.random.uniform(0, 2 * PI)
                radius = np.random.normal(1.5, 0.25)  # Slightly more variation
                x = radius * np.cos(angle) * 0.4
                y = radius * np.sin(angle) * 0.4
            else:
                x = np.random.normal(0, 0.25)  # Slightly more variation
                y = np.random.normal(-1.5, 0.15) + x * 0.5

            point = Dot(
                [x, y, 0],
                radius=0.03,
                color=interpolate_color(GREEN, YELLOW, np.random.random()),
            )
            new_samples.add(point)

        new_samples.move_to(RIGHT * 3).scale(0.7)

        # Animate generation
        self.play(
            LaggedStart(
                *[FadeIn(point, scale=0.5) for point in new_samples],
                lag_ratio=0.01,
                run_time=2.5,
            )
        )

        new_label = Text("Generated Data", font_size=20, color="#90EE90")
        new_label.next_to(new_samples, DOWN, buff=0.3)
        self.play(Write(new_label))

        self.wait(2)

        # Fade out all elements
        self.play(
            FadeOut(complex_dist),
            FadeOut(original_label),
            FadeOut(arrow),
            FadeOut(learning_text),
            FadeOut(new_samples),
            FadeOut(new_label),
        )
