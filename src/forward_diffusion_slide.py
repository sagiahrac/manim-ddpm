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
        xt_label = MathTex("x_t", font_size=24, color=WHITE)
        xt_label.next_to(xt, DOWN, buff=0.2)
        
        xtt_label = MathTex("x_{t+1}", font_size=24, color=WHITE)
        xtt_label.next_to(xtt, DOWN, buff=0.2)
        
        xT_label = MathTex("x_T", font_size=24, color=WHITE)
        xT_label.next_to(xT, DOWN, buff=0.2)
        
        # Show images with labels using lag_ratio for staggered appearance
        right_arrow = Arrow(
            x0.get_center() + UP*1.5 + LEFT * 0.4,
            xT.get_center() + UP*1.5 + RIGHT * 0.4,
            color=GREEN,
            stroke_width=3,
        )
            
        self.play(
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
        
        
        
