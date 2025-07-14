from manim import *
import numpy as np

class DDPMBaseMixin:
    """Base mixin class with shared methods for all DDPM scenes"""
    
    def setup_3b1b_style(self):
        """Set up 3Blue1Brown style background"""
        self.camera.background_color = "#0e1419"
    
    def create_image_representation(self, color, opacity=0.8, size=1.0):
        """Create a more sophisticated image representation"""
        # Main square
        square = Square(side_length=size, fill_color=color, fill_opacity=opacity)
        square.set_stroke(color=WHITE, width=2)
        
        # Add some internal structure to make it look more like an image
        internal_squares = VGroup()
        for i in range(3):
            for j in range(3):
                small_square = Square(side_length=size/4, fill_opacity=opacity*0.6)
                small_square.set_fill(color=interpolate_color(color, WHITE, 0.3*np.random.random()))
                small_square.move_to(square.get_center() + 
                                   (i-1)*size/3*RIGHT + (j-1)*size/3*UP)
                internal_squares.add(small_square)
        
        return VGroup(square, internal_squares)

    def create_noisy_image(self, noise_level, size=1.0):
        """Create a noisy image representation"""
        # Base image with reduced opacity
        base_color = interpolate_color(BLUE_B, GRAY, noise_level)
        base = Square(side_length=size, fill_color=base_color, 
                     fill_opacity=0.8*(1-noise_level))
        base.set_stroke(color=WHITE, width=2)
        
        # Add noise dots
        noise_dots = VGroup()
        num_dots = int(noise_level * 25)
        for _ in range(num_dots):
            dot = Dot(radius=0.02, color=RED)
            # Random position within the square
            x = np.random.uniform(-size/2.2, size/2.2)
            y = np.random.uniform(-size/2.2, size/2.2)
            dot.move_to(base.get_center() + x*RIGHT + y*UP)
            noise_dots.add(dot)
        
        return VGroup(base, noise_dots)
