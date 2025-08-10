from manim import *
from .base import DDPMBaseMixin


PATHS = {
    "x0": "media/images/mnist/mnist-sample-2-clean.png",
    "xt": "media/images/mnist/mnist-sample-2-little-noise.png",
    "xtt": "media/images/mnist/mnist-sample-2-more-noise.png",
    "xT": "media/images/mnist/mnist-sample-2-xT"
}

class BackwardTransitionSlide(Scene, DDPMBaseMixin):
    def image_from_path(self, path, scale=0.2):
        """Load an image from a given path and scale it."""
        img = ImageMobject(path)
        img.scale(scale)
        return img
    
    def framed_image(self, image, color=YELLOW, buff=0.05):
        """Create a framed image with a surrounding rectangle."""
        frame = SurroundingRectangle(image, color=color, buff=buff, stroke_width=2)
        framed_image = Group(image, frame)
        return framed_image
    
    def add_grid_to_image(self, image, grid_color=WHITE, opacity=0.3, lines_per_axis=8):
        """Add a grid overlay to an image."""
        # Get image bounds
        height = image.height
        width = image.width
        center = image.get_center()
        
        # Create grid lines
        grid_lines = VGroup()
        
        # Vertical lines
        for i in range(lines_per_axis + 1):
            x_pos = center[0] - width/2 + (i * width / lines_per_axis)
            line = Line(
                start=[x_pos, center[1] - height/2, 0],
                end=[x_pos, center[1] + height/2, 0],
                color=grid_color,
                stroke_width=4
            ).set_opacity(opacity)
            grid_lines.add(line)
        
        # Horizontal lines
        for i in range(lines_per_axis + 1):
            y_pos = center[1] - height/2 + (i * height / lines_per_axis)
            line = Line(
                start=[center[0] - width/2, y_pos, 0],
                end=[center[0] + width/2, y_pos, 0],
                color=grid_color,
                stroke_width=4
            ).set_opacity(opacity)
            grid_lines.add(line)
        
        return grid_lines
    
    def create_dot_vector(self, center, blue_dots=3, brown_dots=1, dot_radius=0.1, spacing=0.3):
        """Create a vector representation using colored dots."""
        total_dots = blue_dots + brown_dots
        vector_group = VGroup()
        
        # Create a list of colors to randomize
        colors = [BLUE] * blue_dots + [ORANGE] * brown_dots
        import random
        random.shuffle(colors)
        
        # Create dots with randomized colors
        for i in range(total_dots):
            y_pos = center[1] + (total_dots/2 - i - 0.5) * spacing
            dot = Circle(radius=dot_radius, color=colors[i], fill_opacity=1.0)
            dot.move_to([center[0], y_pos, 0])
            vector_group.add(dot)
        
        # Add vector brackets
        bracket_height = total_dots * spacing
        left_bracket = Line(
            start=[center[0] - 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] - 0.2, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_bracket = Line(
            start=[center[0] + 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] + 0.2, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        
        # Add bracket tops and bottoms
        left_top = Line(
            start=[center[0] - 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] - 0.15, center[1] + bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        left_bottom = Line(
            start=[center[0] - 0.2, center[1] - bracket_height/2, 0],
            end=[center[0] - 0.15, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_top = Line(
            start=[center[0] + 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] + 0.15, center[1] + bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_bottom = Line(
            start=[center[0] + 0.2, center[1] - bracket_height/2, 0],
            end=[center[0] + 0.15, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        
        brackets = VGroup(left_bracket, right_bracket, left_top, left_bottom, right_top, right_bottom)
        
        return VGroup(vector_group, brackets)
    
    def construct(self):
        self.setup_3b1b_style()

        
        x0 = self.image_from_path(PATHS["x0"], scale=0.2)
        xt = self.image_from_path(PATHS["xt"], scale=0.2)
        xtt = self.image_from_path(PATHS["xtt"], scale=0.2)
        xT = self.image_from_path(PATHS["xT"], scale=0.2)
        
        # Add yellow frames to each image
        x0 = self.framed_image(x0, color=BLUE, buff=0.05)
        xt = self.framed_image(xt, color=BLUE, buff=0.05)
        xtt = self.framed_image(xtt, color=BLUE, buff=0.05)
        xT = self.framed_image(xT, color=BLUE, buff=0.05)
        

        
        # Position images
        x0.move_to(LEFT * 4.5 + UP)
        xt.move_to(LEFT * 1.5 + UP)
        xtt.move_to(RIGHT * 1.5 + UP)
        xT.move_to(RIGHT * 4.5 + UP)
        
        # Create labels for each image
        x0_label = MathTex("x_0", font_size=24, color=WHITE)
        x0_label.next_to(x0, DOWN, buff=0.2)

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

        self.play(
            AnimationGroup(
                FadeIn(x0),
                Write(x0_label),
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
        
        # Wait a moment, then deploy grids on all images
        self.wait(1)
        
        # Create grids for all images
        x0_grid = self.add_grid_to_image(x0[0], grid_color=BLUE)  # x0[0] is the image inside the frame
        xt_grid = self.add_grid_to_image(xt[0], grid_color=BLUE)
        xtt_grid = self.add_grid_to_image(xtt[0], grid_color=BLUE)
        xT_grid = self.add_grid_to_image(xT[0], grid_color=BLUE)
        
        # Deploy all grids simultaneously
        self.play(
            AnimationGroup(
                FadeIn(x0_grid),
                FadeIn(xt_grid),
                FadeIn(xtt_grid),
                FadeIn(xT_grid),
                lag_ratio=0.1
            ),
            run_time=1.0
        )
        
        # Final wait to show the result
        self.wait(2)
        
        # Now transform all images into vectors (including x_0)
        # Create dot vector representations for all images
        # Each vector is different but doesn't show progression - just different unknown vectors
        x0_vector = self.create_dot_vector(x0.get_center(), blue_dots=4, brown_dots=0)  # x0 vector (all blue for clean representation)
        xt_vector = self.create_dot_vector(xt.get_center(), blue_dots=2, brown_dots=2)
        xtt_vector = self.create_dot_vector(xtt.get_center(), blue_dots=1, brown_dots=3)
        xT_vector = self.create_dot_vector(xT.get_center(), blue_dots=3, brown_dots=1)
        
        # Transform all images to vectors
        self.play(
            AnimationGroup(
                # Fade out all images and their grids, fade in vectors
                FadeOut(x0),
                FadeOut(x0_grid),
                FadeIn(x0_vector),
                FadeOut(xt),
                FadeOut(xt_grid),
                FadeIn(xt_vector),
                FadeOut(xtt),
                FadeOut(xtt_grid),
                FadeIn(xtt_vector),
                FadeOut(xT),
                FadeOut(xT_grid),
                FadeIn(xT_vector),
                lag_ratio=0.2
            ),
            run_time=2.0
        )
        
        self.wait(1)
        
        # Fade out all vectors except x0_vector and focus on the decoding process
        self.play(
            AnimationGroup(
                FadeOut(xt_vector),
                FadeOut(xtt_vector), 
                FadeOut(xT_vector),
                FadeOut(xt_label),
                FadeOut(xtt_label),
                FadeOut(xT_label),
                lag_ratio=0.1
            ),
            run_time=1.5
        )
        
        # Move x0_vector to the right side to make room for decoder
        self.play(
            x0_vector.animate.move_to(RIGHT * 2 + UP),
            x0_label.animate.move_to(RIGHT * 2 + UP * 0.2),
            run_time=1.0
        )
        
        # Add decoder label and arrow
        decoder_label = Text("Decoder", font_size=24, color=YELLOW)
        decoder_label.move_to(ORIGIN)
        
        decoder_arrow = Arrow(
            start=RIGHT * 1 + UP,
            end=LEFT * 1 + UP,
            color=YELLOW,
            stroke_width=4
        )
        
        self.play(
            Write(decoder_label),
            Create(decoder_arrow),
            run_time=1.0
        )
        
        # Create the decoded image on the left side
        x0_decoded = self.image_from_path(PATHS["x0"], scale=0.2)
        x0_decoded = self.framed_image(x0_decoded, color=GREEN, buff=0.05)  # Green frame to distinguish as output
        x0_decoded.move_to(LEFT * 2.5 + UP)
        x0_decoded_grid = self.add_grid_to_image(x0_decoded[0], grid_color=GREEN)
        
        # Create a new label for the decoded image
        x0_decoded_label = MathTex("\\text{Image}", font_size=20, color=GREEN)
        x0_decoded_label.next_to(x0_decoded, DOWN, buff=0.2)
        
        # Transform: show the decoder output appearing
        self.play(
            FadeIn(x0_decoded),
            FadeIn(x0_decoded_grid),
            Write(x0_decoded_label),
            run_time=1.5
        )
        

        
        # Final wait to show the transformed scene
        self.wait(3)