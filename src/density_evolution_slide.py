from manim import *
from .base import DDPMBaseMixin


class DensityEvolutionSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        # Load density images
        density_30 = ImageMobject("/Users/sagi/repos/education/manim-ddpm/ddpm_density_step_30.png")
        density_20 = ImageMobject("/Users/sagi/repos/education/manim-ddpm/ddpm_density_step_20.png")
        density_10 = ImageMobject("/Users/sagi/repos/education/manim-ddpm/ddpm_density_step_10.png")
        density_0 = ImageMobject("/Users/sagi/repos/education/manim-ddpm/ddpm_density_step_0.png")
        
        # Scale images appropriately
        for img in [density_30, density_20, density_10, density_0]:
            img.scale(0.6)
        
        # Position the first image (step 30) on the right side with proper spacing
        density_30.move_to(RIGHT * 4.5)
        
        # Create label for step 30 using LaTeX notation
        label_30 = MathTex("p_{\\theta}(x_T)", font_size=24, color=WHITE)
        label_30.next_to(density_30, DOWN, buff=0.3)
        

        # Introduce step 30 (pure noise) from the right
        self.play(
            FadeIn(density_30),
            Write(label_30),
            run_time=1.2
        )
        self.wait(1)

        xt = Dot(radius=0.035, color=RED)
        target_point = interpolate(density_30.get_top(), density_30.get_bottom(), 0.35)
        xt.move_to(target_point)
        self.play(FadeIn(xt), run_time=0.5)


        # Add description for step 30
        noise_desc = MathTex("\\approx \\mathcal{N}(0, I)", font_size=18, color=GRAY)
        noise_desc.next_to(label_30, DOWN, buff=0.2)
        self.play(Write(noise_desc), run_time=0.8)
        self.wait(1)
        
        # Move step 30 to final position and introduce step 20
        density_20.move_to(RIGHT * 1.5)
        label_20 = MathTex("p_{\\theta}(\cdot |x_{t_2})", font_size=24, color=WHITE)
        label_20.next_to(density_20, DOWN, buff=0.3)
        
        self.play(
            density_30.animate.move_to(RIGHT * 4.5),
            FadeIn(density_20),
            Write(label_20),
            run_time=1.5
        )
        self.wait(0.8)
        
        # Move previous images and introduce step 10
        density_10.move_to(LEFT * 1.5)
        label_10 = MathTex("p_{\\theta}(\cdot |x_{t_1})", font_size=24, color=WHITE)
        label_10.next_to(density_10, DOWN, buff=0.3)
        
        self.play(
            density_20.animate.move_to(RIGHT * 1.5),
            FadeIn(density_10),
            Write(label_10),
            run_time=1.5
        )
        self.wait(0.8)
        
        # Finally introduce step 0 (original distribution)
        density_0.move_to(LEFT * 4.5)
        label_0 = MathTex("p_{\\theta}(x_0|x_1)", font_size=24, color=WHITE)
        label_0.next_to(density_0, DOWN, buff=0.3)
        
        self.play(
            density_10.animate.move_to(LEFT * 1.5),
            FadeIn(density_0),
            Write(label_0),
            run_time=1.8
        )
        self.wait(1)
        
        # Add description for step 0
        original_desc = Text("Original Data", font_size=18, color=GREEN)
        original_desc.next_to(label_0, DOWN, buff=0.2)
        self.play(Write(original_desc), run_time=0.8)
        self.wait(1)
        
        # Add arrows showing the progression with proper spacing
        arrow_1 = Arrow(
            density_0.get_right() + UP * 0.1,
            density_10.get_left() + UP * 0.1,
            color=YELLOW,
            stroke_width=3,
            buff=0.1
        )
        
        arrow_2 = Arrow(
            density_10.get_right() + UP * 0.1,
            density_20.get_left() + UP * 0.1,
            color=YELLOW,
            stroke_width=3,
            buff=0.1
        )
        
        arrow_3 = Arrow(
            density_20.get_right() + UP * 0.1,
            density_30.get_left() + UP * 0.1,
            color=YELLOW,
            stroke_width=3,
            buff=0.1
        )
        
        # Add "Forward Process" label
        forward_label = Text("Forward Process", font_size=20, color=YELLOW)
        forward_label.move_to(UP * 1.2)
        
        self.play(
            Create(arrow_1),
            Create(arrow_2),
            Create(arrow_3),
            Write(forward_label),
            run_time=2
        )
        self.wait(1)
        
        # Highlight the transformation
        self.play(
            density_0.animate.set_opacity(0.3),
            density_10.animate.set_opacity(0.3),
            density_20.animate.set_opacity(0.3),
            density_30.animate.set_opacity(1).scale(1.2),
            run_time=1
        )
        
        self.play(
            density_30.animate.scale(1/1.2),
            density_0.animate.set_opacity(1),
            density_10.animate.set_opacity(1),
            density_20.animate.set_opacity(1),
            run_time=1
        )
        
        # Add final message
        final_message = Text(
            "Reverse process learns to denoise step by step",
            font_size=22,
            color=WHITE
        )
        final_message.move_to(DOWN * 2.5)
        
        self.play(Write(final_message), run_time=1.5)
        self.wait(2)
        
        # Fade out everything
        all_objects = Group(
            density_30, density_20, density_10, density_0,
            label_30, label_20, label_10, label_0,
            noise_desc, original_desc, arrow_1, arrow_2, arrow_3,
            forward_label, final_message
        )
        
        self.play(FadeOut(all_objects), run_time=2)
