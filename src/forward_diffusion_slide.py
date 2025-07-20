from manim import *
from .base import DDPMBaseMixin


PATHS = {
    "x0": "media/images/mnist/mnist-sample-2-clean.png",
    "xt": "media/images/mnist/mnist-sample-2-little-noise.png",
    "xtt": "media/images/mnist/mnist-sample-2-more-noise.png",
    "xT": "media/images/mnist/mnist-sample-2-xT"
}

class ForwardDiffusionSlide(Scene, DDPMBaseMixin):
    
    def image_from_path(self, path, scale=0.2):
        """Load an image from a given path and scale it."""
        img = ImageMobject(path)
        img.scale(scale)
        return img
    
    def framed_image(self, image, color=YELLOW, buff=0.05):
        """Create a framed image with a surrounding rectangle."""
        frame = SurroundingRectangle(image, color=color, buff=buff)
        framed_image = Group(image, frame)
        return framed_image
    
    def construct(self):
        self.setup_3b1b_style()
        
        # Load images
        x0 = self.image_from_path(PATHS["x0"], scale=0.5)
        x0 = self.framed_image(x0, color=YELLOW, buff=0.05)
        

        # Start x0 with 0 opacity at the center
        x0.move_to(ORIGIN).set_opacity(0)
        
        # Create the label
        x0_label = MathTex("x_0", font_size=24, color=WHITE)
        x0_label.move_to(LEFT * 4.5 + DOWN * 1.2)
        
        # First: Fade in at center
        self.play(x0.animate.set_opacity(1), run_time=1)
        
        # Hold for 1 second
        self.wait(1)
        
        # Then: Move to left and scale down
        self.play(
            AnimationGroup(
                x0.animate.move_to(LEFT * 4.5).scale(0.4),
                Write(x0_label),
                lag_ratio=0.3
            ),
            run_time=1.5
        )
        
        self.wait(1)
        
        forward_label = Text("Forward\n Process", font_size=24, color=GREEN)
        forward_label.next_to(x0, UP + LEFT * 0.4, buff=0.5)
        
        self.play(FadeIn(forward_label))

        
        
        xt = self.image_from_path(PATHS["xt"], scale=0.2)
        xtt = self.image_from_path(PATHS["xtt"], scale=0.2)
        xT = self.image_from_path(PATHS["xT"], scale=0.2)
        
        # Add yellow frames to each image
        xt = self.framed_image(xt, color=YELLOW, buff=0.05)
        xtt = self.framed_image(xtt, color=YELLOW, buff=0.05)
        xT = self.framed_image(xT, color=YELLOW, buff=0.05)
        
        # Position images
        xt.move_to(LEFT * 1.5)
        xtt.move_to(RIGHT * 1.5)
        xT.move_to(RIGHT * 4.5)
        
        # Create labels for each image
        xt_label = MathTex("x_{t-1}", font_size=24, color=WHITE)
        xt_label.next_to(xt, DOWN, buff=0.2)
        
        xtt_label = MathTex("x_t", font_size=24, color=WHITE)
        xtt_label.next_to(xtt, DOWN, buff=0.2)
        
        xT_label = MathTex("x_T", font_size=24, color=WHITE)
        xT_label.next_to(xT, DOWN, buff=0.2)
        
        # Create framed text for x_0 ~ q(x_0) at the left tip of the arrow
        x0_distribution = MathTex("x_0 \\sim q(x_0)", font_size=22, color=WHITE)
        x0_frame = SurroundingRectangle(
            x0_distribution, 
            color=GREEN, 
            buff=0.15,
            fill_opacity=1.0,
            fill_color=self.camera.background_color,
            stroke_width=3
        )
        x0_framed_text = VGroup(x0_frame, x0_distribution)  # Frame first, then text on top
        
        # Position it at the left tip of the arrow (overlapping)
        x0_framed_text.move_to(x0.get_center() + UP*1.5)  # Slightly to the left of arrow start

        # Compute the right edge of the frame (not just the text)
        frame_right = x0_frame.get_right()
        # Extend the arrow a bit further to the right so it looks like it goes out of the frame
        arrow_end = xT.get_center() + UP*1.5 + RIGHT * 1.2  # Increase RIGHT offset

        right_arrow = Arrow(
            frame_right,
            arrow_end,
            color=GREEN,
            stroke_width=3,
            buff=0,  # No gap at start/end
            max_tip_length_to_length_ratio=0.025  # Make tip smaller
        )
        self.play(
            FadeIn(x0_framed_text),
            Write(right_arrow),
            AnimationGroup(
                FadeIn(xt),
                Write(xt_label),
                FadeIn(xtt),
                Write(xtt_label),
                FadeIn(xT),
                Write(xT_label),
                lag_ratio=0.3
            ),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Create another framed text for q(x_t}|x_{t-1}) in the middle of the arrow
        transition_distribution = MathTex("q(x_t|x_{t-1})", font_size=20, color=WHITE)
        transition_frame = SurroundingRectangle(
            transition_distribution, 
            color=GREEN, 
            buff=0.12,
            fill_opacity=1.0,
            fill_color=self.camera.background_color,
            stroke_width=3
        )
        transition_framed_text = VGroup(transition_frame, transition_distribution)
        
        # Position it in the middle between xt and xtt images at arrow height
        middle_position = (xt.get_center() + xtt.get_center()) / 2 + UP*1.5
        transition_framed_text.move_to(middle_position)
        
        forward_step_arrow = Arrow(
            xt.get_right() + UP * 0.1,
            xtt.get_left() + UP * 0.1,
            color=GREEN,
            stroke_width=3,
            buff=0.2,
            max_tip_length_to_length_ratio=0.15  # Make tip smaller
        )
        
        # Add dots to show progression between images
        # Dots between x0 and xt
        left_dots = VGroup()
        for i in range(3):
            dot = Dot(color=WHITE, radius=0.03)
            dot.move_to((x0.get_center() + xt.get_center()) / 2 + LEFT * 0.3 + RIGHT * i * 0.2)
            left_dots.add(dot)
        
        # Dots between xtt and xT  
        right_dots = VGroup()
        for i in range(3):
            dot = Dot(color=WHITE, radius=0.03)
            dot.move_to((xtt.get_center() + xT.get_center()) / 2 + LEFT * 0.3 + RIGHT * i * 0.2)
            right_dots.add(dot)
        
        self.play(
            FadeIn(transition_framed_text),
            Create(forward_step_arrow),
            FadeIn(left_dots),
            FadeIn(right_dots),
            run_time=1.0
        )
        
        self.wait(1)
        
        # Add the step-wise transition formula
        step_formula = MathTex(
            "q(x_t | x_{t-1}) = \\mathcal{N}(x_t; \\sqrt{1-\\beta_t} x_{t-1}, \\beta_t I)",
            font_size=32,
            color=WHITE
        )

        step_formula.move_to(DOWN * 2)
        
        
        betas = MathTex(
            "0 < \\beta_t \ll 1",
            font_size=32, 
            color=WHITE
        )
        
        betas.next_to(step_formula, DOWN, buff=0.5)

        # direct_formula.move_to(DOWN * 2.8)
        
        self.play(
            FadeIn(step_formula),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        self.play(
            FadeIn(betas),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Highlight and emphasize the √(1-β_t) term
        # Animation sequence: highlight, enlarge, then return to normal
        self.play(
            step_formula[0][16:26].animate.set_color(GREEN),  # Highlight just the √(1-β_t) part
            run_time=1.0
        )
        
        self.wait(0.5)
        
        self.play(
            step_formula[0][16:22].animate.scale(0.7),
            run_time=0.8
        )
        
        self.play(
            step_formula[0][16:22].animate.scale(1/0.7),
            run_time=0.8
        )
        
        self.play(
            step_formula[0][16:26].animate.set_color(WHITE),  # Highlight just the √(1-β_t) part
            step_formula[0][27:29].animate.set_color(GREEN),  # Highlight just the β_t part
            run_time=1.0
        )
        
        self.wait(1)
        
        self.play(
            step_formula[0][27:29].animate.set_color(WHITE),  # Reset color
            run_time=1.0
        )
        
        self.wait(1)
        
        # Fade out the step formula and betas
        self.play(
            FadeOut(step_formula),
            FadeOut(betas),
            run_time=1.5
        )
        
        self.wait(0.5)
        
        # Add the direct transition formula
        direct_formula = MathTex(
            "q(x_t | x_0) = \\mathcal{N}(x_t; \\sqrt{\\bar{\\alpha}_t} x_0, (1-\\bar{\\alpha}_t) I)",
            font_size=32,
            color=WHITE
        )
        direct_formula.move_to(DOWN * 2)
        
        # Fade in the direct formula
        self.play(
            FadeIn(direct_formula),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Add definition of alpha bar (first part only)
        alpha_definition_part1 = MathTex(
            "\\bar{\\alpha}_t = \\prod_{s=1}^{t}(1-\\beta_s)",
            font_size=28,
            color=WHITE
        )
        alpha_definition_part1.next_to(direct_formula, DOWN, buff=0.5)
        
        # Add the arrow and limit (second part)
        alpha_definition_part2 = MathTex(
            "\\xrightarrow[t \\to \\infty]{} 0",
            font_size=28,
            color=WHITE
        )
        alpha_definition_part2.next_to(alpha_definition_part1, RIGHT, buff=0.1)
        
        self.play(
            FadeIn(alpha_definition_part1),
            run_time=1.5
        )
        
        self.wait(1)
        
        self.play(
            FadeIn(alpha_definition_part2),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Add convergence to normal distribution
        convergence_arrow = MathTex(
            "\\sim \\mathcal{N}(0, I)",
            font_size=26,
            color=GRAY
        )
        convergence_arrow.next_to(direct_formula, RIGHT, buff=0.3)
        
        self.play(
            FadeIn(convergence_arrow),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Create a framed box with the convergence formula
        convergence_formula = MathTex(
            "x_T \\mathrel{\\dot{\\sim}} \\mathcal{N}(0, I)",
            font_size=20,
            color=WHITE
        )
        convergence_frame = SurroundingRectangle(
            convergence_formula,
            color=GREEN,
            buff=0.12,
            fill_opacity=1.0,
            fill_color=self.camera.background_color,
            stroke_width=3
        )
        convergence_framed = VGroup(convergence_frame, convergence_formula)
        
        # Position it above X_T image
        convergence_framed.move_to(xT.get_center() + UP * 1.5)
        
        self.play(
            FadeTransform(convergence_arrow, convergence_framed),
            run_time=2.0
        )
        
