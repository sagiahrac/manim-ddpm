

from manim import *
from .base import DDPMBaseMixin


PATHS = {
    "x0": "media/images/mnist/mnist-sample-2-clean.png",
    "xt": "media/images/mnist/mnist-sample-2-little-noise.png",
    "xtt": "media/images/mnist/mnist-sample-2-more-noise.png",
    "xT": "media/images/mnist/mnist-sample-2-xT"
}

class ChairsZoomSlide(Scene, DDPMBaseMixin):
    
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
        # self.add_sound("ForwardDiffusionSlideScene-enhanced-v2.wav")
        
        # Load images
        x0_init = self.image_from_path(PATHS["x0"], scale=0.5)
        x0_init = self.framed_image(x0_init, color=YELLOW, buff=0.05)
        

        x0_init.move_to(ORIGIN)
        
        # First: Fade in at center
        self.play(FadeIn(x0_init), run_time=1)